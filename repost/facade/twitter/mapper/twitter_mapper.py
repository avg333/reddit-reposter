from datetime import datetime

from tweepy import Response

from repost.domain.twitter_post import TwitterPost


def map_tweet_to_twitter_post(tweet: Response, media_id: str) -> TwitterPost:
    return TwitterPost(
        id=tweet.data["id"],
        text=tweet.data["text"],
        media_id=media_id,
        posted_at=datetime.now()
    )
