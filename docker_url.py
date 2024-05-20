import psutil
import time
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
    page = ChromiumPage(chrome_options)
    for i in open_url():
        url = i.replace('\n', "")
        page.new_tab(url=url)

while True:
    pro = psutil.process_iter()
    filtered = [i for i in pro if "chrome.exe" in i.name()]
    if len(filtered) > 0:
        print("ok")
        time.sleep(120)
    else:
        get_url()
        time.sleep(120)


