
# 警告框
"""
方法：
alert
alert = driver.switch_to.alert	初始化弹出框对象
text	获取文本信息
driver.switch_to.alert.accept()		点击确认按钮
driver.switch_to.alert.dismiss()	点击取消按钮
driver.switch_to.alert.send_keys('xx')	在文本框中输入信息

"""
# 导包
from selenium import webdriver
import time

# 初始化webdriver对象并打开浏览器
driver = webdriver.Chrome()
driver.get('file:///C:/Users/%E6%9D%8E%E6%98%9F%E5%86%B0/Desktop/alert.html')

# 点击确认框
driver.find_element_by_id('alert').click()

# 初始化弹出框对象
alert = driver.switch_to.alert

# 创建警告框的实例化对象：Select（elem），elem为定位元素的对象
print(alert.text)
time.sleep(3)
alert.accept()	# 点击警告框的确认按钮

# 2.确认框：一个确认按钮 一个取消按钮
driver.find_element_by_id('confirm').click()
time.sleep(3)
alert.dismiss()	# 点击警告框的取消按钮

# 3.输入框输入内容
driver.find_element_by_id('prompt').click()
alert.send_keys('wahaha') # 在输入框输入内容
time.sleep(3)
alert.accept() # 点击确认按钮
time.sleep(3)

driver.quit()