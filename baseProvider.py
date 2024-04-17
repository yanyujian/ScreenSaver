'''
  * author 冯自立
  * created at : 2023-11-22 21:28:39
  * description: 基础提取类
'''
import logging
import os.path

import config
import pickle


class BaseProvider:
    """
    基础提取类
    """

    def __init__(self, itemLimitation=10, enableCache=True, cacheFileName=None, itemDisplaySeconds=None):
        """
        构造函数
        :param itemLimitation:  限制条目数
        """
        self.itemLimitation = itemLimitation
        self.enableCache = enableCache
        self.cacheFileName = cacheFileName
        self.itemDisplaySeconds = itemDisplaySeconds

    def titleColor(self):
        """
        获取文本的展示颜色，默认是绿色，请根据需要自己重写
        :return:
        """
        return "green"

    def summaryColor(self):
        """
        摘要文本的展示颜色，默认绿色，目前没有用到（没展示摘要）
        :return:
        """
        return "green"

    def name(self):
        """
        名称
        :return:
        """
        raise NotImplementedError("请实现该方法")

    def downloadHtml(self):
        """
        下载html
        :return:
        """
        raise NotImplementedError("请实现该方法")

    def extractDisplayItems(self, content):
        """
        提取展示的条目
        :return:
        """
        raise NotImplementedError("请实现该方法")

    def getCacheFileName(self):
        """
        获取缓存文件名
        :return:
        """
        if self.cacheFileName is not None:
            return config.getCacheFilePath(self.cacheFileName)
        else:
            return config.getCacheFilePath("cache_" + self.name() + ".pkl")

    def updateCache(self, results):
        """
        更新缓存
        :param results:
        :return:
        """
        if self.enableCache:
            with open(self.getCacheFileName(), 'wb') as f:
                pickle.dump(results, f)
        else:
            raise Exception("未启用缓存")

    def fetchFromCache(self):
        """
        从缓存中获取
        :return:
        """
        if self.enableCache:
            if not os.path.exists(self.getCacheFileName()):
                return []
            with open(self.getCacheFileName(), 'rb') as f:
                return pickle.load(f)
        else:
            raise Exception("未启用缓存")

    def fetch(self):
        """
        获取
        :return:
        """
        try:
            html = self.downloadHtml()
            results = []
            for item in self.extractDisplayItems(html):
                if self.itemDisplaySeconds is not None and self.itemDisplaySeconds > 0:
                    item.displaySeconds = self.itemDisplaySeconds
                results.append(item)
            returnResult = results[:self.itemLimitation]
            try:
                if self.enableCache:
                    self.updateCache(returnResult)
            except Exception as error:
                logging.error(self.name() + "更新缓存失败" + str(error))  # 更新缓存失败，不影响后续运行
            return returnResult
        except Exception as e:
            logging.error(self.name() + "发生错误,启用缓存" + str(e))
            if self.enableCache:
                return self.fetchFromCache()
            else:
                raise
