import requests

page = 1
url = 'https://www.ssg.com/service/bestCtgItemList.ssg?'
headers = {
    #'Accept': 'text/html, */*; q=0.01',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    #'Connection': 'keep-alive',
    # 'Host': 'www.ssg.com',
    #'Referer': 'https://www.ssg.com/service/bestMain.ssg',
    #'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    #'sec-ch-ua-mobile': '?0',
    #'sec-ch-ua-platform': '"Windows"',
    #'Sec-Fetch-Dest': 'empty',
    #'Sec-Fetch-Mode': 'cors',
    #'Sec-Fetch-Site': 'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
params={
    'zoneId':'5000016005',
    #'ctgld:'',
    'page':f'{page}'   
}
response = requests.get(url, headers=headers, data=params)
# print(response.text)

def url(page):
    return f'www.ssg.com/service/bestCtgItemList.ssg?zoneId=5000016005&ctgId=&page={page}'
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
allowed_domains = []
start_urls = []
for page in range(1, 6):
    allowed_domains.append(url(page))
    start_urls.append('http://'+url(page))
#     print(url(page))
# print(allowed_domains)
# print(response.url)
# print(type(response.url))
import pandas as pd
data = pd.read_csv('ssg/ssg/data.csv')
print(data.columns)
print(data.info())
print(data.head())