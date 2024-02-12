import argparse

from repost.usecase.reddit_reposter import RedditReposter, DEFAULT_LIMIT


def parse_args():
    parser = argparse.ArgumentParser(description='Reddit Reposter')
    parser.add_argument('--subreddit', help='Subreddit to repost', required=True)

    limits = [('hot', 'Limit for hot posts'),
              ('top', 'Limit for top posts'),
              ('controversial', 'Limit for controversial posts'),
              ('new', 'Limit for new posts')]

    for limit, help_text in limits:
        parser.add_argument(f'--{limit}_limit', type=int, default=DEFAULT_LIMIT, help=help_text)

    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if not isinstance(args.subreddit, str):
        raise ValueError('Subreddit must be a string')

    for limit in ['hot', 'top', 'controversial', 'new']:
        limit_value = getattr(args, limit + '_limit')
        if not 0 < limit_value < 100:
            raise ValueError(f'{limit} limit must be a positive integer less than 100')


if __name__ == '__main__':
    args = parse_args()
    validate_args(args)
    RedditReposter().repost(args.subreddit, args.hot_limit, args.top_limit, args.controversial_limit, args.new_limit)
