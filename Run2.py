#!/usr/bin/env python3
import os
import time
import subprocess
from platform import platform
if "Windows" in platform():
	import winreg


def findFile(path: str, *extnames: str) -> list:
	"""
	Args:
		path: path 需要遍历的文件夹路径
		extnames: extname=""获取无后缀名文件；省略 extnames 参数可以获取全部文件
	"""
	pathlist = []
	for root, dirs, files in os.walk(path):
		# print(root, dirs, files, sep="\n")
		for file in files:
			fullpath = os.path.join(root, file)
			
			if len(extnames) > 0:
				for extname in extnames:
					if fullpath.lower().endswith(extname):
						pathlist.append(fullpath)
			elif len(extnames) == 0:
				pathlist.append(fullpath)
	return pathlist


def desktop() -> str:
	if "Windows" in platform():
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
		path = winreg.QueryValueEx(key, "Desktop")[0]
	else:  # 未测试
		path = os.path.expanduser("~/Desktop")
	return path


def getPython(path):
	files = findFile(path, ".exe")
	di = {os.path.basename(key): key for key in files}
	return di["python.exe"]


def getPythonFile(path):
	files = findFile(path, ".py")
	try:
		files.remove(__file__)
	except ValueError:
		pass
	return files[0]


def runOnWindows(path):
	python_path = getPython(path)
	python_file = getPythonFile(path)
	print(f"USE: {python_path}\nRUN: {python_file}\n")
	
	# os.popen(f'title "{python_file}"')
	# os.popen(f'call "{python_path}" "{python_file}"')
	# os.popen(f'pause & exit')  # 显示 Python 报错信息
	
	result = subprocess.Popen([python_path, python_file], stderr=subprocess.PIPE)
	if result.stderr:
		print(result.stderr.read())
		time.sleep(5)
	

def runOnMacOS(path):
	# path = os.getcwd()
	pass
	python_file = getPythonFile(path)
	# print(f"USE: {python_path}\nRUN: {python_file}\n")
	
	subprocess.Popen(["python", python_file])


def main():
	path = os.getcwd()
	if "Windows" in platform():
		runOnWindows(path)
	elif "Darwin" in platform():
		runOnMacOS(path)
	elif "Linux" in platform():
		pass
	else:
		print("暂不支持当前系统")
		time.sleep(5)
		
	
if __name__ == "__main__":
	main()
