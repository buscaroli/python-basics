import re, requests
import time as t
from time import gmtime, strftime
from bs4 import BeautifulSoup
def get_titles_links(soup):
    '''Creates and returns a list of tuples of the type
    (title, link)'''
    list_of_links = soup.find_all('a', attrs=re.compile('title'))
    titles=[]
    links=[]
    for link in list_of_links:
        titles.append(link.text)
        links.append(link.get('href'))
    list_of_tuples = list(zip(titles, links))
    return list_of_tuples

def display_tuples(tuples):
    '''Prints the tiles and the corresponding links'''
    for title, link in tuples:
        if len(title) > 50:
            title = title[:47] + '...'
            print(f'''TITLE: {title[:47] + '...'}\n\t{link}''')
        else:
            print(f'''TITLE: {title}\n\t{link}''')

def print_articles(tuples):
    '''Gets the articles from the links in the Webpage and 
    prints them to the console. Takes the list of tuples as 
    an argument'''
    missed_articles = 0
    for title, link in tuples:
        try:
            page = requests.get(link)
            page.raise_for_status()
        except:
            print(f'''Couldn't get this article: {title}, skipping...''')
            missed_articles = missed_articles + 1
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        article = soup.find_all('p')
        
        # Printing the article. Skipping the last two
        # paragraphs as they contain copyright info
        # Would use the copyright iinfo if using this
        # code for an app that would be shared with the
        # public but this is just an exercise
        print(f'''\n\t<~ {title} ~>\n\n''')
        for line in range(len(article)-2):
            print(article[line].text)
        
        # Waiting one second before downloading another 
        # article to be kind to the server
        t.sleep(1)

def save_articles(tuples, town):
    '''Gets the articles from the links in the Webpage and saves
    them to a local file. Takes the list of tuples as an argument'''
    missed_articles = 0
    for title, link in tuples:
        try:
            page = requests.get(link)
            page.raise_for_status()
        except:
            print(f'''Couldn't get this article: {title}, skipping...''')
            missed_articles = missed_articles + 1
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        article = soup.find_all('p')
        
        # Saving the article. Skipping the last two
        # paragraphs as they contain copyright info
        # Would use the copyright iinfo if using this
        # code for an app that would be shared with the
        # public but this is just an exercise
        counter = 1
        # Saving the articles in a file whose name represents
        # the town name and the current date and time
        filename = town.capitalize() + '-' + strftime('%Y-%m-%d-%Hhours', gmtime()) + '.txt'
        with open (filename, 'a') as filehandle:
            filehandle.write(f'\t********** {title} **********\n')
            for line in range(len(article)-2):
                filehandle.write(article[line].text)
                filehandle.write('\n\n')
                counter = counter + 1
                
        # Waiting one second before downloading another 
        # article to be kind to the server
        t.sleep(1)

