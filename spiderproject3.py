# 정해솔 

from selenium import webdriver 
import chromedriver_binary 
import csv

driver = webdriver.Chrome() 

### open a specific!!! url ###
### 특정한 URL 열기 ###
url = 'https://www.amazon.com/'
driver.get(url)



def my_url(keyword):
    keyword = keyword.replace(' ','+')  #spaces must be replaced with plus signs. 
    #공백은 덧셈으로 교체해야 한댜.
    temp = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss' #the link used to be 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss', but "phone case" was removed to make a generic URL
    # 원래 링크가 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss'였지만, "phone case"가 제거되었다. "함수다운" URL을 만들기 위해서이다.  
    return temp.format(keyword)


url = my_url('laptop charger')
#print(url)
driver.get(url) 
