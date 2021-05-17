#!/usr/local/bin/python3

import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

OUTPUT_NAME = 'output/log.csv'
URL = 'https://www.dreamfit.es/centros/moratalaz'

# Fetch HTML from dreamfit
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

# Find relevant data
capacity = soup.select_one('.aforo ul li:nth-child(2) .number')
n = soup.select_one('.aforo ul li:nth-child(3) .number')

if not capacity:
    capacity = 0
else:
    capacity = capacity.string

if not n:
    n = 0
else:
    n = n.string

# Append

dtime = datetime.now(timezone('Europe/Madrid')).strftime("%Y-%m-%d %H:%M:%S%z")

print('[' + dtime + ']', 'Appending new data...')

df_new = pd.DataFrame({
    'date': [dtime],
    'capacity': [capacity],
    'n': [n]
})

try:
    df = pd.read_csv(OUTPUT_NAME, sep = ";")
    df = pd.concat([df, df_new])
except FileNotFoundError:
    df = df_new

df.to_csv(OUTPUT_NAME, sep = ";", index = False)