from requests import get
ip = get('https://api.ipify.org')

print(ip.text)
