# Python3 Screen Saver
# Author: Oslomayor
# Date: Feb 21st, 2019
# GitHub: https://github.com/Oslomayor/Screen-Saver

import random
import tkinter

import config
import webbrowser
import displayTextFacade
import time


class Bio(object):

    def __init__(self, canvas, rootWindow, scrwidth, scrheight):
        # 定义生存时间
        self.displaySeconds = None
        self.item = None

        # 是否删除
        self.hasDelete = False

        # 定义根窗口
        self.root = rootWindow

        # 定义画布
        self.canvas = canvas

        # 定义文字起始位置
        self.xpos = random.randint(50, int(scrwidth - 50))
        self.ypos = random.randint(50, int(scrheight - 50))  # 就这个二货代码，之前写的是scrwidth，导致文字出不来，调了半天才发现

        # 定义文字的速度
        self.xspeed = random.randint(1, 3)
        self.yspeed = random.randint(1, 3)

        # 定义屏幕大小
        self.scrwidth = scrwidth
        self.scrheight = scrheight

        # 定义文字大小字体
        self.fontsize = random.randint(20, 25)
        self.fonttype = '楷体'

    def remove_myself(self):
        self.canvas.delete(self.item)
        self.hasDelete = True  # 标记为已删除

    def enable_auto_destroy(self):
        """
        从根窗口中移除当前文本对象
        :return:
        """
        if self.displaySeconds > 0:
            self.canvas.after(self.displaySeconds * 1000, self.remove_myself)

    def text_click(self, url):
        # 自我销毁，停止运行
        if config.enableOpenLink:
            webbrowser.open_new(url)
        self.root.destroy()

    def draw_Bio(self):
        x = self.xpos
        y = self.ypos
        # 从AI资讯中获取标题和简介
        displayItem = displayTextFacade.nextItem()
        if displayItem is None:
            return False
        self.item = self.canvas.create_text(x, y, text=displayItem.title, font=(self.fonttype, self.fontsize),
                                            fill=displayItem.titleColor)
        print(f" x={x},y={y},text={displayItem.title},fontsize={self.fontsize},fill={displayItem.titleColor}")
        self.canvas.tag_bind(self.item, '<Button-1>', lambda _: self.text_click(displayItem.link))

        if displayItem.displaySeconds is not None and displayItem.displaySeconds > 0:  # 指定了自动销毁的对象开启自动销毁
            self.displaySeconds = displayItem.displaySeconds
            self.enable_auto_destroy()
        return True

    def move_Bio(self):

        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed

        # 当文字撞到了墙
        if self.xpos >= self.scrwidth or self.xpos <= 0:
            self.xspeed *= -1
        if self.ypos >= self.scrheight or self.ypos <= 0:
            self.yspeed *= -1

        self.canvas.move(self.item, self.xspeed, self.yspeed)


# 定义画布的类
class ScreenSaver:

    def __init__(self, bio_nums, restartSeconds=1200):
        self.bios = list()
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        self.root.attributes('-alpha', 1)
        self.root.configure(bg='black')

        ''' 鼠标键盘退出 '''
        if config.enableExitByMouse:
            self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Key>', self.myquit)

        # 得到屏幕大小的规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布
        self.canvas = tkinter.Canvas(self.root, width=w, height=h, bg='black', highlightthickness=0)
        self.canvas.pack()

        # 在画布上画球
        while bio_nums > 0:
            bio = Bio(self.canvas, self.root, scrwidth=w, scrheight=h)
            if bio.draw_Bio():
                self.bios.append(bio)
            bio_nums -= 1

        self.run_screen_saver()
        if restartSeconds > 0:
            self.root.after(restartSeconds * 1000, self.root.destroy)
        self.root.mainloop()

    def run_screen_saver(self):
        self.bios = [x for x in self.bios if not x.hasDelete]  # 将已经展示到期的文本自动移除
        for bio in self.bios:
            bio.move_Bio()  # 移动文本
        self.canvas.after(20, self.run_screen_saver)

    def myquit(self, event):
        # 自我销毁，停止运行
        self.root.destroy()


if __name__ == '__main__':
    ScreenSaver(displayTextFacade.getMaxDisplayItemsCount(), config.autoExitSeconds)
