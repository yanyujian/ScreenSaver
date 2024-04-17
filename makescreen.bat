pip3 install pyinstaller -i https://mirrors.ustc.edu.cn/pypi/web/simple
pyinstaller --onefile ui_screen_saver.pyw
del c:\windows\fstart_saver.scr
copy dist\ui_screen_saver.exe c:\windows\ui_screen_saver.scr