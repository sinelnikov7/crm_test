import requests
from xml.etree import ElementTree
response = requests.get('https://api.direct.yandex.ru/live/v4/wsdl/')
tree = ElementTree.fromstring(response.content)
print(tree)
print(dir(tree))
tree.find('complexType', namespaces=)
# print(response.content)