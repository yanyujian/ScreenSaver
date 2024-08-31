'''
  * author 冯自立
  * created at : 2023-11-22 21:18:53
  * description: 统一的显示文本提供者
'''
import logging
import random

import config

cachedDisplayItems = None


def safeFetch(provider):
    """
    安全的获取
    :param provider:
    :return:
    """
    try:
        return provider.fetch()
    except Exception as error:
        logging.error(provider.name() + "获取数据失败" + str(error))
        return []


def initAllItems():
    """
    获取所有的条目
    :return:
    """
    global cachedDisplayItems
    if cachedDisplayItems is not None:
        return cachedDisplayItems
    cachedDisplayItems = []
    for provider in config.enabledTextProviders:
        results = safeFetch(provider)
        if results is None:
            continue
        cachedDisplayItems.extend(results)
    if config.displayItems_choose_method == 2:  # 随机选择，否则按顺序排列
        random.shuffle(cachedDisplayItems)
    return cachedDisplayItems


currentIndex = -1

initAllItems()  # 初始化所有的条目


def nextItem():
    global cachedDisplayItems
    global currentIndex
    currentIndex += 1
    if cachedDisplayItems is None:
        initAllItems()
    if currentIndex >= len(cachedDisplayItems):
        from displayItem import DisplayItem
        return DisplayItem(title="t没有更多的内容了"+str(currentIndex), summary="没有更多的内容了"+str(currentIndex),link="")
        # return None
    result = cachedDisplayItems[currentIndex]
    print(result.title)
    return result


def getMaxDisplayItemsCount():
    """
    获取最大展示条数
    :return:
    """
    return min(len(cachedDisplayItems), config.displayItems_max)
