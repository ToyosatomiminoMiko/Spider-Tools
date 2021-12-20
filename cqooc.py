#!usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(1)
driver.get("http://www.cqooc.net/")
#点击"登录"
sleep(7)
driver.find_element_by_link_text("登录").click()
#输入用户名
sleep(5)
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("127592023207034")
#输入密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("cqvie+127592023207034")
#点击登录
sleep(3)
driver.find_element_by_id("loginBtn").click()
#*课程
sleep(6)
driver.get("http://www.cqooc.net/learn/mooc/structure?id=334567567")

sleep(10)
