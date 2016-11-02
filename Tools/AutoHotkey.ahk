send, #d
sleep, 100

;~ IfWinExist, ahk_exe Foxmail.exe
;~ {
;~ WinActivate, ahk_exe Foxmail.exe
;~ }
;~ else
;~ {
;~ run, D:\Foxmail 7.2\Foxmail.exe
;~ sleep, 100

;~ WinWait, ahk_exe Foxmail.exe
;~ WinActivate 
;~ }

run, D:\Foxmail 7.2\Foxmail.exe
sleep, 100

WinWait, ahk_exe Foxmail.exe
WinActivate, ahk_exe Foxmail.exe
Sleep, 100

;~ WinActivate, ahk_exe Foxmail.exe
;~ WinGetPos, X, Y, Width, Height, A

;~ SetTitleMatchMode, 2
;~ SetTitleMatchMode, Slow 

X := 75
Y := 600
MouseMove, X, Y
Sleep, 50
Click %X% %Y%
;~ Click 2
sleep, 50

/* 
X := 1065
Y := 45
MouseMove, X, Y
Sleep, 50
Send {Click, X, Y}
sleep, 50 
*/

WinGet, ControlList, ControlList, A
find := RegExMatch(ControlList, "(TTBXButton[1-9]+)",SubPat)
Control, Check, , %SubPat1%

send, {down 4} {Enter}
sleep, 50
Send, {ALTDOWN}s{ALTUP}
sleep, 50

;~ WinActivate, ahk_exe Foxmail.exe
send, !{F4}