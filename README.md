# thinkphp6_lang_rce
仅供安全自检使用，禁止使用本工具进行非法攻击，如因此产生的一切不良后果与作者无关。

采用多线程，探测目标是否存在漏洞
## 用法
#### 安装模块
pip install -r requirements.txt
#### python3运行
python thinkphp6_rce_threading.py
#### 打包成exe
pip install pyinstaller
pyinstaller -i favicon.ico -F -w thinkphp6_rce_threading.py
可直接下载exe文件也可以下载源码进行编译
