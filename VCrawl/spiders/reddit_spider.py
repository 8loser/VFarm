from scrapy import Spider
import praw


class RedditSpider(Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    reddit = praw.Reddit("bot1", user_agent="script bot agent")
    for submission in reddit.user.me().saved(limit=None):
        print(submission.title)
        print(submission.is_video)
        print(submission.media['reddit_video']['hls_url'])


def parse(self, response):
    pass
