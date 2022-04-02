from scrapy import Spider


class RedditSpider(Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/funnyvideos/']


def parse(self, response):
    pass
