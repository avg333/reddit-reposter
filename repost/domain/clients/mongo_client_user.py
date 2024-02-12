import os
from dataclasses import dataclass

ENV_URL_KEY = 'DB_URL'
ENV_DB_NAME_KEY = 'DB_NAME'
ENV_DB_TABLE_NAME_KEY = 'DB_TABLE_NAME'
ENV_DB_KEY_FIELD_KEY = 'DB_KEY_FIELD'

DEFAULT_DB_NAME = 'reddit_reposter'
DEFAULT_TABLE_NAME = 'uploaded_posts'
DEFAULT_KEY_FIELD = 'id'


@dataclass(frozen=True)
class MongoClientUser:
    url: str = os.getenv(ENV_URL_KEY)
    db_name: str = os.getenv(ENV_DB_NAME_KEY, DEFAULT_DB_NAME)
    db_table_name: str = os.getenv(ENV_DB_TABLE_NAME_KEY, DEFAULT_TABLE_NAME)
    db_key_field: str = os.getenv(ENV_DB_KEY_FIELD_KEY, DEFAULT_KEY_FIELD)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if self.url is None:
            raise ValueError(f'{ENV_URL_KEY} environment variable is not set')
