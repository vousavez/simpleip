from requests import get

url = 'https://api.ipify.org'
ip = get(url)

print('Your IP address is: {}'.format(ip.text))
