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
from selenium import webdriver                      # to open a browser on its own
from selenium.webdriver.common.keys import Keys     # to scroll for more images
from selenium import *

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

def imgur_save_pics(search_query):           # extract all detected images (or urls of them) from user_input (which is the search query). Returns search query and folder containing image links
    
    imgur_url = "https://www.imgur.com/search?q="+search_query.replace(" ","+")  
    soup = get_html(imgur_url)
    divided = soup.find_all("a",{"class":"image-list-link"})            # divided only contains things within group a with the class name "image-list-link", thank you imgur for naming your class that

    images = []
    for tag in divided:                                             # looping through each section, only getting those with the img tag
        images.append(tag.find("img"))              
    
    sources = []
    for image in images:                                            # looping through each image
        sources.append("https:"+image['src'][:-5]+".jpg")           # the -5 is to get rid of a b existing at the end of every image link, then I added the .jpg back
    
    if sources == []:
        print("\nError!, no sources detected\n")
        return

    print("Found " + str(len(sources))+" links.")
    folder = "imgur_"+search_query.replace(" ","_")
    path = str(os.getcwd()) + "\\" + str(folder)
    if os.path.isdir(path) == False:
        os.mkdir(folder)
        print("Creating folder \"folder\"...")
    os.chdir(path)

    print("Saving photos...")
    for files in sources:
        urlretrieve(files,str(files[20:]))                          # saving file, removing the first 20 characters which are all "https://i.imgur.com/"
    
    print("done!")

def google_save_pics_small(search_query):     # extract all detected images (or urls of them) from user_input (which is the search query). Returns search query and folder containing image links

    google_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img".format(query = search_query.replace(" ","+"))
    soup = get_html(google_url)
    sources = []

    for image in soup.select("img"):
        if image['class'][0] == "t0fcAb":
            sources.append(image['src'])
    
    if sources == []:
        print("\nError!, no sources detected\n")
        return
    
    print("Found " + str(len(sources))+" links.")
    folder = "google_small_"+search_query.replace(" ","_")
    path = str(os.getcwd()) + "\\" + str(folder)
    if os.path.isdir(path) == False:
        os.mkdir(folder)
        print("Creating folder \"folder\"...")
    os.chdir(path)

    print("Saving photos...")
    for files in sources:
        urlretrieve(files,str(files[54:]+".jpg"))                          # saving file, removing the first 54 characters which are all "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9Gc"
        
    print("Done!")

def google_save_pics_big(search_query):
    browser = webdriver.Chrome(executable_path=os.getcwd()+"\chromedriver.exe")
    browser.get("https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img".format(query = search_query.replace(" ","+")))

    for i in range(1000):
        browser.execute_script("window.scrollBy(0,10000)")
    soup = browser.page_source
    browser.quit()

    sources = []
    all_cleared = False
    while all_cleared == False:
        start_index = soup.find("https://encrypted-tbn0.gstatic.com/images?q=tbn")      # finds index of string containing this substring
        print(str(start_index))
        if start_index == -1:
            break
        end_of_string = False
        jump_index = 1
        while end_of_string == False:                                               # loop to find the rest of the url

            #print(soup[start_index+jump_index])
            if soup[start_index+jump_index] == ";":
                sources.append(soup[start_index:start_index+jump_index])            # add the link to sources
                end_of_string = True
                soup = soup[start_index+jump_index:]            # cuts the string so it's only the contents following the link
                #print(len(sources))
            else:
                jump_index += 1
    
    
    print("Found " + str(len(sources))+" links.")
    folder = "google_big_"+search_query.replace(" ","_")
    path = str(os.getcwd()) + "\\" + str(folder)
    if os.path.isdir(path) == False:
        os.mkdir(folder)
        print("Creating folder \"folder\"...")
    os.chdir(path)

    print("Saving photos...")
    for files in sources:
        urlretrieve(files,str(files[54:]+".jpg"))