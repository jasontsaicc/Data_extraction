from selenium import webdriver
import time

url = "https://www.baidu.com"

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get(url)

# #顯示源碼
# print(driver.page_source)
# #顯示響應對應的url
# print(driver.current_url)
#
# time.sleep(2)
# driver.get("https://douban.com")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

#保存網頁快照 常用於驗證碼
driver.save_screenshot('baidu.png')
driver.quit()
