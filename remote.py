from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities())

driver.get("https://www.baidu.com")

print(driver.title)

driver.quit()