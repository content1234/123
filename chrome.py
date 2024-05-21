import psutil
import time
import os
import requests
from DrissionPage import ChromiumPage, ChromiumOptions

def open_url():
    """
    open打开url文件遍历,并返回数组
    """
    url_list = []
    with open('./url.txt') as f:
        for i in f:
            url_list.append(i)
    return url_list

def get_url():
    """
    多开浏览器标签
    """
    chrome_options = ChromiumOptions().headless()       # 设置无头
    page = ChromiumPage()
    for i in open_url():
        url = i.replace('\n', "")
        page.new_tab(url=url)

def close_chrome(browser_anme):
    """
    关闭浏览器
    """
    for i in psutil.process_iter():
        if i.name() == browser_anme:
            i.kill()
            os.system(f'taskkill /F /IM {browser_anme}')        # 终止进程
    return False

close_chrome("chrome.exe")
while True:
    pro = psutil.process_iter()                                 # 获取进程
    filtered = [i for i in pro if "chrome.exe" in i.name()]     # 过滤进程
    # 判断状态
    if len(filtered) > 0:
        print("ok")
        time.sleep(1200)
    else:
        get_url()
        time.sleep(1200)


