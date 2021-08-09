from selenium import webdriver 
import chromedriver_binary 
import csv
from bs4 import BeautifulSoup

driver = webdriver.Chrome() 

### open a specific!!! url ###
#url = 'https://www.amazon.com/'
#driver.get(url)



def my_url(keyword):
    keyword = keyword.replace(' ','+')  #spaces must be replaced with plus signs. MAKE SURE there is an actual space between the parentheses
    temp = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss' #the link used to be 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss', but "phone case" was removed to make a generic URL
    return temp.format(keyword)


url = my_url('laptop charger')
#print(url)
driver.get(url) 

################################################################

soup = BeautifulSoup(driver.page_source,'html.parser')


soup_results=soup.find_all('div',{'data-component-type':'s-search-result'}) #after inspecting the page, we found that the 'div' tag with the 'data-component...' has the data needed
#print(len(soup_results))

obj=soup_results[0] # first result set to obj
atag = obj.h2.a # h2 variable has been made
des = atag.text.strip()
#print(des)  ----  the description (product's name) should be shown 



url0='https://www.amazon.com'+atag.get('href')
