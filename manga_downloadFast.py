#!/home/benubha/anaconda3/python3.6
import threading
import time
import requests
from bs4 import BeautifulSoup
import os

os.makedirs('/home/benubha/mangas', exist_ok=True)
os.chdir('/home/benubha/mangas')
