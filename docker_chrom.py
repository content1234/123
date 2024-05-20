import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities())
wd = webdriver.Chrome(options=chrome_options)
url = "https://www.baidu.com/"
wd.get(url=url)

# 程序即将结束时，询问是否关闭浏览器
choice = input("Do you want to close the browser? (Y/N) ")
if choice.lower() == "y":
    # 关闭浏览器
    wd.quit()
else:
    print("Browser will remain open.")
