import requests #to make requests to the required page
import bs4 #contains BS for pulling data out of HTML and XML files 
import pandas as pd #to convert our data to a dataframe 



##############################################################################################




ourdata = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
#print(ourdata.text)  ----  used to check the data extracted using requests 



bsp = bs4.BeautifulSoup(ourdata.text,'xml') # parsing data. the 'xml' at the end specifies the format we want
#print(bsp)  -----  again, used to check what it extracted



titles = bsp.select('title') # selects the 'title' tax part of the whole code and extracts it
#print(titles) 



notaxtitle = titles[0].getText() #removes tax
#print(notaxtitle) 
### OR you can just print it without setting any variables ###
#print(titles[0].getText()) 



title_class = bsp.select('h2') #selects the 'h2' tax part of the whole code. try replacing with '.mw-headline'
#print(title_class)

### extracting the text out of 'title_class' ###
#for i in title_class:
    #print(i.text)  

#print(title_class[5].getText())  ----  try putting different numbers in the brackets. "count from zero!!!"



#print(bsp.select('h3 > span'))  ----  try this and find out what it does



#print(bsp.select('link'))  ----  extracts all 'link' tags

#print(bsp.select('img'))  ----  extracts all 'img' tags




##############################################################################################




import wikipedia #after installing wikipedia library 
from pprint import pprint #apparently makes things more readable




#print(wikipedia.search('south park'))  ----  gives you pages related to your search 

southpark = wikipedia.page(wikipedia.search('south park')[0])
#print(southpark) 
#print(dir(southpark))  ----  shows you what kind of info they can provide
#print(southpark.summary)  ----  "summary" can be replaced with "title", "url" etc. 
#print(southpark.content)  ----  shows just about everything on the page
#print(southpark.images)  ----  extracts all images
#print(southpark.url)  ----  gives you the url of the page
