from bs4 import BeautifulSoup
import re, requests, sys


url = 'https://www.ilrestodelcarlino.it/rimini/meteo/caldo-ottobre-1.4842921'


try:
    page = requests.get(url)
    page.raise_for_status()
except requests.exceptions.HTTPError() as err:
    print(err)
    sys.exit(1)

soup = BeautifulSoup(page.content, "html.parser")

title = 'My Article'
article = soup.find_all('p')
print(f'''{title}''')
for line in range (len(article)-2):
    print(article[line].text)
