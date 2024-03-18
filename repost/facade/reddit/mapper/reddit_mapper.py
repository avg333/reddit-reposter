from datetime import datetime

from praw.models import Submission

from repost.domain.reddit_post import RedditPost


def map_posts_to_reddit_posts(posts: list[Submission]) -> list[RedditPost]:
    return [_map_post_to_reddit_post(post) for post in posts]


def _map_post_to_reddit_post(post: Submission) -> RedditPost:
    return RedditPost(
        author=post.author.name if post.author else "Unknown",
        created_utc=datetime.fromtimestamp(post.created_utc),
        id=post.id,
        is_original_content=post.is_original_content,
        is_self=post.is_self,
        name=post.name,
        num_comments=post.num_comments,
        over_18=post.over_18,
        permalink=post.permalink,
        score=post.score,
        selftext=post.selftext,
        subreddit=post.subreddit.display_name if post.subreddit else "Unknown",
        title=post.title,
        upvote_ratio=post.upvote_ratio,
        url=post.url)
