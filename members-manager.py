import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('example.ini')
config.read('config.ini') #overwrite values if config.ini is defined

s = requests.Session()

#params = {'username': config['Comelin']['username'], 'password': config['Comelin']['password']}
#loginResponse = s.get('https://epiceriedal.comelin.com/admin-login', params=params)
#if (loginResponse):
#    print('success')

data={
    'ctl00$cp$txtPassword':config['Comelin']['password'], 
    'ctl00$cp$cmdConnect':'Se+connecter', 
    '__VIEWSTATE': '/wEPDwUKLTgzMjE2ODE0MGRk0Hac/nPOyUDk/IkgIF7fT2dmNhgMCji7TXeZz3xhxds=', 
    '__VIEWSTATEGENERATOR': '82312306', 
    '__EVENTVALIDATION': '/wEdAAPgv4UYYoNz0vSrmOQVDw6gv/Q6v4a8EcF0W8X+HyR3nQio+wlyS62GHXUS+QQQsXRBaLk+Ri+KeDLS2UBV8HbFw0ufEBh3FQw6VoPc8qcs/A=='}
    
loginResponse2 = s.post('https://epiceriedal.comelin.com/admin/login.aspx', data=data)
if (loginResponse2):
    print('success')

print(s.cookies)

custListResponse = s.get('https://epiceriedal.comelin.com/Api/Customers')
if (custListResponse):
    print(custListResponse.text)

emplListResponse = s.get('https://epiceriedal.comelin.com/admin/employe/list')
if (emplListResponse):
    print(emplListResponse.status_code)
    print(emplListResponse.text)
