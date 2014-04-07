#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = "http://html.cita.illinois.edu/nav/dtable/dtable-example-simple.php"

response = requests.get(url)

soup = BeautifulSoup(response.text)

values = list()

for table in soup.find_all('table'):
  for tr in table.find_all('tr'):
    for td in tr.find_all('td'):
      values.append(td.string)

values = [value for value in values if value is not None]
values = [float(value.replace('%', '').replace(',', '.')) for value in values]

# Special bonus
#filter(lambda x: x>80, values)
