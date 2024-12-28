'''
  * author 冯自立
  * created at : 2024-12-28 21:43:02
  * description: 解决provider单独测试时会出现的循环引用问题
'''
import os

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
