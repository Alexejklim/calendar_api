import re

import requests
from bs4 import BeautifulSoup
from ics import Calendar
from ics.parse import ParseError

def get_html(url):
    r = requests.get(url)
    return r.text


def parser(html):
    soup = BeautifulSoup(html, 'lxml')
    columns = soup.findAll(class_="four columns")
    countrys = []
    for column in columns:
        referencelist = column.findAll('a',href =re.compile('/countries/'))
        for reference in referencelist:
            country = reference.get_text('href')
            country = re.sub('\xa0', '', country)
            countrys.append(country)
    return countrys


def get_countrys():
    url = 'https://www.officeholidays.com/countries/index.php'
    all_countrys = parser(get_html(url))
    return all_countrys


def get_holydayevents(country_name):
    url = 'https://www.officeholidays.com/ics/ics_country.php?tbl_country=' + country_name
    holydays = []
    try:
        c = Calendar(requests.get(url).text)
    except ParseError:
        pass
    else:
        for i in c.events:
            holydays.append([i.name, i._begin.datetime])        
    return holydays

for country in get_countrys():
    get_holydayevents(country)
