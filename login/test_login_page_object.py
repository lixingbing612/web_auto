# 使用po模式进行设计测试用例
"""
页面层（page）：所有需要操作的页面对象都封装到page层
操作层（logic）：所有功能操作顺序（逻辑）
业务层（TestCase）：进行测试用例的编写
"""
# 导包
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# 对象层 ： 定义页面元素
class LoginPage():
	# 点击登录按钮对象
	login_link_elem = (By.LINK_TEXT, "登录")
	# 用户名对象
	username_elem = (By.ID, "username")
	# 密码对象
	password_elem = (By.ID, "password")
	# 验证码对象
	verify_elem = (By.ID, "verify_code")
	# 登录对象
	login_button_elem = (By.NAME, "sbtbutton")
	# 登录成功消息对象
	login_success_msg = (By.LINK_TEXT, "13112345678")
	# 登录失败信息对象
	login_error_msg = (By.CLASS_NAME, "layui-layer-ico layui-layer-close layui-layer-close1")


# 操作层 ： 定义操作逻辑（顺序）
class LoginLogic():
	# 定义登录
	def login(self, driver, username, password, verify_code):
		# 点击登录按钮
		driver.find_element(*LoginPage.login_link_elem).click()
		# 输入用户名
		driver.find_element(*LoginPage.username_elem).send_keys(username)
		# 输入密码
		driver.find_element(*LoginPage.password_elem).send_keys(password)
		# 输入验证码
		driver.find_element(*LoginPage.verify_elem).send_keys(verify_code)
		# 点击登录
		driver.find_element(*LoginPage.login_button_elem).click()
		sleep(3)

	# 获取错误消息
	def get_password_errno_msg(self,driver):
		return driver.find_element(*LoginPage.login_error_msg).text

	# 获取成功消息
	def get_login_success_msg(self,driver):
		return driver.find_element(*LoginPage.login_success_msg).text


# 业务层 ： 定义测试用例
class TestLogin(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.lg = LoginLogic()

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("http://localhost")

	def tearDown(self) -> None:
		self.driver.quit()

	# case1 登录成功
	def test_login_success(self):
		self.lg.login(self.driver,"13112345678","123456","8888")
		login_success_msg = self.lg.get_login_success_msg(self.driver)
		self.assertEqual("13112345678",login_success_msg)

	# case2 密码错误
	def test_password_is_wrong(self):
		self.lg.login(self.driver,"13112345678","1234567","8888")
		err_msg = self.lg.get_password_errno_msg(self.driver)
		self.assertEqual("密码错误!",err_msg)

	# case3 密码为空
	def test_password_is_null(self):
		self.lg.login(self.driver,"13112345678","","8888")
		err_msg = self.lg.get_password_errno_msg(self.driver)
		self.assertEqual("密码不能为空!",err_msg)

if __name__ == '__main__':
	unittest.main()

