'''
获取当前窗口句柄 ：driver.current_window_handle
获取所有窗口句柄 ： driver.window_handles
切换到指定窗口句柄 ： driver.switch_to.window(handle)

'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://jrj.com.cn')

print(driver.current_window_handle)

driver.find_element_by_link_text('登录').click()
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id('txtUsername').send_keys('123')