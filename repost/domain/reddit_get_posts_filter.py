from dataclasses import dataclass
from typing import Optional


@dataclass
class RedditGetPostsFilter:
    hot_limit: Optional[int]
    top_limit: Optional[int]
    controversial_limit: Optional[int]
    new_limit: Optional[int]
