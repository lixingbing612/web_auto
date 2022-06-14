

# 使用xpath定位
"""
1. 属性定位 = 相对路径 + 属性名
格式： //标签名[@属性名=值]
2. 属性与逻辑结合：
格式：//标签名[@属性名1='值' and 属性名2='值2']
3. 属性与层级结合
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost")
# 点击登录：使用xpath的元素属性定位
driver.find_element_by_xpath("//a[@href='/Home/user/login.html']").click()

driver.find_element_by_xpath("//input[@class='text_cmu' and @name='username']").send_keys('13112345678')