'''
  * author 冯自立
  * created at : 2023-11-20 15:57:21
  * description: 抓取掘金网站的最新AI资讯标题
'''
import random

import requests
from bs4 import BeautifulSoup as BS


def downloadHtml():
    """
    下载掘金网站的最新AI资讯
    :return:
    """
    response = requests.get("https://llm.juejin.cn/news", proxies={}) # 默认禁用代理
    return response.text


def extractJueJinAINews():
    """
    提取掘金网站的最新AI资讯
    :return:
    """
    content = downloadHtml()
    bs = BS(content, 'html.parser')
    articles = bs.find_all("div", attrs={"class": "text-dwd1XE noImg-zgcFxV"})
    articles2 = bs.find_all("div", attrs={"class": "entryItem-vi2K_b"})
    articles.extend(articles2)
    return articles


def extractAllAINewsTitleAndSummary():
    """
    提取所有AI资讯的标题和简介
    :return:
    """
    articles = extractJueJinAINews()
    random.shuffle(articles)
    result = {}
    for article in articles:
        title = article.find("div", attrs={"class": "title-XsdBod"})
        introduce = article.find("div", attrs={"class": "description-DtNpUT"})
        result[title.text] = introduce.text
    return result


class AINewsHolder:
    """
    AI资讯的持有者
    """

    def __init__(self):
        try:
            self.ainews = extractAllAINewsTitleAndSummary()
        except Exception as e:
            print("获取AI资讯失败", e)
            self.ainews = {}

    def getAINews(self):
        return self.ainews

    currentIndex = -1

    def nextNews(self):
        """
        获取下一条资讯
        :return:
        """
        self.currentIndex += 1
        if self.currentIndex >= len(self.getAINews()):
            return None, None, None
        return list(self.ainews.keys())[self.currentIndex], list(self.ainews.values())[
            self.currentIndex], "https://llm.juejin.cn/news"


if __name__ == "__main__":
    print(extractAllAINewsTitleAndSummary())
