## Renpy Launcher

###  RenPy 的替代启动器
理论支持所有 RenPy 制作的游戏  
原理：直接运行其未设置限制的 Python 脚本


### 支持平台
- ✅ Windows
- ✅ Mac
- ⭕️ ~~Linux~~


|   脚本  |   支持系统 |  备注  |
|--------|---------|---------|
|Run.bat | 理论支持所有 Win 系统 | 无法在 `Program Files` 等目录中运行 |
|Run.py  | 安装 Python3 的 Win 系统 | 可以在 `Program Files` 等目录中运行 |
|Run.py  | 自带 Python3 的 Mac 系统 | 需要在终端里执行 |


### 使用方法
#### Win 平台
Steam 下载路径：
` C:\Program Files (x86)\Steam\steamapps\common\ `

0. 下载相关脚本，移动至游戏程序`xxx.exe`所在目录下
1. 复制游戏文件，至非 `Program Files` 目录下
2. 双击执行脚本，开始游戏  


#### Mac 平台
Steam 下载路径：`~/Library/Application Support/Steam/steamapps/common/ `

0. 下载相关脚本，移动至游戏程序`xxx.py`所在目录下
1. 在游戏所在目录打开终端
2. 执行脚本`python3 Run.py`，开始游戏


### Todo
- ✅ Win 的 batch 脚本
- ✅ Win 的 python 脚本
- ✅ Mac 的 python 脚本
- ~~win 的 powershell 脚本~~
- ~~创建桌面快捷方式~~
- ~~修改图标~~
- linux 的 bash 脚本


## 原始功能 & [原始脚本](./Origin/Run.bat)
使用  embedding python 给没有 Python 环境的人，执行 python 脚本

