rem 20161025
rem 生成文件备注信息

@echo off
echo.&echo.
set /p it=输入文件夹的描述信息:

rem 删除原有desktop.ini
attrib %1\desktop.ini -s -h
del %1\desktop.ini

rem 生成新desktop.ini
echo [.ShellClassInfo]>%1\desktop.ini
echo InfoTip=%it%>>%1\desktop.ini
attrib %1\desktop.ini +h +s
attrib %1 +s

rem 设置文件夹属性
echo.&echo.