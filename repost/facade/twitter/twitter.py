import logging

from tweepy import Client, OAuthHandler, API

from repost.domain.clients.twitter_client_user import TwitterClientUser
from repost.domain.reddit_post import RedditPost
from repost.domain.twitter_post import TwitterPost
from repost.facade.twitter.mapper.twitter_mapper import map_tweet_to_twitter_post


class TwitterPoster:
    def __init__(self, twitter_client_user: TwitterClientUser):
        self.api = API(OAuthHandler(twitter_client_user.api_key,
                                    twitter_client_user.api_key_secret,
                                    twitter_client_user.access_token,
                                    twitter_client_user.access_token_secret))
        self.client = Client(
            consumer_key=twitter_client_user.api_key,
            consumer_secret=twitter_client_user.api_key_secret,
            access_token=twitter_client_user.access_token,
            access_token_secret=twitter_client_user.access_token_secret
        )

    def post_reddit_post_in_twitter(self, reddit_post: RedditPost) -> TwitterPost:
        logging.info("Posting tweet on Twitter...")

        # TODO Migrate upload media to V2 API when it's available
        media = self.api.media_upload(reddit_post.media_filename)

        post = self.client.create_tweet(user_auth=True, text=reddit_post.caption, media_ids=[media.media_id])

        twitter_post = map_tweet_to_twitter_post(post, media.media_id)

        logging.info(f"Posted tweet on Twitter successfully! Tweet id: {twitter_post.id}")
        return twitter_post
