@echo off
REM echo 切换至 UTF8
chcp 65001 > nul
REM echo 开启延迟变量
setlocal EnableDelayedExpansion
REM test=1 输出测试内容
set test=0


REM 切换文件所在目录
call :myecho "当前目录"
set Folder=%~dp0
echo %Folder%
cd /d %Folder%


REM 设置临时文件路径
set PythonPathTxt="%Folder%PythonPath.txt"
call :myecho "%PythonPathTxt:"=%"
echo.
goto FindPython
EXIT /B %ERRORLEVEL% 


REM 寻找 Python 程序路径
:FindPython
call :myecho "寻找 Python 程序路径"
dir /s/b | findstr "python.exe" >> %PythonPathTxt%
for /f "usebackq delims=," %%a in (%PythonPathTxt%) do (
	set "PythonPath=%%~a"
	REM set PythonPath=%%~a
	call :myecho "!PythonPath!"
	)


if %test%==1 (
	echo. > Nul
	REM del /q %PythonPathTxt%
	)^
else (
	del /q %PythonPathTxt%
	)
	
	
REM 循环寻找Python程序，找到后运行脚本
if "%cd%"=="%~d0\" (
	if "!PythonPath!"=="" (
		echo 当前磁盘下没有 python.exe 
		goto End
		)
	)
if "%PythonPath%"=="" (
	call :myecho "当前目录下没有 python.exe"
	goto BackToParentPath
	)^
else (
	if %test%==1 echo.
	call :myecho "已经找到 python.exe"
	call :myecho "!PythonPath:"=!"
	goto RunScript
	)
EXIT /B %ERRORLEVEL% 


REM 返回上级目录
:BackToParentPath
if %test%==1 echo.
call :myecho "返回上级目录"
for %%a in ("%cd%") do set ParentPath=%%~dpa
call :myecho %ParentPath%
cd %ParentPath%
goto FindPython
EXIT /B %ERRORLEVEL% 


REM 拼接路径，执行脚本
:RunScript
cd /d %Folder%
if %test%==1 echo.
call :myecho "寻找 Python 脚本路径"
set PythonFile="%~f0"
set PythonFile=%PythonFile:.cmd=.py%
set PythonFile=%PythonFile:.bat=.py%
title %PythonFile:"=%
call :myecho "%PythonFile:"=%"


REM 检测脚本存在与否
if not exist %PythonFile% (
	echo 不存在： %PythonFile:"=%
	echo 脚本不存在，退出运行
	echo.
	goto End
	)
	

REM 执行脚本
if %test%==1 echo.
call :myecho "执行脚本"
echo USE %PythonPath:"=%
echo RUN %PythonFile:"=%
echo.
echo.
REM cd /d %~dp0
call "%PythonPath%" %PythonFile%
goto End
EXIT /B %ERRORLEVEL% 


:End
call :myecho "已删除 PythonPath.txt"
del /q %PythonPathTxt%
pause & exit
EXIT /B %ERRORLEVEL% 


:myecho 
REM echo myecho
if %test%==1 echo %~1
EXIT /B 0