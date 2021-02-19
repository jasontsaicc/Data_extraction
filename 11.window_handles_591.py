from selenium import webdriver
import time
url = 'https://www.591.com.tw/'

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get(url)

driver.find_element_by_xpath('//*[@id="area-box-body"]/dl[1]/dd[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/nav/div/div[3]/ul/li[3]/a').click()

el_list = driver.find_elements_by_xpath('//*[@id="content"]/ul/li[2]/h3')

driver.quit()

