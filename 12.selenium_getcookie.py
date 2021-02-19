from selenium import webdriver
import time
url = 'https://www.google.com/'

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get(url)

# print(driver.get_cookies())

cookies = {}
for data in driver.get_cookies():
    cookies[data['name']] = data['value']

print(cookies)
# driver.quit()