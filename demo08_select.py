
# 选择下拉框
"""
方法：
1.select_by_index(index)	通过索引获取它的值
2.select_by_value(value)	value代表的是value对应的值
3.select_by_visible_text(text)	text代表文本内容

"""
# 导包
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

# 初始化webdriver对象并打开浏览器
driver = webdriver.Chrome()
driver.get('file:///C:/Users/%E6%9D%8E%E6%98%9F%E5%86%B0/Desktop/drop_down.html')

element = driver.find_element_by_name('辛弃疾')

# 创建select的实例化对象：Select（elem），elem为定位元素的对象
select = Select(element)

# 使用对应的方法来进行选择
sleep(3)
select.select_by_index(2)	# 获取列表中第3个元素

sleep(3)
select.select_by_value('01')	# 获取列表中第一个元素

sleep(3)
select.select_by_visible_text('可怜白发生！')	# 获取列表中的此文本

driver.quit()