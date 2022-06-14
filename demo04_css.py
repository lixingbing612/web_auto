

# 使用css定位
"""
css定位方式：
1.通过id定位： #元素名
2.通过class定位： .属性值
3.通过属性选择器定位： [属性名=值]
4.通过组合定位： #元素[属性名=值]	 #元素名.属性值	 .属性值[属性名=值]
"""

# 点击登录
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost")

# 点击登录：使用xpath的元素属性定位
driver.find_element_by_xpath("//a[@href='/Home/user/login.html']").click()

# 输入用户名：使用css的id定位
driver.find_element_by_css_selector("#username").send_keys("13112345678")

# 输入密码：使用css的属性定位
driver.find_element_by_css_selector("[type='password']").send_keys("123456")

# 输入验证 css组合选择器进行定位
driver.find_element_by_css_selector("input#verify_code").send_keys("8888")

# 点击登录 css的class选择器定位
driver.find_element_by_css_selector(".J-login-submit").click()

