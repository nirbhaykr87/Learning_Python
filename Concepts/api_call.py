import requests

url = "https://api.freeapi.app/api/v1/public/randomjokes"
response = requests.get(url)


if response.status_code==200:
    data=response.json()
    print(data['data']['data'][1]['content'])
    