from urllib.request import urlopen
from bs4 import BeautifulSoup
import string

html = urlopen("https://it.wikipedia.org/wiki/Eliofania_in_Italia")
soup = BeautifulSoup(html, features = 'html.parser')
for paragraph in soup.findAll('p'):
    print(10 * '~')
    print(paragraph.contents[1].string)
    print(10 * '~')
    print(paragraph.get_text())