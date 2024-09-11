import urllib3
from bs4 import BeautifulSoup

url = "https://www.imdb.com/?ref_=nv_home"

if __name__ == '__main__':
    response = urllib3.request("GET",url)
    