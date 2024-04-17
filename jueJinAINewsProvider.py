'''
  * author 冯自立
  * created at : 2023-11-22 21:33:13
  * description: 掘金AI新闻提供者
'''
import random

import requests

from baseProvider import BaseProvider
from displayItem import DisplayItem
from bs4 import BeautifulSoup as BS


class JueJinAINewsProvider(BaseProvider):
    """
    掘金AI新闻提供者
    """

    def __init__(self, itemLimitation=10, enableCache=True, cacheFileName=None, itemDisplaySeconds=None):
        """
        构造函数
        :param itemLimitation:  限制条目数
        :param enableCache: 是否启用缓存
        :param cacheFileName: 缓存文件名
        """
        super().__init__(itemLimitation, enableCache, cacheFileName, itemDisplaySeconds)

    def name(self):
        """
        名称
        :return:
        """
        return "掘金AI新闻"

    def downloadHtml(self):
        """
        下载html
        :return:
        """
        response = requests.get("https://llm.juejin.cn/news", proxies={})  # 默认禁用代理
        return response.text

    def extractDisplayItems(self, content):
        """
        提取展示的条目
        :return:
        """
        bs = BS(content, 'html.parser')
        articles = bs.find_all("div", attrs={"class": "text-dwd1XE noImg-zgcFxV"})
        articles2 = bs.find_all("div", attrs={"class": "entryItem-vi2K_b"})
        articles.extend(articles2)
        # random.shuffle(articles) #默认不打乱了
        result = []
        for article in articles:
            title = article.find("div", attrs={"class": "title-XsdBod"}).text
            introduce = article.find("div", attrs={"class": "description-DtNpUT"})
            introduceContent = introduce.text
            result.append(DisplayItem(title, introduceContent, "https://llm.juejin.cn/news"))
        return result
