from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument("--headless")
driver = Chrome(options=options)

driver.get("https://example.com")
sleep(5)
