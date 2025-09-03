import requests
city=input("Enter the city name: ")
url=f"https://v2.xxapi.cn/api/weather?city={city}"
response=requests.get(url)
data=response.json()
print(f"The weather in {data['data']['city']}is{data['data']['data'][0]['weather']}")