import concurrent
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Callable

from praw import Reddit
from praw.models import Submission
from prawcore import PrawcoreException

from repost.domain.clients.reddit_client_user import RedditClientUser
from repost.domain.reddit_get_posts_filter import RedditGetPostsFilter
from repost.domain.reddit_post import RedditPost
from repost.exception.no_posts_found_exception import NoPostsFoundException
from repost.facade.reddit.mapper.reddit_mapper import map_posts_to_reddit_posts

IMGUR_LINK = "imgur"
VALID_IMG_FORMATS = ["jpg", "jpeg", "png", "webp"]


class RedditPostFetcher:

    def __init__(self, reddit_client_user: RedditClientUser):
        self.reddit = Reddit(client_id=reddit_client_user.client_id,
                             client_secret=reddit_client_user.client_secret,
                             user_agent=reddit_client_user.user_agent)

    def get_reddit_posts(self, reddit_subreddit: str, reddit_filter: RedditGetPostsFilter) -> list[RedditPost]:
        logging.info(f"Searching posts in the subreddit {reddit_subreddit}...")

        posts = self._get_subreddit_posts(reddit_subreddit, reddit_filter)
        reddit_posts = map_posts_to_reddit_posts(posts)
        valid_posts = self._get_valid_posts(reddit_posts)

        if not valid_posts:
            logging.error("No valid posts found")
            raise NoPostsFoundException

        logging.info(f"Found {len(valid_posts)} posts!")
        return valid_posts

    def _get_subreddit_posts(self, reddit_subreddit: str, reddit_filter: RedditGetPostsFilter) -> list[Submission]:

        subreddit = self.reddit.subreddit(reddit_subreddit)

        categories = {
            'hot': subreddit.hot,
            'top': subreddit.top,
            'controversial': subreddit.controversial,
            'new': subreddit.new
        }

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._fetch_posts, category, function, limit)
                       for category, function in categories.items()
                       if (limit := getattr(reddit_filter, f"{category}_limit"))]

            posts = [post for future in concurrent.futures.as_completed(futures) for post in future.result()]

        return posts

    @staticmethod
    def _fetch_posts(category: str, category_function: Callable, limit: int) -> list[Submission]:
        try:
            return category_function(limit=limit)
        except PrawcoreException:
            logging.error(f"Error searching for posts in the {category} category", exc_info=True)
            return []

    def _get_valid_posts(self, posts: list[RedditPost]) -> list[RedditPost]:
        valid_posts = [post for post in posts if self._is_valid_post(post)]
        return list({post.id: post for post in valid_posts}.values())

    def _is_valid_post(self, reddit_post: RedditPost) -> bool:
        return (self._contains_valid_media(reddit_post) and
                not self._contains_imgur_link(reddit_post) and
                not self._is_over_18(reddit_post))

    @staticmethod
    def _contains_valid_media(reddit_post: RedditPost) -> bool:
        return any(x in reddit_post.url.lower() for x in VALID_IMG_FORMATS)

    @staticmethod
    def _contains_imgur_link(reddit_post: RedditPost) -> bool:
        return IMGUR_LINK in reddit_post.url.lower()

    @staticmethod
    def _is_over_18(post: RedditPost) -> bool:
        return post.over_18
