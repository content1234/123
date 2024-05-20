import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities())
wd = webdriver.Chrome(options=chrome_options)
url = "https://www.baidu.com/"
wd.get(url=url)

time.sleep(30)
data = wd.page_source
# print(data)
wd.quit()
