# import requests
#
# value = input('Введите текст:')
#
# url = 'https://raskladki.net.ru/post.php'
# response = requests.post(url, data=dict(text=value, lang='eng2rus'))
# print(response.text)
#
#
# print(isinstance(2, str))
# import datetime
# import time
#
# for i in range(4):
#     print(i)
# print(datetime.datetime.now())
#
# a = datetime.datetime.now()
# print(f"{a.day}-{a.month}-{a.year} {a.hour}:{a.minute}:{a.second}")
import requests

data = {"user": "admin", "password": "testtest1"}
response = requests.post('https://strojregionfilomena.workhere.ru/api/auth/login', data=data).json()
print(response['data']['token'])

for i in range(1,5):
    print(i)
