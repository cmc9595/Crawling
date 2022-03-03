import requests
import json
import pandas as pd

CLIENT_ID = 'b8CNbRsU6Ub8vUSkZJ8v'
CLIENT_SECRET = '721JewZp2I'
headers = {
    #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Naver-Client-Id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_SECRET,
    'Content-Type': 'application/json',
}

def get_news_data(query):
    query = '푸틴'
    url = f'https://openapi.naver.com/v1/search/news.json?query={query}&display=10&start=1'
    response = requests.get(url, headers=headers)
    
    if response.status_code!=200:
        print(response.text)
        return None
    else:
        items = response.json()['items']
        datas = []
        for i in items:
            data = {
                'title':i['title'],
                'pubDate':i['pubDate'],
                'originallink':i['originallink'],
                'description':i['description'],
                'papago':translate(i['title'])
            }
            datas.append(data)
            #print(i['title'])
        return pd.DataFrame(datas)
def translate(line):
    data = {
        'source':'ko',
        'target':'en',
        'text': line
    }
    data = json.dumps(data)
    url2 = 'https://openapi.naver.com/v1/papago/n2mt'
    response = requests.post(url2, headers=headers, data=data)
    if response.status_code==200:
        return response.json()['message']['result']['translatedText']
    else:
        return None
print(translate('배가고프다'))   
data = get_news_data('푸틴')
data.to_csv('papago.csv')