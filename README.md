# Screen-Saver
A screen saver written by python for windows . 一个 用python写的屏幕保护程序，能够自动抓取掘金的AI新闻，也可以自定义Rss，该项目提供了简单的接入模板，只需要继承BaseProvider重写展示相关的关键方法即可。


# python实现的屏保程序

### 进度记录

##### 2023.12.22 增加定时展示文本，超过一定时间自动隐藏，详见AutoText

##### 2023.12.11 添加缓存功能（各数据提供端通过配置是否开启，默认提供的天气预报、掘金新闻、RSS都开启了，注意RSS由于可以启用多个，需要给每个RSS单独指定文件名），具体参见config.py；所有的缓存默认存储在d:/screen_saver_cache，当成功获取在线数据后会更新，否则一直保留。

##### 2023.12.11 启用文件日志，方便调试，默认存储在d:/screen_saver/中，如果遇到运行问题可在这里先检查。

##### 2023.12.05 增加了展示天气的功能。在config.py中配置即可。

##### 2023.11.23 增加了展示Provider的功能。目前已经实现了掘金新闻和Rss（以博客园Rss为例，默认未开启）、本地提醒配置的Provider。在config.py中配置即可。

##### 注意：windows下通过管理员身份运行makescreen.bat文件，即可生成屏保程序，然后在屏保设置中选择该屏保程序即可。否则生成文件后无法复制到c:/windows目录中，需要自己手动复制并且修改exe后缀为scr。

###### 功能扩展2： 增加了notification.txt文件，用于显示通知信息，可以通过修改该文件来设置重要提醒，会在屏保中展示。注意：格式为英文逗号，具体参加文件说明。

##### notification.txt默认需要放到D盘根目录下，根据需要调整config.py然后打包即可。

###### 注意：程序自带打开链接功能

## 1. 效果

如下图所示，具体内容可以在config.py中配置，包括天气、掘金新闻、RSS等，可以根据需要开启或关闭。
展示中的文字会随机运动，实现动画效果。

![](Snipaste_2024-04-17_09-41-51.jpg)

## 2. 运行

### 1. 运行环境

Windows + Python 3, 程序所用到的 random, tkinter 库，均为 Pyhton 自带的库，需要安装requests和bs4 库用来抓取第三方数据

### 2. 如何运行

下载代码文件，运行makescreen.bat即可编译打包，生成屏保程序，然后在屏保设置中选择该屏保程序即可。
注意makescreen.bat在编译完成后会自动将exe程序复制到c:\windows\中并重命名为scr（windows屏保专用后缀），但是由于windows的权限限制复制过程经常被拒绝，需要手动复制，然后在屏保中就能选择到。
本地调试的话，直接运行saver_ui_facade.pyw即可。
