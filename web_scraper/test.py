# just testing selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *
from bs4 import BeautifulSoup
import os
import time

#
#                   currently fucked, can't get the shit i want
#                       https://selenium-python.readthedocs.io/locating-elements.html
#                       https://github.com/WandSilva/google_images_scraper/blob/master/google_images_scraper.py

browser = webdriver.Chrome(executable_path=os.getcwd()+"\chromedriver.exe")
browser.get("https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q=test&oq=test&gs_l=img")

for i in range(500):
    if i == 250:
        browser.find_element_by_id("smb").clock()
    browser.execute_script("window.scrollBy(0,10000)")

soup = browser.page_source

#soup = BeautifulSoup(soup, "html.parser")

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

print("done! with "+str(len(sources))+" urls")

print("\n\n")
print(sources)
    
            
            


#print(soup)
# for i in soup:
#     for j in i:
#         print("\n\n\n")
#         print(j)
#     break
#soup.find_all(as="image")




# sources = []
# for image in soup.select("img"):
#     print("=")
#     if image['class'][0] == "t0fcAb":
#         sources.append(image['src'])
        

# print(len(sources))
# print("\n\n")
# print(sources)




# print(browser.find_elements_by_tag_name("img"))
# print("ping")
# print(browser.find_elements_by_class_name("rg_i Q4LuWd"))
# print("ping2")
# print(browser.find_elements_by_css_selector("img.rg_i Q4LuWd"))
# print("ping3")
# print(browser.find_elements_by_partial_link_text("https://encrypted"))
# print("ping4")
# print(browser.find_elements_by_xpath("//div[contains(@class,'rg_meta')]"))