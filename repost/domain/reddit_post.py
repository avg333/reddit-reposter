from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin

from bson import timestamp

SHORT_URL = 'https://redd.it'
IMAGE_EXTENSION = '.png'


@dataclass
class RedditPost:
    author: Any
    created_utc: timestamp
    id: str
    is_original_content: bool
    is_self: bool
    name: str
    num_comments: int
    over_18: bool
    permalink: str
    score: int
    selftext: str
    subreddit: str
    title: str
    upvote_ratio: float
    url: str

    @property
    def shortlink(self) -> str:
        return urljoin(SHORT_URL, self.id)

    @property
    def caption(self) -> str:
        return f"{self.title} {self.shortlink}"

    @property
    def media_filename(self) -> str:
        return self.id + IMAGE_EXTENSION
