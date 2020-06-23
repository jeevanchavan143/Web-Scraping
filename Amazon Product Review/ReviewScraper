import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd



source=requests.get('https://www.amazon.in/Samsung-Galaxy-10-1-Wi-Fi-Silver/product-reviews/B07SSTH14H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews').content
soup=BeautifulSoup(source,'html.parser')

#print(soup.prettify())

names=soup.find_all('span',class_='a-profile-name')
cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name.pop(0)
cust_name.pop(0)
print(cust_name)

titles=soup.find_all('a',class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
review_title=[]
for i in range(0,len(titles)):
    review_title.append(titles[i].span.get_text())
print(review_title)

ratings=soup.find_all('span',class_='a-icon-alt')
review_rating=[]
for i in range(0,len(ratings)):
    review_rating.append(ratings[i].get_text())

review_rating.pop(0)
review_rating.pop(0)
review_rating.pop(0)
print(review_rating)
review=soup.find_all('span',{"data-hook":"review-body"})
reviews=[]
for i in range(0,len(review)):
    reviews.append(review[i].span.get_text())
print(reviews)

df=pd.DataFrame()

df['Customer Name']=cust_name
df['Rating']=review_rating
df['Headline']=review_title
df['Review']=reviews

print(df)

df.to_csv(r'ReviewData.csv',index=True)
