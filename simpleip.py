def myip():
  from requests import get
  return get('https://api.ipify.org')
