'''
@project:高级课程
@auther:SinBoi
@file:考试.py
@date:2022/8/17 16:28
@desc:
'''
import time

from selenium import webdriver
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='E:\\test\driver\chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https:\\www.baidu.com')
driver.find_element(By.ID,'kw').send_keys('新梦想软件')
driver.find_element(By.ID,'su').click()
