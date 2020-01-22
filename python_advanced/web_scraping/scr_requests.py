from requests import get

url = "https://webscraper.io/test-sites/tables"
url_2 = 'https://httpbin.org/ip'

r = get(url_2)
print(r.json())