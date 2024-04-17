'''
  * author 冯自立
  * created at : 2023-11-23 19:07:12
  * description: 
'''
import datetime

from notificationConfiguration import NotificationConfiguration
from baseProvider import BaseProvider
from displayItem import DisplayItem


class NotificationProvider(BaseProvider):
    """
    通知提供者
    """

    def __init__(self, notificationPath, itemLimitation=10, encoding="utf-8", titleColor="red", summaryColor="red",
                 enableCache=False, cacheFileName=None):
        """
        构造函数
        :param self:
        :param notificationPath:  通知的路径
        :param encoding: 编码
        :param titleColor 文本颜色
        :param summaryColor 摘要颜色
        :param itemLimitation:  限制条目数
        :param cacheFileName: 缓存文件名
        :param enableCache: 是否启用缓存
        :return:
        """
        self.notificationPath = notificationPath
        self.encoding = encoding
        self._titleColor = titleColor
        self._summaryColor = summaryColor
        super().__init__(itemLimitation, enableCache, cacheFileName)

    def titleColor(self):
        return self._titleColor

    def summaryColor(self):
        return self._summaryColor

    def name(self):
        """
        名称
        :return:
        """
        return "通知提供者"

    def downloadHtml(self):
        """
        下载html
        :param self:
        :return:
        """
        with(open(self.notificationPath, encoding=self.encoding)) as fl:
            return fl.read()

    def extractDisplayItems(self, content):
        """
        提取展示的条目
        :return:
        """
        for line in content.split("\n"):
            config = self.loadNotificationConfig(line)
            if config is not None and config.isEnabled():
                yield DisplayItem(config.title, None, None, titleColor=self.titleColor(),
                                  summaryColor=self.summaryColor())

    def convertStrToDate(self, str):
        """
        将字符串转换为日期
        :param self
        :param str:
        :return:
        """
        try:
            return datetime.datetime.strptime(str, "%Y-%m-%d")
        except Exception as e:
            print(str + "转时间失败", e)
            return None

    def loadNotificationConfig(self, line):
        """
        2023-11-21  2023-11-30  check mobile number
        :param self:
        :param line: 2023-11-21  2023-11-30  check mobile number
        :return:
        """
        line = line.strip()
        if line.startswith("#"):
            return None
        if line == "":
            return None
        parts = line.split(",")
        if len(parts) != 3:
            return None
        startDay = self.convertStrToDate(parts[0])
        endDay = self.convertStrToDate(parts[1])
        title = parts[2]
        if title.strip() == "":
            return None
        return NotificationConfiguration(startDay, endDay, title)


if __name__ == '__main__':
    provider = NotificationProvider("notification.txt")
    for item in provider.fetch():
        print(item.title)
        print(item.summary)
        print(item.link)
