import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 页面层page
class LoginPage():
	login_link = (By.LINK_TEXT,'登录')
	username = (By.ID,'username')
	password = (By.ID,'password')
	code = (By.ID,'verify_code')
	button = (By.NAME,'sbtbutton')
	err_msg = (By.CLASS_NAME,'layui-layer-content')
	suc_msg = (By.LINK_TEXT,'13112345678')


# 逻辑层logic
class LoginLogic():

	def login(self,driver,username,password,code):
		driver.maximize_window()
		driver.find_element(*LoginPage.login_link).click()
		driver.find_element(*LoginPage.username).send_keys(username)
		driver.find_element(*LoginPage.password).send_keys(password)
		driver.find_element(*LoginPage.code).send_keys(code)
		driver.find_element(*LoginPage.button).click()
		sleep(3)


	def login_err_msg(self,driver):
		return driver.find_element(*LoginPage.err_msg).text

	def login_suc_msg(self,driver):
		return driver.find_element(*LoginPage.suc_msg).text


# 业务层case
class TestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.lg = LoginLogic()

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get('http://localhost')

	def tearDown(self) -> None:
		self.driver.quit()

	def test_login_success(self):
		self.lg.login(self.driver,'13112345678','123456','8888',)
		login_suc_msg = self.lg.login_suc_msg(self.driver)
		self.assertEqual('13112345678',login_suc_msg)

	def test_username_wrong(self):
		self.lg.login(self.driver,'1311345678','123456','8888',)
		login_err_msg = self.lg.login_err_msg(self.driver)
		self.assertEqual('账号格式不匹配!',login_err_msg)

if __name__ == '__main__':
    unittest.main()