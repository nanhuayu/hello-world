rem 20161025
rem 生成文件备注信息

@echo off
echo.&echo.
set /p fn=输入文件夹路径或者用鼠标把文件夹左键按住拖到此窗口:
echo.&echo.
set /p it=输入你对此文件夹的描述信息:

rem 删除原有desktop.ini
attrib %fn%\desktop.ini -s -h
del %fn%\desktop.ini

rem 生成新desktop.ini
echo [.ShellClassInfo]>%fn%\desktop.ini
echo InfoTip=%it%>>%fn%\desktop.ini
attrib %fn%\desktop.ini +h +s

rem 设置文件夹属性
attrib %fn% +s