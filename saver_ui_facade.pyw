'''
  * author 冯自立
  * created at : 2023-12-22 18:14:44
  * description: 
'''

import displayTextFacade
from saver_ui import ScreeSaverUI
import random
import tkinter as tk


class SaveUIFacade:
    """
    屏保UI外观
    """

    def __init__(self, displayTextProvider, alpha=1):
        """
        构造函数
        """
        self.displayTextProvider = displayTextProvider
        self.alpha = alpha
        windowHelper = tk.Tk()
        self.windowHeight = windowHelper.winfo_screenheight()
        self.windowWidth = windowHelper.winfo_screenwidth()
        windowHelper.destroy()

    def show(self):
        """
        展示
        :return:
        """
        saverWindow = ScreeSaverUI(self.alpha)
        while True:
            item = self.displayTextProvider.nextItem()
            if item is None:
                break
            saverWindow.appendAutoText(item, random.randint(0, self.windowWidth), random.randint(0, self.windowHeight),
                                       moveSpeedX=random.randint(4, 10),
                                       moveSpeedY=random.randint(5, 15),
                                       destroyCallback=None,
                                       destroyUserData=None,
                                       fontType='楷体',
                                       fontSize=random.randint(25, 45)
                                       , fontColor=item.titleColor, moveFrequency=100)
        saverWindow.show()


if __name__ == '__main__':
    SaveUIFacade(displayTextFacade).show()
