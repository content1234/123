from DrissionPage import ChromiumPage, ChromiumOptions

def open_url():
    """
    open打开url文件遍历,并返回数组
    """
    url_list = []
    with open('url.txt') as f:
        for i in f:
            url_list.append(i)
    return url_list

def get_url(url_list,page):
    """
    多开浏览器标签
    """
    for i in url_list:
        page.new_tab(url=i.replace('\n', ""))

if __name__ == "__main__":
    chrome_options = ChromiumOptions().headless()       # 设置无头
    page = ChromiumPage(chrome_options)
    url_list = open_url()
    get_url(url_list=url_list,page=page)


