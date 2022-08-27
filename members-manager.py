import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('example.ini')
config.read('config.ini') #overwrite values if config.ini is defined

loginResponse = requests.get('https://epiceriedal.comelin.com/admin-login?username=')
if (loginResponse):
    print('success')

cookies = loginResponse.cookies
print(cookies)

emplListResponse = requests.get('https://epiceriedal.comelin.com/admin/employe/list', cookies=cookies)
if (emplListResponse):
    print(emplListResponse.text)
