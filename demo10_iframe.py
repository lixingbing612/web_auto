
# iframe 框架

"""
# 方法
1. driver.switch_to.frame(frame_reference) :切换到指定frame的方法
2. driver.switch_to.default_content() :恢复默认页面方法

"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://i.qq.com')

driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()