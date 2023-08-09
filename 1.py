import requests

value = input('Введите текст:')

url = 'https://raskladki.net.ru/post.php'
response = requests.post(url, data=dict(text=value, lang='eng2rus'))
print(response.text)


print(isinstance(2, str))
