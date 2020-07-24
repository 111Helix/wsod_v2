''' 
    Python Web Scraper, still in early stages, started: 27/6/20

    Functions script
'''


from requests import get # https://2.python-requests.org/en/master/user/quickstart/#response-status-codes   
from requests.exceptions import RequestException
from contextlib import closing  # https://docs.python.org/3/library/contextlib.html     brings in the with() statement also, allowing our try.. except.. finally.. stuff to be encapsulated
from bs4 import BeautifulSoup # https://www.crummy.com/software/BeautifulSoup/bs4/doc/  will help with manipulative raw html data
import os
from urllib.request import urlretrieve    # to save photos from url

def get_html(url):      # Gets HTML of url inputted
    try:
        with closing(get(url, stream=True)) as response:        # could just be done without closing(), but it's 'good practice' to use it.  .get simply tries to access that website
            if response.status_code == 200 and response.headers['Content-Type'].lower().find('html') > -1:              # checking if response is HTML
                # response.content is the RAW html, the ugly stuff
                #return BeautifulSoup(response.text, "lxml") #using lxml instead of html.parser amd response.text instead of response.content
                return BeautifulSoup(response.content,"html.parser")
                
            else:
                print("ERROR with format of " + str(url) + " : " + "not html format")   # error message when html isn't in the content type headers
    except RequestException as error:
        print("\nERROR trying to reach " + str(url) + " : " + str(error))     # error message when url can't be reached

def get_links(search_query): # searches input into google and returns 3 lists: titles, links and descriptions, limited only to the first page of google results
    
    google_url = "https://google.com/search?q="+search_query.replace(" ","+")                        # replaces spaces with pluses so that it's in the right format for google urls  AND
    soup = get_html(google_url)                                                                    # appends user_input to url so it google searches
    
   
    ### new approach FROM: https://www.pingshiuanchua.com/blog/post/scraping-search-results-from-google-search

    divided = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    links = []
    titles = []
    descriptions = []

    for i in divided:
        try:
            link = i.find('a', href = True)
            title = i.find('div', attrs={'class':'vvjwJb'}).get_text()
            description = i.find('div', attrs={'class':'s3v9rd'}).get_text()
            
            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '': 
                links.append(link['href'][7:])          # the [7:] just gets rid of '/url?q=' from each link
                titles.append(title)
                descriptions.append(description)
                
        # Next loop if one element is not present
        except:
            continue
    print("no errors getting links it seems.")
    
    return titles, links, descriptions

def save_pics(search_query):           # extract all detected images (or urls of them) from user_input (which is the search query). Returns search query and folder containing image links
    
    imgur_url = "https://www.imgur.com/search?q="+search_query.replace(" ","+")  
    soup = get_html(imgur_url)
    divided = soup.find_all("a",{"class":"image-list-link"})            # divided only contains things within group a

    images = []
    for tag in divided:                                             # looping through each section, only getting those with the img tag
        images.append(tag.find("img"))              
    
    sources = []
    for image in images:                                            # looping through each image
        sources.append("https:"+image['src'][:-5]+".jpg")           # the -5 is to get rid of a b existing at the end of every image link, then I added the .jpg back
    
    print("Found " + str(len(sources))+" links.")
    folder = search_query.replace(" ","_")
    path = str(os.getcwd()) + "\\" + str(folder)
    if os.path.isdir(path) == False:
        os.mkdir(folder)
        print("Creating folder \"folder\"...")
    os.chdir(path)

    print("Saving photos...")
    for files in sources:
        urlretrieve(files,str(files[20:]))                          # saving file, removing the first 20 characters which are all "https://i.imgur.com/"
        print("ding")


    #note: how to os https://appdividend.com/2019/02/06/python-os-module-tutorial-with-example/ https://www.pythonforbeginners.com/os/pythons-os-module/
# e.g.
