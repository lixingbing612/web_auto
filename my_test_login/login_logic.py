
# 操作层
from time import sleep

from my_test_login.login_page import LoginPage



class LoginLogic():

	# def login(self,driver,username,password,verify):
	# 	driver.find_element(*LoginPage.login_link).click()
	# 	driver.find_element(*LoginPage.login_username).send_keys(username)
	# 	driver.find_element(*LoginPage.login_password).send_keys(password)
	# 	driver.find_element(*LoginPage.login_verify).send_keys(verify)
	# 	driver.find_element(*LoginPage.login_button).click()
	# 	sleep(5)
	# def login_sucess_msg(self,driver):
	# 	return driver.find_element(*LoginPage.login_sucess).text
	#
	# def login_errno_msg(self,driver):
	# 	return driver.find_element(*LoginPage.login_errno).text

	# 对定义登录的步骤进行操作
	def login(self,driver,username,password,verify_code):
		driver.find_element(*LoginPage.login_link).click()
		driver.maximize_window()
		driver.find_element(*LoginPage.login_username).send_keys(username)
		driver.find_element(*LoginPage.login_password).send_keys(password)
		driver.find_element(*LoginPage.login_verify).send_keys(verify_code)
		driver.find_element(*LoginPage.login_button).click()
		sleep(3)

	def login_success(self,driver):
		return driver.find_element(*LoginPage.login_sucess).text

	def login_wrong(self, driver):
		return driver.find_element(*LoginPage.login_errno).text