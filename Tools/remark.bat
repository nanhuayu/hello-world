@echo off
set /p it=input comments on the document:
echo.&echo. 
attrib %1\desktop.ini -s -h
del %1\desktop.ini
echo [.ShellClassInfo]>%1\desktop.ini
echo InfoTip=%it%>>%1\desktop.ini
attrib %1\desktop.ini +h +s
attrib %1 +s
@echo on
echo.&echo.