## Renpy Launcher
###  RenPy 的替代启动器
理论支持所有 RenPy 制作的游戏  
原理：直接运行其未设置限制的 Python 脚本


### 支持平台
- Windows
- ~~Mac~~
- ~~Linux~~


|脚本名称 | 支持系统 |备注|
|--------|---------|---------|
|Run.bat | 理论支持所有 Win 系统 | 无法在 `Program Files` 等目录中运行 |
|Run.py  | 支持安装 Python3 的 Win 系统 | 可在 `Program Files` 等目录中运行 |


### 使用方法
0. 下载相关脚本，移动至游戏程序`xxx.exe`所在目录下
1. 复制游戏文件，至非 `Program Files` 目录下
2. 双击脚本，运行游戏


### Todo
- ~~创建桌面快捷方式~~
- ~~修改图标~~
- win 的 powershell 脚本
- mac 的 python 脚本
- linux 的 bash 脚本


## 原始功能 & [原始脚本](./Origin/Run.bat)
使用  embedding python 给没有 Python 环境的人，执行 python 脚本

