# 정해솔 

# 해외의 온라인 매장인 아마존을 스크래핑해볼 것이다. 아마존은 위키백과, 모의 스크래핑을 위한 온라인 서점 사이트와는 다르게 오로지 requests와 
# BeautifulSoup로만 스크래핑이 안된다. 따라서 Selenium과 구글 크롬의 웹 드라이버를 이용하여 정보를 가져오고 특정한 창을 열어보는 연습을 
# 할 것이다. 


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
