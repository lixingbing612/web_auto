# 需求：在百度输入框中输入关键字python进行搜索

# 1.导包
from selenium import webdriver
import time
# 2.创建浏览器驱动
driver = webdriver.Chrome()
# 3.打开web页面-tpshop
driver.get("http://localhost")
# 4.暂停3s
time.sleep(3)
driver.maximize_window()
# 5.使用link_text定位首页登录按钮，进入登录页面
driver.find_element_by_link_text("登录").click()
time.sleep(2)
# 6.使用id定位用户输入框，
driver.find_element_by_id("username").send_keys("13112345678")
# 7.使用name定位密码输入框
driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_id("password").send_keys("123456")
# 8.使用name定位验证码输入框
driver.find_element_by_name("verify_code").send_keys("8888")
# driver.find_element_by_id("verify_code").send_keys("8888")
# 9.使用name定位登录按钮
driver.find_element_by_class_name("J-login-submit").click()
# driver.find_element_by_name("sbtbutton").click()
time.sleep(3)
driver.find_element_by_class_name("home").click()
driver.find_element_by_id("q").send_keys("小米")
driver.find_element_by_class_name("ecsc-search-button").click()
time.sleep(3)
driver.refresh()
time.sleep(2)
# 关闭浏览器
driver.quit()
