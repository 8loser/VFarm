from scrapy import Spider
import praw


class RedditSpider(Spider):
    name = 'reddit'
    # allowed_domains = ['reddit.com']
    # start_urls = ['https://www.reddit.com/r/funnyvideos/']
    reddit = praw.Reddit("bot1", user_agent="script bot agent")
    for item in reddit.user.me().saved(limit=None):
        print(item)


def parse(self, response):
    pass
