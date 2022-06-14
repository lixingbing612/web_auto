
# 鼠标操作

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://localhost")


# 1. 创建ActionChains对象
action = ActionChains(driver)


# 获取登录元素 ：
login_elm = driver.find_element_by_xpath("//a[@href='/Home/user/login.html']")



# 2. 去调用鼠标操作的方法

# 2.1 )鼠标右击 ：context_click()
action.context_click(login_elm).perform()
# time.sleep(5)  强制等待

driver.implicitly_wait(10)


# 2.2 ） 鼠标悬停 ：move_to_element()  , 鼠标移动到家用电器的分类上

good_type_home = driver.find_element_by_xpath("//a[@href='/Home/Goods/goodsList/id/2.html']")

action.move_to_element(good_type_home).perform()