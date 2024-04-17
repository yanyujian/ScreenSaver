'''
  * author 冯自立
  * created at : 2023-12-22 12:05:02
  * description: 
'''
import sys
import tkinter as tk
import config
from displayItem import DisplayItem
from models.auto_text import AutoText


class ScreeSaverUI:
    """
    屏保UI
    """

    def __init__(self, alpha=1):
        """
        构造函数
        """
        self.canvas = None
        self.window = tk.Tk()
        self.window.overrideredirect(1)  # 隐藏标题栏
        self.window.attributes("-alpha", alpha)  # 透明度(0.0~1.0)
        self.window.configure(background='black')
        self.bindQuitEvent()
        # self.window.after(1000, self.onTimer) # 1秒后启动定时器
        self.buildCanvas()

    def show(self):
        self.window.mainloop()

    def buildCanvas(self):
        """
        构建画布
        :return:
        """
        self.canvas = tk.Canvas(self.window, width=self.window.winfo_screenwidth(),
                                height=self.window.winfo_screenheight(), bg='black', highlightthickness=0)
        self.canvas.pack()

    def bindQuitEvent(self):
        """
        绑定退出事件
        :return:
        """
        if config.enableExitByMouse:
            self.window.bind("<Button-1>", self.quit)
        self.window.bind("<Key>", self.quit)
        self.window.bind("<Escape>", self.quit)

    def quit(self, event):
        """
        退出
        :return:
        """
        self.window.destroy()
        sys.exit(0)

    def appendAutoText(self, displayItem: DisplayItem, startX, startY, moveSpeedX, moveSpeedY, destroyCallback,
                       destroyUserData, fontType, fontSize, fontColor, moveFrequency):
        """
        展示文本信息
        :param displayItem:
        :param startX:
        :param startY:
        :param moveSpeedX:
        :param moveSpeedY:
        :param destroyCallback:
        :param destroyUserData:
        :param fontType:
        :param fontSize:
        :param fontColor:
        :param moveFrequency:
        :return:
        """
        auto_text = AutoText(displayItem.title, startX, startY, moveSpeedX, moveSpeedY, self.canvas, None, None,
                             self.window, displayItem.displaySeconds, destroyCallback, destroyUserData,
                             fontType=fontType,
                             fontSize=fontSize, fontColor=fontColor, moveFrequency=moveFrequency)
        auto_text.start()
