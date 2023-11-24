from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_path = "D:/MyThings/Development/Chrome_For_Testing/chrome_win64/chrome.exe"
chrome_driver = "D:/MyThings/Development/Chrome_For_Testing/chromedriver_win64/chromedriver.exe"

option = webdriver.ChromeOptions()
option.binary_location = chrome_path
option.add_experimental_option("detach", True)

service = Service(executable_path=chrome_driver)
driver = webdriver.Chrome(options=option, service=service)

driver.get("https://www.youtube.com")
