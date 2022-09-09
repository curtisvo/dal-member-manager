import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('example.ini')
config.read('config.ini') #overwrite values if config.ini is defined

s = requests.Session()

params = {'username': config['Comelin']['username'], 'password': config['Comelin']['password']}
loginResponse = s.get('https://epiceriedal.comelin.com/admin-login', params=params)
if (loginResponse):
    print('success')

print(s.cookies)

custListResponse = s.get('https://epiceriedal.comelin.com/Api/Customers')
if (custListResponse):
    print(custListResponse.text)

emplListResponse = s.get('https://epiceriedal.comelin.com/admin/employe/list')
if (emplListResponse):
    print(emplListResponse.status_code)
    print(emplListResponse.text)
