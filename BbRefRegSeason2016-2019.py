import requests

from selenium import webdriver
from time import sleep

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import json
import time
import copy
import pprint

def gamelogurl_to_pddf(url):  
    r = requests.get(url)
    r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    indices = tables[0].find_all('th')
    rows = tables[0].find_all('tr')
    indices, rows
    columns = {}
    for index in indices[1:32]:
        columns[index.text] = None
    d = {}
    for row in rows:
        d[row.text] = None
    all_data = []
    keys = list(columns.keys())
    for i,row in enumerate(rows):
        if i > 0:
            new_row = copy.copy(columns)
            entries = row.find_all('td')
            for j,entry in enumerate(entries):
                new_row[keys[j]]= entry.text
            all_data.append(new_row)
    return pd.DataFrame.from_records(all_data)


def gamelogurl_to_csv(url):  
    r = requests.get(url)
    r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    indices = tables[0].find_all('th')
    rows = tables[0].find_all('tr')
    indices, rows
    columns = {}
    for index in indices[1:32]:
        columns[index.text] = None
    d = {}
    for row in rows:
        d[row.text] = None
    all_data = []
    keys = list(columns.keys())
    for i,row in enumerate(rows):
        if i > 0:
            new_row = copy.copy(columns)
            entries = row.find_all('td')
            for j,entry in enumerate(entries):
                new_row[keys[j]]= entry.text
            all_data.append(new_row)
    pd.DataFrame.from_records(all_data).to_csv(f'data/{url[54:57]}{url[-4:]}.csv')


def scrape_gamelogs2016(lst):
    for team in lst:
        gamelogurl_to_csv(f'https://www.baseball-reference.com/teams/tgl.cgi?team={team}&t=b&year=2016')
        sleep(1)

def scrape_gamelogs2017(lst):
    for team in lst:
        gamelogurl_to_csv(f'https://www.baseball-reference.com/teams/tgl.cgi?team={team}&t=b&year=2017')
        sleep(1)                     

def scrape_gamelogs2018(lst):
    for team in lst:
        gamelogurl_to_csv(f'https://www.baseball-reference.com/teams/tgl.cgi?team={team}&t=b&year=2018')
        sleep(1)

def scrape_gamelogs2019(lst):
    for team in lst:
        gamelogurl_to_csv(f'https://www.baseball-reference.com/teams/tgl.cgi?team={team}&t=b&year=2019')
        sleep(1)        


