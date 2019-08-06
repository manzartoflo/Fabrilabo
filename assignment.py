#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:55:58 2019

@author: manzar
"""

import requests
from bs4 import BeautifulSoup

url = "http://fabrilabo.com/?page_id=67&lang=en"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

name = soup.findAll('div', {'class': 'title-block'})

webs = soup.findAll('div', {'class', 'button-block'})\

discription = soup.findAll('div', {'class': 'description-block_2'})