from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('https://bj.58.com/')

print(driver.current_url)
print(driver.window_handles)

 # 點擊合租
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[3]/a').click()
print(driver.current_url)
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')

print(len(el_list))
# # 切换窗口
# driver.switch_to.window(driver.window_handles[-1])
#
# print(driver.current_url)
# # 记录所有的窗口句柄，新打开的窗口句柄将会添加到列表尾部
# print(driver.window_handles)
#
#
# el_list = driver.find_elements_by_xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/h2/a')
# print(el_list)
#
# for el in el_list:
#     print(el.text, el.get_attribute('href'))

driver.quit()