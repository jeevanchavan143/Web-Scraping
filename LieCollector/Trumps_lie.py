import requests
from bs4 import BeautifulSoup
import pandas as pd
source=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
print(source.status_code)

soup=BeautifulSoup(source.text,'lxml')
#print(soup.prettify())
results=soup.find_all('span',attrs={'class':'short-desc'})

records=[]
for result in results:
    date=result.find('strong').text[0:-1]+ ', 2017'
    lie=result.contents[1][1:-2]
    explaination=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,explaination,url))
#print(records)

df=pd.DataFrame(records,columns=['date','lie','explaination','url'])
df['date']=pd.to_datetime(df['date'])
df.to_csv('trump_lies.csv',index=False,encoding='utf-8')
