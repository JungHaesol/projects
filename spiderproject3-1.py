# 정해솔 

from selenium import webdriver 
import chromedriver_binary 
import csv
from bs4 import BeautifulSoup

driver = webdriver.Chrome() 

### open a specific!!! url ###
### 특정한 URL 열기 ###
#url = 'https://www.amazon.com/'
#driver.get(url)



def my_url(keyword):
    keyword = keyword.replace(' ','+')  #spaces must be replaced with plus signs. 
    #공백은 덧셈으로 교체해야 한댜.
    temp = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss' #the link used to be 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss', but "phone case" was removed to make a generic URL
    # 원래 링크가 'https://www.amazon.com/s?k=phone+case&ref=nb_sb_noss'였지만, "phone case"가 제거되었다. "함수다운" URL을 만들기 위해서이다.  
    return temp.format(keyword)


url = my_url('laptop charger')
#print(url)
driver.get(url) 

################################################################

soup = BeautifulSoup(driver.page_source,'html.parser')


soup_results=soup.find_all('div',{'data-component-type':'s-search-result'}) # after inspecting the page, we found that the 'div' tag with the 'data-component...' has the data needed
# 웹페이지를 검사하고 'data-component...'와 함께 있는 'div' 태그가 필요한 정보를 가지고 있음을 알 수 있었다 
#print(len(soup_results))

obj=soup_results[0] # first result set to obj
# 첫번째 결과를 obj라고 한다
atag = obj.h2.a # h2 variable has been made
# h2 변수가 생성되었다 
des = atag.text.strip()
#print(des)  ----  the description (product's name) should be shown ---- 설명(구매




url0='https://www.amazon.com'+atag.get('href')
