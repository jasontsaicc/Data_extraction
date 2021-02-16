import requests
from lxml import etree

class Tieba(object):

    def __init__(self, name):
        self.url = "https://tieba.baidu.com/f?kw={}".format(name)
        print(self.url)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
            #"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        with open("temp.html", "wb") as f:
            f.write(response.content)
        return response.content

    def parse_data(self, data):
        #創建element對象
        data = data.decode().replace("<!--","").replace("-->!","")
        html = etree.HTML(data)

        el_list = html.xpath('//li[@class=" j_thread_list clearfix thread_item_box"]/div/div[2]/div[1]/div[1]/a')
        #print(len(el_list))
        data_list = []

        for el in el_list:
            temp = {}
            temp['title'] = el.xpath("./text()")[0]
            temp['link'] = "https://tieba.baidu.com/" + el.xpath("./@href")[0]
            data_list.append(temp)

        #獲取下一頁
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页>")]/@href')[0]
        except:
            next_url = None
        return data_list , next_url

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        #url
        #headers
        next_url = self.url

        while True:
            #發送請求，獲取響應
            data = self.get_data(next_url)
            #從響應中提取數據（數據和翻頁用的url）
            data_list, next_url = self.parse_data(data)

            self.save_data(data_list)

            print(next_url)
            #判斷是否終結
            if next_url == None:
                break

if __name__ == '__main__':
    tieba = Tieba("书")
    tieba.run()