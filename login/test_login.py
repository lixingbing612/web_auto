import unittest
from selenium import webdriver
from time import sleep


class TestLogin(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("http://localhost")

	def tearDown(self) -> None:
		self.driver.quit()

	# case1：密码错误
	def test_password_is_wrong(self):
		# 1. 点击首页的'登录'按钮，进入登录页面
		self.driver.find_element_by_link_text("登录").click()
		# 2. 输入正确的用户名
		self.driver.find_element_by_id("username").send_keys("13112345678")
		# 3. 输入错误的密码
		self.driver.find_element_by_id("password").send_keys("1234567")
		# 4. 输入验证码
		self.driver.find_element_by_id("verify_code").send_keys("8888")
		# 5. 点击登录按钮
		self.driver.find_element_by_name("sbtbutton").click()
		sleep(5)
		# 6. 获取错误提示信息，并验证其信息 。
		err_msg = self.driver.find_element_by_class_name("layui-layer-content").text
		print(err_msg)
		self.assertEqual("密码错误!",err_msg)
		# result = self.driver.find_element_by_class_name("layui-layer-content").text
		# self.assertEqual("密码错误!",result)
		# print("获取到的信息：", result)


	# case2 ：登录成功
	def test_login_success(self):
		# 1. 点击首页的'登录'按钮，进入登录页面
		self.driver.find_element_by_link_text("登录").click()
		# 2. 输入正确的用户名
		self.driver.find_element_by_id("username").send_keys("13112345678")
		# 3. 输入正确的密码
		self.driver.find_element_by_id("password").send_keys("123456")
		# 4. 输入验证码
		self.driver.find_element_by_id("verify_code").send_keys("8888")
		# 5. 点击登录按钮
		self.driver.find_element_by_name("sbtbutton").click()
		sleep(5)
		# 6. 登录成功，获取账号信息 。
		suc_msg = self.driver.find_element_by_link_text("13112345678").text
		print(suc_msg)
		self.assertEqual("13112345678",suc_msg)

	# case3 ：密码为空
	def test_password_null(self):
		# 1. 点击首页的'登录'按钮，进入登录页面
		self.driver.find_element_by_link_text("登录").click()
		# 2. 输入正确的用户名
		self.driver.find_element_by_id("username").send_keys("13112345678")
		# 3. 不输入密码

		# 4. 输入验证码
		self.driver.find_element_by_id("verify_code").send_keys("8888")
		# 5. 点击登录按钮
		self.driver.find_element_by_name("sbtbutton").click()
		sleep(5)
		# 6. 获取错误提示信息，并验证其信息 。
		err_msg = self.driver.find_element_by_class_name("layui-layer-content").text
		print(err_msg)
		self.assertEqual("密码不能为空!",err_msg)

if __name__ == '__main__':
	unittest.main()
