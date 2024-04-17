'''
  * author 冯自立
  * created at : 2023-12-22 12:46:52
  * description: 
'''
import tkinter
import random


class AutoText:
    """
    完全自管理的文本。
    主要支持下述功能：
    1、自动创建文本并附加到画布
    2、自动销毁
    3、支持销毁后回调（以便外面的调度器能根据业务情况自行操作）
    """

    def __init__(self, text, currentX, currentY, xSpeed, ySpeed,
                 canvas: tkinter.Canvas, clickCallback, clickUserData,
                 window: tkinter.Tk,
                 liveSeconds, destroyCallback, destroyUserData,
                 fontType='楷体', fontSize=30, fontColor='white',
                 moveFrequency=50):
        """
        初始化自管理文本对象
        :param text: 要展示的文本
        :param canvas: 文本所属画布
        :param clickCallback: 点击文本时的回调函数：clickCallback(autoText, event, clickUserData) ; autoText: 当前文本对象；event：点击事件；clickUserData：点击文本回调时自定义参数
        :param clickUserData: 点击文本回调时自定义参数
        :param window: 文本所属窗口
        :param liveSeconds: 当前文本展示时间
        :param destroyCallback: 文本展示到期销毁时的回调函数
        :param destroyUserData: 文本销毁后回调的用户对象
        :param currentX: 起始X轴展示位置
        :param currentY: 起始Y轴展示位置
        :param xSpeed: x方向的移动速度
        :param ySpeed: y方向的移动速度
        :param fontType: 字体类型
        :param fontSize: 字体大小
        :param fontColor: 字体颜色
        """
        self.text = text
        self.canvas = canvas
        self.clickCallback = clickCallback
        self.clickUserData = clickUserData
        self.liveSeconds = liveSeconds
        self.destroyCallback = destroyCallback
        self.destroyUserData = destroyUserData
        self.currentX = currentX
        self.currentY = currentY
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.originalXSpeed = xSpeed
        self.originalYSpeed = ySpeed
        self.displayItem = None
        self.hasDelete = False
        self.fontType = fontType
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.moveFrequency = moveFrequency
        self.window = window
        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHeight = self.window.winfo_screenheight()

    def on_click(self, event):
        """
        点击文本时的回调函数
        :param event:
        :return:
        """
        if self.clickCallback is not None:
            self.clickCallback(self, event, self.clickUserData)

    def on_destroy(self):
        """
        文本展示到期销毁时的回调函数
        :return:
        """
        if self.destroyCallback is not None:
            self.destroyCallback(self, self.destroyUserData)
        self.canvas.delete(self.displayItem)
        self.hasDelete = True

    def auto_move(self):
        """
        自动移动
        :return:
        """
        if self.hasDelete:
            return
        self.currentX += self.xSpeed
        self.currentY += self.ySpeed
        self.canvas.move(self.displayItem, self.xSpeed, self.ySpeed)
        # 边界检测，运动方向调整
        if self.currentX <= 0 or self.currentX >= self.screenWidth:
            # self.xSpeed = (random.randint(int(self.originalXSpeed / 2), self.originalXSpeed)) * (
            #     1 if self.xSpeed > 0 else -1)
            self.xSpeed = -self.xSpeed
        if self.currentY <= 0 or self.currentY >= self.screenHeight:
            # self.ySpeed = (random.randint(int(self.originalYSpeed / 2), self.originalYSpeed)) * (
            #     1 if self.ySpeed > 0 else -1)
            self.ySpeed = -self.ySpeed
        # 开启下一次移动
        self.canvas.after(self.moveFrequency, self.auto_move)

    def enable_auto_move(self):
        """
        启用自动移动
        :return:
        """
        self.canvas.after(self.moveFrequency, self.auto_move)

    def start(self):
        """
        开始执行展示逻辑：附加到画布中并开始倒计时（如果有的话）
        :return:
        """
        self.displayItem = self.canvas.create_text(self.currentX, self.currentY, text=self.text,
                                                   font=(self.fontType, self.fontSize),
                                                   fill=self.fontColor)
        self.canvas.tag_bind(self.displayItem, '<Button-1>', self.on_click)
        if self.liveSeconds is not None:
            self.canvas.after(self.liveSeconds * 1000, self.on_destroy)
        self.enable_auto_move()
