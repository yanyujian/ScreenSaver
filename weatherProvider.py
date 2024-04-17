'''
  * author 冯自立
  * created at : 2023-12-05 18:25:38
  * description: http://www.nmc.cn/publish/forecast/ABJ/beijing.html
'''

import random

import requests

from baseProvider import BaseProvider
from displayItem import DisplayItem
from bs4 import BeautifulSoup as BS


class WeatherProvider(BaseProvider):
    """
    天气预报信息抓取器
    """

    def __init__(self, url, itemLimitation=2, encoding='utf-8', titleColor='white', summaryColor='green',
                 enableCache=True, cacheFileName=None):
        super().__init__(itemLimitation, enableCache, cacheFileName)
        if url is None or len(url.strip()) == 0:
            url = "http://www.nmc.cn/publish/forecast/ABJ/beijing.html"
        self.url = url
        self.encoding = encoding
        self.titleColor = titleColor

    def name(self):
        """
        名称
        :return:
        """
        return "天气预报信息"

    def downloadHtml(self):
        """
        下载html
        :return:
        """
        response = requests.get(self.url, proxies={})
        return response.content.decode(self.encoding)

    def extractDisplayItems(self, content):
        bs = BS(content, 'html.parser')
        weatherLists = bs.find_all("div", attrs={"class": "weatherWrap"})[0:self.itemLimitation]
        result = []
        for weather in weatherLists:
            divList = weather.find_all("div")
            if divList is None or len(divList) == 0:
                continue
            else:
                date = divList[0].text.replace("\n", "")
                description = (",".join([div.text for div in divList[5:] if len(div.text) > 0])).strip(" ").strip(
                    " ").strip(",").replace("\n", "")
                result.append(
                    DisplayItem("天气" + date + description, "", self.url, self.titleColor, self.summaryColor))
        return result
