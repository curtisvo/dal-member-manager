import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('example.ini')
config.read('config.ini') #overwrite values if config.ini is defined

loginResponse = requests.get('https://epiceriedal.comelin.com/admin-login?username='+config['Comelin']['username']+'&password='+config['Comelin']['password'])
if (loginResponse):
    print('success')

cookies = loginResponse.cookies
print(cookies)

custListResponse = requests.get('https://epiceriedal.comelin.com/Api/Customers', cookies=cookies)
if (custListResponse):
    print(custListResponse.text)

emplListResponse = requests.get('https://epiceriedal.comelin.com/admin/employe/list', cookies=cookies)
if (emplListResponse):
    print(emplListResponse.text)
