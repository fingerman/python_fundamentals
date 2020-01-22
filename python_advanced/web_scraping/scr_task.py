import pandas as pd
import requests
from bs4 import BeautifulSoup

# read html to data frame
df = pd.read_html('https://webscraper.io/test-sites/tables', header=0, index_col=0)[0]
print(df)
print(type(df))
print(df.head())


# mit soup
r = requests.get('https://webscraper.io/test-sites/tables')
soup = BeautifulSoup(r.text, features='html.parser')
table_1 = soup.find('table')
df1 = pd.read_html(str(table_1), header=0, index_col=0)[0]
print(df1)
