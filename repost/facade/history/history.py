import logging

from repost.client.mongodb.mongo import MongoDBClient
from repost.domain.clients.mongo_client_user import MongoClientUser
from repost.domain.reddit_post import RedditPost
from repost.exception.no_posts_found_exception import NoPostsFoundException


class HistoryManager:
    def __init__(self, mongo_client_user: MongoClientUser):
        self.mongo_db_client = MongoDBClient(mongo_client_user)

    def filter_not_reposted_posts(self, reddit_posts: list[RedditPost]) -> list[RedditPost]:
        posts_ids = [post.id for post in reddit_posts]
        logging.info(f"Filtering if in {len(posts_ids)} posts are available posts to repost...")

        not_uploaded_ids = set(self.mongo_db_client.get_not_uploaded_posts(posts_ids))

        not_uploaded_posts = list(filter(lambda post: post.id in not_uploaded_ids, reddit_posts))

        if not not_uploaded_posts:
            logging.error("No found not uploaded posts")
            raise NoPostsFoundException

        logging.info(f"{len(not_uploaded_posts)} posts are available to repost")
        return not_uploaded_posts

    def save_repost_in_history(self, reddit_post: RedditPost) -> None:
        logging.info(f"Saving the repost of the post with id {reddit_post.id} in the history...")

        self.mongo_db_client.insert_post_in_db(reddit_post.id)

        logging.info(f"Repost of the post {reddit_post.id} saved in the history")
