from selenium import webdriver 
import chromedriver_binary 
import csv

driver = webdriver.Chrome() 

### open a specific!!! url ###
url = 'https://www.amazon.com/'
driver.get(url)



def my_url(keyword):
    keyword = keyword.replace(' ','+')  #spaces must be replaced with plus signs. MAKE SURE there is an actual space between the parentheses
    temp = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss' #the link used to be 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss', but "phone case" was removed to make a generic URL
    return temp.format(keyword)


url = my_url('laptop charger')
#print(url)
driver.get(url) 



