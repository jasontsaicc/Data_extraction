from selenium import webdriver

url = 'https://www.google.com'
opt = webdriver.ChromeOptions()

opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=opt)

driver.get(url)

driver.save_screenshot('google_screen.jpg')

driver.quit()