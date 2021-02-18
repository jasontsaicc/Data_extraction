import time
from selenium import webdriver

# 通過指定chromedriver的路徑來實例化driver對象，chromedriver放在當前目錄。
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# chromedriver已經添加環境變數
#driver = webdriver.Chrome()

# 控製瀏覽器訪問url地址
driver.get("https://www.baidu.com/")

# 在百度搜索框中搜索'python'
driver.find_element_by_id('kw').send_keys('python123')
# 點選'百度搜索'
driver.find_element_by_id('su').click()

time.sleep(6)
# 退出瀏覽器
driver.quit()