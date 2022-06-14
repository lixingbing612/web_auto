import os
import unittest
from selenium import webdriver
from time import sleep
import allure
import pytest

"""
@allure.epic() : epic描述 ，类似项目名称
@allure.feature() ：用于定义被测试的功能，被测产品的需求点 ，如登录功能
@allure.story() ： 用于定义被测功能的用户场景，即子功能点
@allure.title(用例的标题): 用例的标题
@allure.testcase() : 测试用例的链接地址，对应功能测试用例系统里的case
@allure.issue() : 缺陷 ，对应缺陷管理系统里面的链接 。
@allure.description() : 用例描述 ，测试用例的描述信息
@allure.step() ：用于将一个测试用例，分成几个步骤在报告中输出
@allure.serverity() : 用例等级 ，包括blocker ,critical ,normal ,minor ,trivial
@allure.link() : 链接，定义一个链接 ，在测试报告中展现
@allure.attach ： 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
"""

@allure.feature('登录模块')
@allure.story('登录子模块：登录的正向和反向用例')
class TestLogin(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("http://localhost")

	def tearDown(self) -> None:
		self.driver.quit()

	# case1：密码错误
	@allure.title('密码错误')
	@allure.description('输入正确的用户名错误的密码，点击登录，返回密码错误')
	def test_password_is_wrong(self):

		with allure.step('验证密码错误'):
			allure.attach('1.点击登录按钮')
			allure.attach('2.输入正确用户名{}'.format('13112345678'))
			allure.attach('3.输入错误密码{}'.format('1234567'))
			allure.attach('4.输入正确验证码{}'.format('8888'))
			allure.attach('5.点击登录按钮')
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
	@allure.title('登录成功')
	@allure.description('输入正确的用户名正确的密码，点击登录，返回登录成功')
	def test_login_success(self):

		with allure.step('验证密码错误'):
			allure.attach('1.点击登录按钮')
			allure.attach('2.输入正确用户名{}'.format('13112345678'))
			allure.attach('3.输入正确密码{}'.format('123456'))
			allure.attach('4.输入正确验证码{}'.format('8888'))
			allure.attach('5.点击登录按钮')
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
	@allure.title('密码为空')
	@allure.description('输入正确的用户名不输入的密码，点击登录，返回密码为空')
	def test_password_null(self):

		with allure.step('验证密码错误'):
			allure.attach('1.点击登录按钮')
			allure.attach('2.输入正确用户名{}'.format('13112345678'))
			allure.attach('3.输入空密码{}'.format(''))
			allure.attach('4.输入正确验证码{}'.format('8888'))
			allure.attach('5.点击登录按钮')
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
	# unittest.main()
	json_dir_path = 'json_path'
	html_dir_path = 'html_path'
	args_list = ['-s','-v','test_login_report.py','--alluredir',json_dir_path]
	pytest.main(args_list)

	# 使用allure命令，生成测试报告
	cmd = 'allure generate {} -o {} -c'.format(json_dir_path,html_dir_path)
	os.system(cmd)