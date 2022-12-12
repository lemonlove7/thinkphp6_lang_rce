### thinkphp6_lang_rce
仅供安全自检使用，禁止使用本工具进行非法攻击，如因此产生的一切不良后果与作者无关。

### 功能
1、可批量导入待检测的目标或在单行文本框中输入要检测的目标

2、采用多线程+进度条，加快对目标检测的速度

<img width="516" alt="图片" src="https://user-images.githubusercontent.com/56328995/207056789-607781c2-6856-4002-8ea3-d3d6241490ce.png">


## 用法
#### 安装模块
pip install -r requirements.txt
### 源码运行
python thinkphp6_rce_threading.py
#### 打包成exe
pip install pyinstaller

pyinstaller -i favicon.ico -F -w thinkphp6_rce_threading.py

### 可执行文件运行
下载到本地即可运行：https://github.com/lemonlove7/thinkphp6_lang_rce/releases/download/thinkphp6_lang_rce_gui_v1.0/thinkphp6_rce_threading.exe

### 使用截图
批量对目标进行安全检测

<img width="517" alt="图片" src="https://user-images.githubusercontent.com/56328995/207057834-33fd4d34-815e-4495-b001-bf96896d3df3.png">

对单个目标进行安全检测
