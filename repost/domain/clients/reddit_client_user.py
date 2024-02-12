import os
from dataclasses import dataclass

ENV_CLIENT_ID_KEY = 'REDDIT_CLIENT_ID'
ENV_CLIENT_SECRET_KEY = 'REDDIT_CLIENT_SECRET'
ENV_USER_AGENT_KEY = 'REDDIT_USER_AGENT'


@dataclass(frozen=True)
class RedditClientUser:
    client_id: str = os.getenv(ENV_CLIENT_ID_KEY)
    client_secret: str = os.getenv(ENV_CLIENT_SECRET_KEY)
    user_agent: str = os.getenv(ENV_USER_AGENT_KEY)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if self.client_id is None:
            raise ValueError(f'{ENV_CLIENT_ID_KEY} environment variable is not set')
        if self.client_secret is None:
            raise ValueError(f'{ENV_CLIENT_SECRET_KEY} environment variable is not set')
        if self.user_agent is None:
            raise ValueError(f'{ENV_USER_AGENT_KEY} environment variable is not set')
