import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('example.ini')
config.read('config.ini') #overwrite values if config.ini is defined

for key in config['Comelin']:
    print(key+"="+config['Comelin'][key])
