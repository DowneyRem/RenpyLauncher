import os


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


def main():
	path = os.getcwd()
	python_path = getPython(path)
	python_file = getPythonFile(path)
	print(f"USE: {python_path}\nRUN: {python_file}\n")
    # os.popen(f'chcp 65001 > nul')  # 不支持
	os.popen(f'title "{python_file}"')
	os.popen(f'call "{python_path}" "{python_file}"')
	os.popen(f'exit')  # 显示 Python 报错信息
	
	
if __name__ == "__main__":
	main()
