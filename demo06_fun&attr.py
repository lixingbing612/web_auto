

# 方法或属性

"""
属性 size 返回元素大小 driver.size
属性 text 返回元素的文本信息 driver.text
方法 get_attribute("xxx")获取属性值，传递的参数为元素的属性名
方法 is_displayed() 判断元素是否可见 driver.find_element_by_id("kw").is_displayed()
方法 is_enabled() 判断元素是否可用 driver.find_element_by_id("kw").is_enabled()
方法 is_selected() 判断元素是否被选中，用来检查复选框或单选按钮是否被选中。
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost")

# 点击注册按钮
driver.find_element_by_link_text("注册").click()

# 获取注册信息的文本标题 ： text
reget_info = driver.find_element_by_xpath("//span[@class='m-fntit']").text
print(reget_info)

# 获取文本的大小 ： size
size = driver.find_element_by_xpath("//span[@class='m-fntit']").size
print(size)

# 获取属性值 get_attribute()
attri_vls = driver.find_element_by_css_selector('#reflsh_code2').get_attribute('src')
print(attri_vls)

# 判断元素是否可见 is_displayed()
a_vls = driver.find_element_by_css_selector("#password").is_enabled()
print(a_vls)
# 判断元素是否可用  is_enabled()
i_vls = driver.find_element_by_css_selector("#password").is_displayed()
print(i_vls)
# 判断元素是否被选中  is_selected()
select = driver.find_element_by_css_selector("[type=checkbox]").is_selected()
print(select)

quit()