import argparse

from repost.usecase.reddit_reposter import RedditReposter, DEFAULT_LIMIT


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Reddit Reposter')
    parser.add_argument('--subreddit', type=str, help='Subreddit to repost', required=True)

    limits = [('hot', 'Limit for hot posts'),
              ('top', 'Limit for top posts'),
              ('controversial', 'Limit for controversial posts'),
              ('new', 'Limit for new posts')]

    for limit, help_text in limits:
        parser.add_argument(f'--{limit}_limit', type=_valid_limit_range, default=DEFAULT_LIMIT, help=help_text)

    return parser.parse_args()


def _valid_limit_range(limit: str) -> int:
    limit = int(limit)
    if limit < 0 or limit > 99:
        raise argparse.ArgumentTypeError("Value must be an integer between 0 and 99")
    return limit


if __name__ == '__main__':
    args = _parse_args()
    RedditReposter().repost(args.subreddit, args.hot_limit, args.top_limit, args.controversial_limit, args.new_limit)
