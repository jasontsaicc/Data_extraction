from selenium import webdriver
import time

url = 'https://www.baidu.com'

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get(url)

#driver.find_element_by_xpath('//*[@id="kw"]').send_keys('iphone12')

# driver.find_element_by_css_selector('#kw').send_keys('iphone12')

# driver.find_element_by_name('wd').send_keys('iphone12')

#driver.find_element_by_class_name('s_ipt').send_keys('iphone12')

#driver.find_element_by_id('su').click()

# driver.find_element_by_link_text('hao123').click()

driver.find_element_by_partial_link_text('hao').click()
time.sleep(3)
driver.quit()