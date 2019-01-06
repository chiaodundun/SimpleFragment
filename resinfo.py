#! /usr/bin/python3
'''
start the result script
'''
from isconnected import check_connection
import mesApi
import requests
import os
from bs4 import BeautifulSoup
import time

url = 'http://14.139.205.173:83/Default.aspx'
testUrl = 'http://www.google.com'

def get_working():
    check_connection()      # will throw error if problem with net connectivity
    while True:
        try:
            res = requests.get(url)
            while True:
                try:
                    mesApi.SendMessage('Result Out For IIIT Ranchi',[9459372335])
                    break
                except Exception as e:
                    print(e)
                    t=60*10
                    continue
            break

        except requests.exceptions.RequestException as e:
            t = 60*60*2
            time.sleep(t)
            continue


get_working()
