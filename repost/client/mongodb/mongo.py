import logging

from pymongo import MongoClient

from repost.domain.clients.mongo_client_user import MongoClientUser


class MongoDBClient:
    def __init__(self, mongo_client_user: MongoClientUser):
        self.mongo_client_user = mongo_client_user

    def get_not_uploaded_posts(self, reddit_post_ids: list[str]) -> list[str]:
        logging.info(f"Checking if some of the {len(reddit_post_ids)} post do not exist in the database...")

        with MongoClient(self.mongo_client_user.url) as client:
            upload_db = client[self.mongo_client_user.db_name][self.mongo_client_user.db_table_name]
            posts_in_db = list(upload_db.find({self.mongo_client_user.db_key_field: {"$in": reddit_post_ids}}))

        not_found_ids = [post_id for post_id in reddit_post_ids if
                         post_id not in (post[self.mongo_client_user.db_key_field] for post in posts_in_db)]

        logging.info(f"{len(not_found_ids)} posts do not exist in the database")
        return not_found_ids

    def insert_post_in_db(self, reddit_post_id: str) -> None:
        logging.info(f"Uploading the repost info (id={reddit_post_id}) to the database...")

        with MongoClient(self.mongo_client_user.url) as client:
            upload_db = client[self.mongo_client_user.db_name][self.mongo_client_user.db_table_name]
            upload_db.insert_one({self.mongo_client_user.db_key_field: reddit_post_id})

        logging.info(f"Repost info (id={reddit_post_id}) uploaded to the database")
