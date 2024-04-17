'''
  * author 冯自立
  * created at : 2023-11-21 19:10:50
  * description: 
'''
import datetime


class NotificationConfiguration:
    """
    通知的配置
    """

    def __init__(self, startDay, endDay, title):
        self.startDay = startDay
        self.endDay = endDay
        self.title = title

    def isEnabled(self):
        """
        是否启用
        :return:
        """
        if self.startDay is None:
            return False
        today = datetime.datetime.now()
        if self.endDay is not None:
            return self.startDay <= today <= self.endDay
        else:
            return self.startDay <= today


