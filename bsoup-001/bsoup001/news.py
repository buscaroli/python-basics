# LEARNING PYTHON
# USING BEAUTIFUL SOUP 4 TO COLLECT ARTICLES
# FROM AN ITALIAN NEWSPAPER CALLED 'IL RESTO DEL CARLINO'
# Matteo

import requests, sys, news_funcs
from bs4 import BeautifulSoup

url = 'https://ilrestodelcarlino.it/'

# Town of choice passed as an argument from the console
# If nothing passed will use Bologna as the default value
if len(sys.argv) < 2:
    town = 'bologna'
else:
    town = sys.argv[1].lower()

full_url = url + town


print(f'The complete url is {full_url}')

try:
    page = requests.get(full_url)
    page.raise_for_status()
except requests.exceptions.HTTPError() as err:
    print(err)
    sys.exit(1)

soup = BeautifulSoup(page.content, "html.parser")

print(f'Collecting articles related to the town of {town.capitalize()}...')

#getting a list made up of tuples of the type (title, link)
tuples = news_funcs.get_titles_links(soup)

#DEBUG
#news_funcs.display_tuples(tuples)

# Printing the articles to the console
#news_funcs.print_articles(tuples)

# Saving articles inside separate files
news_funcs.save_articles(tuples, town)