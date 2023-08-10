<<<<<<< HEAD
import requests
from xml.etree import ElementTree
response = requests.get('https://api.direct.yandex.ru/live/v4/wsdl/')
tree = ElementTree.fromstring(response.content)
print(tree)
print(dir(tree))
tree.find('complexType', namespaces=)
# print(response.content)
=======
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
>>>>>>> d773a47f7f769d3f194f7920aae47bf02effc5ac
