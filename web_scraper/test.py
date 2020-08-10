# just testing selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *
import os
import time

#
#                   currently fucked, can't get the shit i want
#                       https://selenium-python.readthedocs.io/locating-elements.html
#                       https://github.com/WandSilva/google_images_scraper/blob/master/google_images_scraper.py

browser = webdriver.Chrome(executable_path=os.getcwd()+"\chromedriver.exe")
browser.get("https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q=test&oq=test&gs_l=img")

html = browser.page_source
print(html)
f = open("fuck.txt","x",encoding="utf-8")
f.write(html)
f.close()
time.sleep(6)
browser.execute_script("window.scrollBy(0,10000)")
soup = browser.page_source
f = open("shit.txt","x",encoding="utf-8")
f.write(soup)
f.close()


print(soup)
print(html == soup)
print(html > soup)
print(html >= soup)
print(html is soup)

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