from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RedditGetPostsFilter:
    hot_limit: Optional[int]
    top_limit: Optional[int]
    controversial_limit: Optional[int]
    new_limit: Optional[int]

    def __str__(self):
        return f"hot_limit={self.hot_limit}, top_limit={self.top_limit}, " \
               f"controversial_limit={self.controversial_limit}, new_limit={self.new_limit}"
