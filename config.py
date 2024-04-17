'''
  * author 冯自立
  * created at : 2023-11-21 12:59:44
  * description: 
'''
import os.path
import logging

# 配置全局日志
if not os.path.exists('d:/scree_saver'):
    os.makedirs('d:/scree_saver')
try:
    # Configure the logging
    logging.basicConfig(
        filename='d:/scree_saver/logger.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
except Exception as e:
    print(f"Error setting up logging: {e}")

from jueJinAINewsProvider import JueJinAINewsProvider
from notificationProvider import NotificationProvider
from rssProvider import RssProvider
from weatherProvider import WeatherProvider

# ui配置
enableExitByMouse = True  # 是否启用鼠标移动退出

displayItems_max = 50  # 最大展示条数，从可选的条目中选择
displayItems_choose_method = 1  # 1:按顺序；2：乱序随机

enableOpenLink = False  # 是否启用打开链接，注意，这个会导致别人通过启动的浏览器访问本地文件内容，所以默认不启用，如果你想启用，可以将这个值设置为True

notificationPath = "d:/notification.txt"  # 通知的配置文件

# 当前启用的文本提供者，RssProvider是Rss提供者，根据实际情况配置多个，JueJinAINewsProvider是掘金AI资讯提供者
enabledTextProviders = [
    WeatherProvider("http://www.nmc.cn/publish/forecast/ABJ/beijing.html", itemLimitation=2, encoding='utf-8',
                    titleColor='blue', summaryColor='blue', enableCache=True, cacheFileName="北京.pkl"),  # 北京天气预报
    NotificationProvider(notificationPath),
    # RssProvider("https://feed.cnblogs.com/blog/sitehome/rss", "cnblogs",enableCache=True,cacheFileName="cnblogs.pkl"),  # 博客园Rss
    JueJinAINewsProvider(itemLimitation=30, enableCache=True, cacheFileName="juejin.pkl", itemDisplaySeconds=-5),
]

autoExitSeconds = -7200  # 自动退出时间

cacheFolder = "d:/screen_saver_cache/"  # 缓存文件夹

if not os.path.exists(cacheFolder):
    os.makedirs(cacheFolder)


def getCacheFilePath(fileName):
    """
    获取缓存文件路径
    :param fileName:
    :return:
    """
    return os.path.join(cacheFolder, fileName)


displaySeconds = 10
