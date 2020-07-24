''' 
   Python Web Scraper, still in early stages, started: 27/6/20

   main
'''

#ALSO : pip install -r requirements.txt to download requirements

'''     **** EXAMPLE FOR FUTURE USE **** --- - - - EXTRACT DATA FROM SECTION OF HTML FILE

            if u wanna extract smt that's for e.g. within the <p> section of a html file
            use beautiful soup as follows

            raw_html = open('example.html').read()
            html = BeautifulSoup(raw_html, 'html.parser')
            for paragraph in html.select('p'):
                if p['id'] == 'walrus':
                    print(paragraph.text)

            this will output the whole paragraph that contains the word 'walrus'
'''

from functions import *


def main():
    # testing 
    user_input = input("What do you want to search? ")
    titles, links, descriptions = get_links(user_input)
    print(links)
    



main()