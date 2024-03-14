@echo off
REM echo 切换至 UTF8
chcp 65001 > nul
REM echo 开启延迟变量
setlocal EnableDelayedExpansion
REM test=1 输出测试内容
set test=0


if %test%==1 (
	echo 当前目录
	echo %~dp0
	echo.
	)
	
cd /d %~dp0
set PythonPathTxt="%~dp0PythonPath.txt"
goto FindPython


:FindPython
if %test%==1 echo 寻找 Python 程序
dir /s/b | findstr "python.exe" >> %PythonPathTxt%
for /f "usebackq delims=," %%a in (%PythonPathTxt%) do (
	set "PythonPath=%%~a"
	if %test%==1 echo !PythonPath!
	)
del /q %PythonPathTxt%
goto FindPythonFile


:FindPythonFile
if %test%==1 (
	echo.
	echo 寻找 Python 脚本
	)
cd /d %~dp0
for %%i in (*.py) do (
	set PythonFile=%~dp0%%i
	goto RunScript
)


:RunScript
title %PythonFile%
if %test%==1 (
	echo %PythonFile%
	echo.
	echo 执行脚本
	)
echo USE %PythonPath%
echo RUN %PythonFile%
echo.
if %test%==1 (
	REM call "%PythonPath%"
	call "%PythonPath%" "%PythonFile%"
	)^
else (
	call "%PythonPath%" "%PythonFile%"
	)
REM 同时结束运行
goto exit  


:End
pause & exit

