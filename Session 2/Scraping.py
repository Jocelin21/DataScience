from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://www.imdb.com/list/ls574761151/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

movies = soup.select('h3.lister-item-header a')
print(movies[0].get_text())

title = [t.get_text() for t in soup.select('h3.lister-item-header a')]
print(title[1])

links = soup.select('h3.lister-item-header a')
print(links[0].get_text())

#links = [a.attrs.get('href') for a in soup.select('h3.lister-item-header a')]

links=[]
for a in soup.select('h3.lister-item-header a'):
  links.append(a.attrs.get('href'))

print(links[0].get_text())

ratings = soup.select('h3.lister-item-header a')
print(ratings[0].get_text())
vote = [a.attrs.get('title') for a in soup.select('h3.lister-item-header a')]
print(vote[0].get_text())


#apply regex searchon first record

match_s=re.search("on",vote[0])
match_e=re.search("user",vote[0])
vote = vote[0][match_s.end() :match_e.start()] #slicing
print(vote.strip()) #clean white space

list = []
 
# Iterating over movies to extract
# each movie's details
for i in range(len(soup.select('h3.lister-item-header a'))):

    rank=soup.select('h3.lister-item-header a')[i].get_text()
    # clean the rank data, we just want the first digit before ".", and remove all white space
    rank=rank[0:rank.find('.')].strip()

    movie_title=soup.select('h3.lister-item-header a')[i].string
    year=soup.find_all('span', class_='lister-item-year')
    #clean the year data, remove "(" and ")"
    # year=year.replace('(',"").replace(')',"")
    print(year[0])

    crew=soup.select('h3.lister-item-header a')[i].attrs.get('title')

    rating=soup.select('h3.lister-item-header a')[i].get_text()
    vote=soup.select('h3.lister-item-header a')[i].attrs.get('title')
    #cleaning the votes data
    match_s=re.search("on",vote)
    match_e=re.search("user",vote)
    vote = vote[ match_s.end() :match_e.start()].strip()

    link=soup.select('h3.lister-item-header a')[i].attrs.get('href')
    #add the domain name
    link="https://www.imdb.com" + link

    data = {"rank":rank,
            "movie_title": title,
            "year": year,
            "crew": crew,
            "rating": rating,
            "link": link,
            "votes": vote}
    list.append(data)

df = pd.DataFrame(list, columns = ['rank', 'movie_title', 'year', 'crew', 'rating', 'link', 'votes'])
# print(list[0])
# print (df.head())

df.to_csv('250movie.csv', index=False)

