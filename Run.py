#!/usr/bin/env python3
import os
import time
import platform
import subprocess
from functools import wraps
if "Windows" in platform.system():
	import winreg


def timer(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = function(*args, **kwargs)
		end = time.perf_counter()
		print(f"{function.__module__}.{function.__name__}: {end - start}")
		return result
	return wrapper


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
	if "Windows" in platform.system():
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
		path = winreg.QueryValueEx(key, "Desktop")[0]
	else:  # Mac & Linux
		path = os.path.expanduser("~/Desktop")
	return path


def getPython(path):
	extname = "" # 类 unix: Darwin macOS Linux 默认无后缀名
	if "Windows" in platform.system():
		extname = ".exe"
	files = findFile(path, extname)
	di = {os.path.basename(key): key for key in files}
	python_path = os.path.abspath(di[f"python{extname}"])
	return python_path


def getPythonFile(path):
	files = findFile(path, ".py")
	try:
		files.remove(__file__)
	except ValueError:
		pass
	return files[0]


@timer
def runScript(path):
	python_path = getPython(path)
	python_file = getPythonFile(path)
	print(f"USE: {python_path}\nRUN: {python_file}\n")
	
	result = subprocess.run(
		[python_path, python_file], encoding="UTF8", stderr=subprocess.PIPE)
	if result.stderr:  # 输出错误信息
		print(result.stderr)
		time.sleep(5)
		

def main():
	system = platform.system()
	systems = "Windows Darwin macOS Linux".split(" ")
	if system in systems:
		runScript(path=os.getcwd())
	else:
		print(f"暂不支持 {system} 系统")
		time.sleep(5)
		exit(0)
	
	
if __name__ == "__main__":
	main()
