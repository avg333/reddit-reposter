from dataclasses import dataclass

from repost.domain.clients.mongo_client_user import MongoClientUser
from repost.domain.clients.reddit_client_user import RedditClientUser
from repost.domain.clients.twitter_client_user import TwitterClientUser


@dataclass(frozen=True)
class ReposterClients:
    reddit_client_user: RedditClientUser = RedditClientUser()
    mongo_client_user: MongoClientUser = MongoClientUser()
    twitter_client_user: TwitterClientUser = TwitterClientUser()
