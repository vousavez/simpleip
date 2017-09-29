import requests

ans = input('Check IP ? ')
if ans == True:
  response = requests.get('https://api.ipify.org')
  print(response.text)
