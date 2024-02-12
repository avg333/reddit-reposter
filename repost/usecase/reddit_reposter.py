#!/usr/bin/env python
"""
Upload to the Twitter platform a post of the chosen subreddit
"""

__author__ = "Adrian Villar Gesto"
__version__ = "2.1.0"
__email__ = "adrian.villar.gesto@gmail.com"
__status__ = "Production"

import logging

from repost.domain.clients.reposter_clients import ReposterClients
from repost.domain.reddit_get_posts_filter import RedditGetPostsFilter
from repost.facade.history.history import HistoryManager
from repost.facade.image.image import save_url_image
from repost.facade.reddit.reddit import RedditPostFetcher
from repost.facade.twitter.twitter import TwitterPoster
from repost.utils.image import remove_img

DEFAULT_LIMIT = 10


class RedditReposter:

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        reposter_clients = ReposterClients()
        self.reddit_post_fetcher = RedditPostFetcher(reposter_clients.reddit_client_user)
        self.twitter_poster = TwitterPoster(reposter_clients.twitter_client_user)
        self.history_manager = HistoryManager(reposter_clients.mongo_client_user)

    def repost(self,
               subreddit: str,
               hot_limit: int = DEFAULT_LIMIT,
               top_limit: int = DEFAULT_LIMIT,
               controversial_limit: int = DEFAULT_LIMIT,
               new_limit: int = DEFAULT_LIMIT) -> None:

        if not subreddit:
            raise ValueError("Subreddit can not be empty")

        reddit_filter = RedditGetPostsFilter(hot_limit, top_limit, controversial_limit, new_limit)

        logging.info(f"Starting repost of subreddit {subreddit}...")

        reddit_posts = self.reddit_post_fetcher.get_reddit_posts(subreddit, reddit_filter)

        reddit_valid_posts = self.history_manager.filter_not_reposted_posts(reddit_posts)

        for reddit_post in reddit_valid_posts:

            logging.info(f"Reposting post {reddit_post.id}...")

            save_url_image(reddit_post.url, reddit_post.media_filename)

            self.history_manager.save_repost_in_history(reddit_post)

            twitter_post = self.twitter_poster.post_reddit_post_in_twitter(reddit_post)

            remove_img(reddit_post.media_filename)

            if twitter_post:
                logging.info(f"Post {reddit_post.id} was reposted successfully!")
                return

        logging.warning("No post was reposted")
