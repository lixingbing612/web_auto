

from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.by import By


class LoginPage():

	# 找到定位登录连接对象
	login_link = (By.LINK_TEXT,'登录')
	# 用户输入框对象
	username = (By.ID,'username')
	# 密码输入框对象
	password = (By.ID,'password')
	# 验证码输入框对象
	verify_code = (By.ID,'verify_code')
	# 登录按钮对象
	login_button = (By.NAME,'sbtbutton')
	# 登录成功消息对象
	success_msg = (By.LINK_TEXT,'13112345678')
	# 登录失败对象
	errno_msg = (By.CLASS_NAME,'layui-layer-content')


class LoginLogic():

	# 对定义登录的步骤进行操作
	def login(self,driver,username,password,verify_code):
		driver.find_element(*LoginPage.login_link).click()
		driver.maximize_window()
		driver.find_element(*LoginPage.username).send_keys(username)
		driver.find_element(*LoginPage.password).send_keys(password)
		driver.find_element(*LoginPage.verify_code).send_keys(verify_code)
		driver.find_element(*LoginPage.login_button).click()
		sleep(3)

	def login_success(self,driver):
		return driver.find_element(*LoginPage.success_msg).text

	def login_wrong(self, driver):
		return driver.find_element(*LoginPage.errno_msg).text


class TestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.lg = LoginLogic()

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("http://localhost")

	def tearDown(self) -> None:
		self.driver.quit()

# 编写测试用例
	def test_login_success(self):
		self.lg.login(self.driver, "13112345678", "123456", "8888")
		success_msg = self.lg.login_success(self.driver)
		self.assertEqual("13112345678",success_msg)
	def test_username_wrong(self):
		self.lg.login(self.driver,'1313131313','123456','8888')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('账号格式不匹配!',errno_msg)
	def test_username_not_exits(self):
		self.lg.login(self.driver,'13131313133','123456','8888')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('账号不存在!',errno_msg)
	def test_username_is_null(self):
		self.lg.login(self.driver,'','123456','8888')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('用户名不能为空!',errno_msg)
	def test_password_wrong(self):
		self.lg.login(self.driver,'13112345678','131211','8888')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('密码错误!',errno_msg)
	def test_password_is_null(self):
		self.lg.login(self.driver,'13112345678','','8888')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('密码不能为空!',errno_msg)
	def test_verify_wrong(self):
		self.lg.login(self.driver,"13112345678", "123456", "8828")
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('验证码错误',errno_msg)
	def test_verify_is_null(self):
		self.lg.login(self.driver,'13112345678','123456','')
		errno_msg = self.lg.login_wrong(self.driver)
		self.assertEqual('验证码不能为空!',errno_msg)
if __name__ == '__main__':
    unittest.main()