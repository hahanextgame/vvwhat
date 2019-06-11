import requests
import json

url = 'http://10.0.4.22:9000/content/v1/HKBBTVSSK/video/find'
headers = {
    'Host': '10.0.4.22:9000',
    'Connection': 'keep-alive',
    'Content-Length': '121',
    'Accept': '*/*',
    'Origin': 'http://10.0.4.21:7025',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://10.0.4.21:7025/t/show/HKBBTVSSK/content/article/list',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7,az;q=0.6,fr;q=0.5',

}
data = {"sourceType": "1,4,5", "status": "1,2,3", "contentType": "1,2", "orderKey": "pub_time", "order": False,
        "pageNum": 2, "pageSize": 10}
response = requests.post(url, data=json.dumps(data),headers=headers)
print(response.text)


datas = json.loads(response.text).get('data')

content = [i['content'] for i in datas.get('data')]
content = [json.loads(i) for i in content]

topicInfo = [i['topicInfo'] for i in datas.get('data')]

summary = [i['summary'] for i in datas.get('data')]
