from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

firefox_driver = "D:/MyThings/Development/Chrome_For_Testing/geckodriver/geckodriver.exe"

option = Options()
service = Service(executable_path=firefox_driver)

driver = webdriver.Firefox(options=option, service=service)

driver.get("https://www.youtube.com")
driver.maximize_window()
