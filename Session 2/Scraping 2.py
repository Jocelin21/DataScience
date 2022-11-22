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
#print(rating[0].get_text())

total_votes = soup.find_all('span',attrs={'name':'nv'})
votes=[]
for i in total_votes:
    votes.append(i.get_text())

desc = soup.find_all('p')
print(desc[0].get_text())


df=pd.DataFrame(list(zip(title,year,rating,votes)), columns=['Title','Airdate','Rating','Votes'])
#print(df.head())

# list=[]
# for i in range(len(soup.select('h3.lister-item-header a'))):
#     response = requests.get(url,headers=headers)
#     soup = BeautifulSoup(response.content,'html.parser')

#     movies = soup.select('h3.lister-item-header a')
#     # print(movies[0].get_text())

#     year= soup.find_all('span',class_='lister-item-year text-muted unbold')
#     # print(year[0].get_text())
    
#     #add the domain name
#     # link="https://www.imdb.com" + link

#     data = {"movie_title": movies,
#             "year": year,
#             }
#     list.append(data)

# df = pd.DataFrame(list, columns = ['movie_title', 'year'])

# movie_title.append(movies.text)
# years.append(year.text)
# ratings.append(rating.text)
# votes.append(total_votes.text)
# desc.append(total_votes.text)

# df = pd.DataFrame(list(zip(episode_number, movie_title, years, ratings, total_votes, desc)), 
#     columns =['Episode Number', 'Movies', 'Year', 'Rating', 'Total Votes', 'Description'])