import os
from dataclasses import dataclass

ENV_API_KEY = 'TWITTER_API_KEY'
ENV_API_KEY_SECRET = 'TWITTER_API_KEY_SECRET'
ENV_ACCESS_TOKEN = 'TWITTER_ACCESS_TOKEN'
ENV_ACCESS_TOKEN_SECRET = 'TWITTER_ACCESS_TOKEN_SECRET'


@dataclass(frozen=True)
class TwitterClientUser:
    api_key: str = os.getenv(ENV_API_KEY)
    api_key_secret: str = os.getenv(ENV_API_KEY_SECRET)
    access_token: str = os.getenv(ENV_ACCESS_TOKEN)
    access_token_secret: str = os.getenv(ENV_ACCESS_TOKEN_SECRET)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if self.api_key is None:
            raise ValueError(f'{ENV_API_KEY} environment variable is not set')
        if self.api_key_secret is None:
            raise ValueError(f'{ENV_API_KEY_SECRET} environment variable is not set')
        if self.access_token is None:
            raise ValueError(f'{ENV_ACCESS_TOKEN} environment variable is not set')
        if self.access_token_secret is None:
            raise ValueError(f'{ENV_ACCESS_TOKEN_SECRET} environment variable is not set')
