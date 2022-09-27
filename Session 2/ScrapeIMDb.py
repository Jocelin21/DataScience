from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://www.imdb.com/list/ls574761151/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

title = soup.select('h3.lister-item-header a')

year= soup.find_all('span',class_='lister-item-year text-muted unbold')

rating = soup.find_all('span',class_='ipl-rating-star__rating')

total_votes = soup.find_all('span',attrs={'name':'nv'})
votes=[]
for i in total_votes:
    votes.append(i.get_text())

desc = soup.find_all('p')

text=[]
x=0
for i in desc:
    if ((x+2) % 4 == 0):
        text.append(i.get_text())
    x+=1

runtime= soup.find_all('span',class_='runtime')

genre= soup.find_all('span',class_='genre')

cert= soup.find_all('span',class_='certificate')
#print(cert[0].get_text())

df=pd.DataFrame(list(zip(title,year,rating,votes,text,runtime,genre,cert)), columns=['Title','Airdate','Rating','Votes','Description','Runtime','Genre','Certificate'])
print(df.head())

df.to_csv('IMDbData.csv', index=False, encoding= 'utf-8')
