'''# 3.操作方法，支持的方法有：
context_click(element) #右击 --> 模拟鼠标右击点击效果
#等待的三种方法：
double_click(element) #双击 -->模拟鼠标双击
drag_and_drop(source,target) #拖动 -->模拟鼠标拖动效果
move_to_element(element) #悬停 -->模拟鼠标悬停效果'''

# 鼠标操作

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 创建ActionChains对象	实例化对象
action = ActionChains(driver)

# 鼠标双击
change = driver.find_element_by_xpath("//span[@class='hot-refresh-text']")
action.double_click(change).perform()
sleep(3)

# 鼠标单击
click = driver.find_element_by_xpath("//area[@target='_blank']")
action.click(click).perform()
sleep(2)

# 全屏
driver.maximize_window()
sleep(2)

#  鼠标右键
space = driver.find_element_by_xpath("//a[@name='tj_briicon']")
action.context_click(space).perform()
sleep(2)

# 输入京东
driver.find_element_by_css_selector("#kw").send_keys("京东")
sleep(2)

# 点击百度一下
driver.find_element_by_css_selector("#su").click()
sleep(2)

# 选择京东首页
driver.find_element_by_xpath("//div[@class='c-img-border c-img-radius-large']").click()

login = driver.find_element_by_xpath("//a[@class=link-login]")
#  鼠标悬停
action.move_to_element(login).perform()

good_type_home = driver.find_element_by_xpath("//a[@href='/Home/Goods/goodsList/id/2.html']")

action.move_to_element(good_type_home).perform()

quit()