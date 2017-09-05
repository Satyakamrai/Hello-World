from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver_win32/chromedriver.exe')
driver.get('http://google.co.in')
time.sleep(3)
element = driver.find_element_by_xpath(".//input[@type='text']")

element.send_keys('satyakam')
