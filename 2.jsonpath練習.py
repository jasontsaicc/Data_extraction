import requests
import json
import jsonpath

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}

response = requests.get(url, headers=headers)
html_str = response.content.decode()
jsonobj = json.loads(html_str)

citylist = jsonpath.jsonpath(jsonobj, '$..name')

print (jsonobj)
print(citylist)

with open('city_name.txt','w') as f:
    content = json.dumps(citylist, ensure_ascii=False)
    f.write(content)

