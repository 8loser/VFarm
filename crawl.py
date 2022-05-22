from abc import ABC, abstractmethod


class Crawl(ABC):

    @abstractmethod
    def crawl(self):
        '爬取邏輯'
        return NotImplemented

    @abstractmethod
    def save(self):
        '儲存邏輯'
        return NotImplemented
