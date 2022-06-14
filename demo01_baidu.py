# 需求：在百度输入框中输入关键字python进行搜索
'''context_click(element) #右击 --> 模拟鼠标右击点击效果
#等待的三种方法：
double_click(element) #双击 -->模拟鼠标双击
drag_and_drop(source,target) #拖动 -->模拟鼠标拖动效果
move_to_element(element) #悬停 -->模拟鼠标悬停效果'''
# 1.导包
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 2.创建浏览器驱动
driver = webdriver.Chrome()
# 3.打开web页面-百度
driver.get("http://www.baidu.com")
# 4.暂停3s
time.sleep(3)
# 5.在浏览器中输入关键字：python
driver.find_element_by_id("kw").send_keys("python")
time.sleep(3)

driver.find_element_by_id('kw').clear()
time.sleep(3)

driver.find_element_by_id('kw').send_keys('java')
time.sleep(3)

# 6.点击按钮 ： 百度一下
driver.find_element_by_id("su").click()
# 7.暂停：
time.sleep(3)
# 8.后退
driver.back()
time.sleep(3)

# 9.前进
driver.forward()
time.sleep(3)

# 10.刷新
driver.refresh()
time.sleep(3)

# 11.窗口最大化
driver.maximize_window()
time.sleep(3)

# 8.关闭浏览器
driver.quit()

"""
方法 get(url) 在地址栏中输入url地址	driver.get("http://www.baidu.com")
方法 click() 点击 driver.find_element_by_id("su").click()
方法 send_keys(“内容”)	输入框输入内容 driver.find_element_by_id("kw").send_keys("python")
方法 clear() 清除输入框内容 driver.find_element_by_id("kw").clear()
属性 title 打印标题 driver.title
属性 current_url 打印当前页的url driver.current_url
方法 maximize_window()浏览器最大化 driver.maximize_window()
方法 forward() 前进 driver.forward()
方法 back() 后退 driver.back()
方法 refresh() 刷新 driver.refresh()
方法 close() 关闭当前窗口 driver.close()
方法 quit() 关闭所有窗口 driver.quit()
"""
