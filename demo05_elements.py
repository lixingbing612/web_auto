


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost")

# 点击登录：使用xpath的元素属性定位
driver.find_element_by_xpath("//a[@href='/Home/user/login.html']").click()

# 输入账号： 使用find_elements_by_class_name定位
print(driver.find_elements_by_class_name("text_cmu"))

driver.find_elements_by_class_name("text_cmu")[0].send_keys("131123456678")

# 输入密码
driver.find_elements_by_class_name("text_cmu")[1].send_keys("123456")

# 输入验证码
driver.find_elements_by_class_name("text_cmu")[2].send_keys("8888")
