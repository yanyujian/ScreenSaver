'''
  * author 冯自立
  * created at : 2023-11-22 21:30:50
  * description: 展示的条目
'''


class DisplayItem:
    """
    展示的条目
    """

    def __init__(self, title, summary, link, titleColor="green", summaryColor="green", displaySeconds=None):
        """
        构造函数
        :param title: 标题
        :param summary: 摘要
        :param link: 链接
        :param titleColor: 标题颜色
        :param summaryColor: 摘要颜色
        :param displaySeconds: 展示时长（单位：秒）
        :param
        """
        self.title = title
        self.summary = summary
        self.link = link
        self.titleColor = titleColor
        self.summaryColor = summaryColor
        self.displaySeconds = displaySeconds

    def __str__(self):
        return "标题：" + self.title + " 摘要：" + self.summary + " 链接：" + self.link + " 标题颜色：" + self.titleColor + " 摘要颜色：" + self.summaryColor + " 展示时长：" + str(self.displaySeconds)