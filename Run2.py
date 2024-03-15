#!/usr/bin/env python3
import os
import time
import subprocess
from platform import platform
from functools import wraps
if "Windows" in platform():
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
	if "Windows" in platform():
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
		path = winreg.QueryValueEx(key, "Desktop")[0]
	else:  # 未测试
		path = os.path.expanduser("~/Desktop")
	return path


def getPython(path):
	if "Windows" in platform():
		files = findFile(path, ".exe")
		di = {os.path.basename(key): key for key in files}
		return di["python.exe"]
	
	elif "Darwin" in platform():
		files = findFile(path, "")
		di = {os.path.basename(key): key for key in files}
		python_path = os.path.abspath(di["python"])
		return python_path
	
	elif "Linux" in platform():
		pass
	else:
		print("暂不支持当前系统")
		time.sleep(5)
	return None


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
	if "Windows" in platform() or "Darwin" in platform():
		runScript(path=os.getcwd())
	else:
		print("暂不支持当前系统")
		time.sleep(5)
		exit(0)
	
	
if __name__ == "__main__":
	main()
