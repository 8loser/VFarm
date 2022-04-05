import datetime
import praw
from reddit_db import RedditDB


class RedditCrawler:

    reddit = praw.Reddit("bot1", user_agent="script bot agent")

    def __init__(self):
        self.submissions = []
        self.db = RedditDB()

    def crawl(self):
        for submission in self.submissions:
            if submission.is_video:
                id = submission.id
                subreddit = str(submission.subreddit)
                title = submission.title
                link_flair_text = submission.link_flair_text
                author = str(submission.author)
                url = submission.url
                duration = submission.media['reddit_video']['duration']
                over_18 = submission.over_18
                score = submission.score
                upvote_ratio = submission.upvote_ratio
                hls_url = submission.media['reddit_video']['hls_url']
                hls_url = hls_url.split(".m3u8")[0] + '.m3u8'
                record = (id, subreddit, title, link_flair_text, author, url,
                          duration, over_18, score, upvote_ratio, hls_url, 0,
                          datetime.datetime.now())
                self.db.create(record)


class RedditSaved(RedditCrawler):
    '''
    Saved 的 submission
    '''

    def __init__(self):
        super().__init__()

    def crawl(self, count=None):
        self.submissions = self.reddit.user.me().saved(limit=count)
        super().crawl()


crawler = RedditSaved()
crawler.crawl()
