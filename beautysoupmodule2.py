from bs4 import BeautifulSoup
import pandas as pd
import requests as rq
url="https://inshorts.com/en/read"
dat=rq.get(url)
soup=BeautifulSoup(dat.content,'lxml')
data=soup.find('div',attrs={'class':'container'})
headlines=[]
news=[]
for row in soup.findAll('div',attrs={'class':'news-card z-depth-1'}):
    print("Topic- ",row.find('span',attrs={'itemprop':'headline'}).text,"\n")
    print("News- ",row.find('div',attrs={'itemprop':'articleBody'}),"\n")
    print("----------------------------------------------------------------------\n")
    headlines.append(row.find('span',attrs={'itemprop':'headline'}).text)
    news.append(row.find('div',attrs={'itemprop':'articleBody'}).text)

for child in soup.children:
    print(child.find(''))

#d={'headlines':headlines,'news':news}
#df=pd.DataFrame(d)
#df.to_csv('news.csv',index=False)




