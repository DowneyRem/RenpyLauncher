## RenPy Launcher Original Version (Archived)

##  RenPy 替代启动器 原始版本(已归档)

使用  embedding python 给没有 Python 环境的人，执行 py 脚本

## 原始功能
- 从当前目录向上级文件夹中搜寻 python.exe，直至根目录（以最近的一个  python.exe 为准）
- 执行与之同名的 Python 脚本

### 优点
- 使用  embedding python ，无需配置 Python 环境
- 优先以指定 Python 版本为准，而非系统中的 Python 版本
- 理论支持所有 Windows 系统

### 缺陷
- 需要修改 Run.bat 的文件名，使其与 Python 脚本一致
- 无法获取其他分区上的 Python 环境
- 需要根据 Windows 系统版本版本，提供 Python 环境

### Windows 版本对应的最高Python 版本
以原版 iso 可以安装的 python 版本为准
| Windows 版本     | Python 版本   |
| --------------- | ------------- |
| WindowsXP SP3   | Python 3.4.4  |
| Windows7 2009   | Python 3.4.4  |
| Windows7 2011   | Python 3.7.6  |
| Windows7 2019   | Python 3.8.10 |
| Windows8.1 2014 | Python 3.9+ |
