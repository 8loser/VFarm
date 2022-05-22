from abc import ABC, abstractmethod
import praw
from Crawl import Crawl


class IRedditCrawler(Crawl, ABC):
    '''
    抓取條件
    '''
    UPVOTE_RATIO = 0.8
    SCORE = 250
    '''
    抓取數量
    '''
    COUNT = 100
    reddit = praw.Reddit("bot1", user_agent="script bot agent")

    def __init__(self):
        self.submissions = []

    def crawl(self):
        for submission in self.submissions:
            if submission.is_video and \
                submission.upvote_ratio >= self.UPVOTE_RATIO and \
                    submission.score > self.SCORE:

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
                print(hls_url)
                # record = (id, subreddit, title, link_flair_text, author, url,
                #           duration, over_18, score, upvote_ratio, hls_url, 0,
                #           datetime.datetime.now())

    def save(self):
        print('RedditCrawler.save')

    @abstractmethod
    def prepare(self):
        '定義要抓取的submissions'
        return NotImplemented


class Submissions_Saved(IRedditCrawler):
    'Saved 的 submission'

    def __init__(self):
        super().__init__()
        self.prepare()

    def prepare(self):
        self.submissions = self.reddit.user.me().saved(limit=self.COUNT)


class Submissions_Subreddit(IRedditCrawler):
    '使用 subreddit 名稱抓取'

    def __init__(self, subreddit):
        super().__init__()
        self.subreddit = subreddit
        self.prepare()

    def prepare(self):
        self.submissions = self.reddit.subreddit(
            self.subreddit).hot(limit=self.COUNT)


class RedditCrawler(Crawl):

    def __init__(self):
        super().__init__()

    def crawl(self):
        Submissions_Saved().crawl()
        # Submissions_Subreddit('funnyvideos')

    def save(self):
        print('RedditCrawler.save')


if __name__ == '__main__':
    crawler = RedditCrawler()
    crawler.crawl()
