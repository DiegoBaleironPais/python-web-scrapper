import urllib3
import re
from bs4 import BeautifulSoup

url = "https://myanimelist.net/anime.php?cat=0&q=&type=0&score=8&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[0]=a&c[1]=b&c[2]=c&c[3]=f&genre[0]=1&o=3&w=1"

if __name__ == '__main__':
    response = urllib3.request("GET",url)
    if response.status == 200:
        html_content = response.data.decode("utf-8")

        soup = BeautifulSoup(html_content,"html.parser")

        for tag in soup.find_all('a', class_="hoverinfo_trigger fw-b fl-l"):
            print(tag)

        #print(soup.prettify())
        print(soup.title.name)
    else:
        print(f"HTTP error during request: Error {response.status}")