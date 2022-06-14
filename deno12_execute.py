from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://baidu.com')

driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
sleep(3)

# 鼠标下滑底部
js = 'window.scrollTo(0, document.body.scrollHeight)'
driver.execute_script(js)
sleep(3)
# 鼠标上滑顶部
js = 'window.scrollTo(0, document.body.scrollTop=0)'
driver.execute_script(js)


