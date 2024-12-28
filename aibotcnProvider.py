'''
  * author 冯自立
  * created at : 2024-12-28 19:42:38
  * description: 
'''
from typing import List

import requests
from bs4 import BeautifulSoup as BS

from baseProvider import BaseProvider
from displayItem import DisplayItem


class AIBotCnNewsProvider(BaseProvider):

    def __init__(self,itemLimitation=30):
        super().__init__(itemLimitation=itemLimitation)
        self.url = 'https://ai-bot.cn/daily-ai-news'

    def name(self):
        return "AIBot.cn"

    def downloadHtml(self):
        response = requests.get(self.url)
        return response.content.decode('utf-8')

    def extractDisplayItems(self, content) -> List[DisplayItem]:
        bs = BS(content, 'html.parser')
        newsList = bs.find_all('div', class_='news-list')
        result = []
        for newsListItem in newsList:
            for newsItem in newsListItem.find_all('div', class_='news-item'):
                title = newsItem.find('h2').text
                summary = newsItem.find('p').text
                link = newsItem.find('a').get('href')
                displayInfor = DisplayItem(title, summary, link)
                result.append(displayInfor)
        return result


if __name__ == '__main__':
    _aiBotProvider = AIBotCnNewsProvider()
    _results = _aiBotProvider.fetch()
    for item in _results:
        print(item)
