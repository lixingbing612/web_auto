
# 页面层

from selenium.webdriver.common.by import By

class LoginPage():

	login_link = (By.LINK_TEXT, '登录')
	login_username = (By.ID,'username')
	login_password = (By.ID,'password')
	login_verify = (By.ID,'verify_code')
	login_button = (By.NAME,'sbtbutton')
	login_sucess = (By.LINK_TEXT,'账户设置')
	login_errno = (By.CLASS_NAME,'layui-layer-content')

