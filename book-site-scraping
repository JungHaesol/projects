import requests #to make requests to the required page
import bs4 #contains BS for pulling data out of HTML and XML files 
import pandas as pd #to convert our data to a dataframe 


#####################################################################


pages = []
prices = []
ratings = []
title = []
urls = [] 



no_of_pages = 5 #number of pages to be selected 

### looping through the required pages and selecting the pages accordingly
for i in range(1,no_of_pages+1): #to include the last page
    url=('http://books.toscrape.com/catalogue/page-{}.html'.format(i))
    pages.append(url)

#print('Number of pages:', len(pages)) 
#print(pages) 



for item in pages:
    page=requests.get(item)
    soup=bs4.BeautifulSoup(page.text,'html.parser')

#print(soup)  ----  OUTPUT LOOKS UGLY 
#print(soup.prettify())  ----  OUTPUT IS MORE ORGANISED 



### the titles (the titles have h3 tags) ###
for t in soup.findAll('h3'):
    titless=t.getText() 
    title.append(titless)  # now the title list is filled
    #print(titless) 

#print(title) 



### the prices ###
for p in soup.find_all('p',class_='price_color'):
    price = p.getText()
    prices.append(price)  # now the prices list is filled
    ###print(price) 

#print(prices)  



### the ratings ###
for s in soup.find_all('p',class_='star-rating'):
    for k,v in s.attrs.items(): #to read about attr: https://www.attrs.org/en/stable/, k will contain the class(u can print(k) to see what is inside, V is going to contain a list like ['star-rating', 'Two'], we use v[1] to get the second item which is the actual ratings)
        star=v[1]
        ratings.append(star)  # now the ratings list is filled
        #print(star) 

#print(ratings) 



### image urls ###
divs=soup.find_all('div',class_='image_container') #getting all the 'div' tags in the class 'image_container'
#print(divs)
for thumbs in divs:
    tagss=thumbs.find('img',class_='thumbnail')
    #print(taggs)
    links='http://books.toscrape.com/' + str(tagss['src'])
    newlinks = links.replace('..','') #gets rid of '..', makes links more readable
    urls.append(newlinks) # now the urls list is filled

#print(urls)  



