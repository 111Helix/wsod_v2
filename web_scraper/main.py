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
    # testing get_links() function
    # user_input = input("What do you want to search? ")
    
    # print(links)
    
    # testing get_pics() function


    print("\nHello! Here are our options:\n\t1. Download images from imgur.com\n\t2. Download images from google (small version)\n\t3. Download images from google(big version)\n\t4. Extract links from a google search")
    user_input = input("Please input 1,2,3 or 4: ")
    if int(user_input) == 1:
        user_input = (input("Please enter your search query: "))
        imgur_save_pics(user_input)
    elif int(user_input) == 2:
        user_input = (input("Please enter your search query: "))
        google_save_pics_small(user_input)
    elif int(user_input) == 3:
        user_input = (input("Please enter your search query: "))
        google_save_pics_big(user_input)
    elif int(user_input) == 4:
        user_input = (input("Please enter your search query: "))
        titles, links, descriptions = get_links(user_input)
        print("\nPrinting titles, links, then descriptions\n")
        print(titles+"\n")
        print(links+"\n")
        print(descriptions+"\n")


main()