import requests
import time
import random
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://www.foody.vn/ha-noi',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    # 't' : '1714801360103',
    'page': '1',
    'lat': '21.033333',
    'lon': '105.85',
    'count': '12',
    'districtId':'', 
    'cateId': '',
    'cuisineId': '',
    'isReputation': '',
    'type' : '1',
}

product_id = []

def scrape_data(endpoint, params):
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        print('Request success!!!')
        return response.json().get('Items', [])
    else:
        print('Request failed!!!')
        return []


endpoint = 'https://www.foody.vn/__get/Place/HomeListPlace'


for i in range(1, 15):
    params['page'] = i
    data = scrape_data(endpoint, params)
    for record in data:
        product_id.append({
            'Id': record.get('Id'),
            'Name': record.get('Name'),
            'Address': record.get('Address'),
            'Phone': record.get('Phone'),
            'Image': record.get('PhotoUrl')
        })
    time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)

