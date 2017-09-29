import requests

url = 'https://api.ipify.org'
ip = requests.get(url)

print('Your IP address is: {}'.format(ip.text))
