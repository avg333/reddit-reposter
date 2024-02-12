from dataclasses import dataclass
from datetime import datetime


@dataclass
class TwitterPost:
    id: str
    text: str
    media_id: str
    posted_at: datetime
