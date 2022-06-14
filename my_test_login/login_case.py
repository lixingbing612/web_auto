
# 业务层

import unittest
from my_test_login.login_logic import LoginLogic
from selenium import webdriver


class TestLogin(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.lgc = LoginLogic()

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get('http://localhost')

	def tearDown(self) -> None:
		self.driver.quit()

	def test_login_success(self):
		self.lgc.login(self.driver, "13112345678", "123456", "8888")
		success_msg = self.lgc.login_success(self.driver)
		self.assertEqual("账户设置",success_msg)
	def test_username_wrong(self):
		self.lgc.login(self.driver,'1313131313','123456','8888')
		errno_msg = self.lgc.login_wrong(self.driver)
		self.assertEqual('账号格式不匹配!',errno_msg)
	# def test_username_not_exits(self):
	# 	self.lgc.login(self.driver,'13131313133','123456','8888')
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('账号不存在!',errno_msg)
	# def test_username_is_null(self):
	# 	self.lgc.login(self.driver,'','123456','8888')
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('用户名不能为空!',errno_msg)
	# def test_password_wrong(self):
	# 	self.lgc.login(self.driver,'13112345678','131211','8888')
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('密码错误!',errno_msg)
	# def test_password_is_null(self):
	# 	self.lgc.login(self.driver,'13112345678','','8888')
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('密码不能为空!',errno_msg)
	# def test_verify_wrong(self):
	# 	self.lgc.login(self.driver,"13112345678", "123456", "8828")
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('验证码错误',errno_msg)
	# def test_verify_is_null(self):
	# 	self.lgc.login(self.driver,'13112345678','123456','')
	# 	errno_msg = self.lgc.login_errno_msg(self.driver)
	# 	self.assertEqual('验证码不能为空!',errno_msg)
if __name__ == '__main__':
    unittest.main()