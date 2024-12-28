pip3 install pyinstaller -i https://mirrors.ustc.edu.cn/pypi/web/simple
pyinstaller --onefile ui_screen_saver.pyw
echo "下面这步经常不成功，自己手动操作吧"
del c:\windows\ui_screen_saver
copy dist\ui_screen_saver.exe c:\windows\ui_screen_saver.scr