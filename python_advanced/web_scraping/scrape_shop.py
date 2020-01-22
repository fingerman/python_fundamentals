# read name, pricce, description
# read via product link
# webscraper.io/test-sites/e-commerce/allinone

import pandas as pd
import requests
from bs4 import BeautifulSoup


r = requests.get('http://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(r.text, features='html.parser')

#products = soup.find_all(attrs=['title','price', 'description'])
products = soup.find_all('h4', {'class':'pull-right price'})
print(products)
for i in products:
    print(i)

