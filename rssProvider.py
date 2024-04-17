'''
  * author 冯自立
  * created at : 2023-11-23 13:47:38
  * description: 
'''
import requests
from bs4 import BeautifulSoup as BS
from displayItem import DisplayItem

from baseProvider import BaseProvider


class RssProvider(BaseProvider):
    """
    Rss提供者
    """

    def __init__(self, rssUrl, itemLimitation=10, name="RssProvider", encoding="utf-8", entryTag="entry",
                 titleTag="title", linkTag="link",
                 summaryTag="summary", linkAttr="href",
                 enableCache=True, cacheFileName=None):
        self.name = name
        self.rssUrl = rssUrl
        self.encoding = encoding
        self.entryTag = entryTag
        self.titleTag = titleTag
        self.linkTag = linkTag
        self.summaryTag = summaryTag
        self.linkAttr = linkAttr
        super().__init__(itemLimitation, enableCache, cacheFileName)

    def name(self):
        """
        名称
        :return:
        """
        return self.name

    def downloadHtml(self):
        return requests.get(self.rssUrl).content.decode(self.encoding)

    def extractDisplayItems(self, content):
        bs = BS(content, 'xml')
        entryList = bs.find_all(self.entryTag)
        for entry in entryList:
            title = entry.find(self.titleTag).text
            link = entry.find(self.linkTag).attrs[self.linkAttr]
            summary = entry.find(self.summaryTag).text
            yield DisplayItem(title, summary, link)


if __name__ == '__main__':
    rssProvider = RssProvider("https://feed.cnblogs.com/blog/sitehome/rss", "cnblogs")
    for item in rssProvider.fetch():
        print(item.title)
        print(item.summary)
        print(item.link)
