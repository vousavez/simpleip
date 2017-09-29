from requests import get

response = get('https://api.ipify.org')
print(response.text)
