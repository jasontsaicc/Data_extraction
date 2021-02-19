from selenium import webdriver

url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get(url)

top100_list = driver.find_elements_by_xpath('//*[@id="main"]/div/div[3]/div/div/div[3]/h3/a')

for top100 in top100_list:
    print(top100.text)

driver.quit()