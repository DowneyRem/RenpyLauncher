@echo off
REM echo 切换至 UTF8
chcp 65001 > nul
REM echo 开启延迟变量
setlocal EnableDelayedExpansion
REM test=1 输出测试内容
set test=1


if %test%==1 (
	echo 当前目录
	echo %~dp0
	echo.
	)	
cd /d %~dp0
set PythonPathTxt="%~dp0PythonPath.txt"
goto FindPython


:FindPython
set PythonPath=""
if %test%==1 echo 寻找 Python 程序
dir /s/b | findstr "python.exe" >> %PythonPathTxt%
for /f "usebackq delims=," %%a in (%PythonPathTxt%) do (
	set "PythonPath=%%~a"
	)
	
REM REM 搜索到系统盘时，补全路径
REM echo %PythonPath%| findstr %SystemDrive% >nul && (
    REM set "PythonPath=%PythonPath%\python.exe"
	REM ) 


if %test%==1 (
	echo. > Nul
	del /q %PythonPathTxt%
	)^
else (
	del /q %PythonPathTxt%
	)
	
	
REM 循环寻找Python程序，找到后运行脚本
if "%cd%"=="%~d0\" (
	if "!PythonPath!"=="" (
		echo 当前磁盘下没有 python.exe 
		REM goto End
		%SystemDrive%
		)
	)
if %PythonPath%=="" (
	if %test%==1 echo 当前目录下没有 python.exe 
	goto BackToParentPath
	)^
else (
	if %test%==1 echo !PythonPath!
	goto FindPythonFile
	)
	

:BackToParentPath
for %%a in ("%cd%") do set ParentPath=%%~dpa
cd %ParentPath%
if %test%==1 (
	echo.
	echo 返回上级目录
	echo %ParentPath%
	echo.
	)
goto FindPython


:FindPythonFile
if %test%==1 (
	echo.
	echo 寻找 Python 脚本
	)	
cd /d %~dp0
set PythonFile=""
for %%i in (*.py) do (
	set PythonFile=%~dp0%%i
	)
	
	
if %PythonFile%=="" (
	echo 当前磁盘下没有 python 脚本
	goto End
	)^
else (
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
	call "%PythonPath%"
	REM call "%PythonPath%" "%PythonFile%"
	)^
else (
	call "%PythonPath%" "%PythonFile%"
	)
goto End


:End
pause & exit

