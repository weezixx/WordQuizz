from bs4 import BeautifulSoup
import urllib
import socket
import time

start_time = time.time()

#url = " https://app.memrise.com/course/391903/5000-most-used-dutch-words/1/ "

url_source = " https://app.memrise.com/course/391903/5000-most-used-dutch-words/"

data = open("memrise.txt","w")

k = 0

for i in range(1,273,1):

  url = url_source + str(i)

  f = urllib.request.urlopen(url)

  html = f.read()

  soup = BeautifulSoup(html)

  div = soup.find('div', class_='things clearfix')

  for item in div.select("div.text"):

    data.write(item.get_text()+"\n")
    k+=1

print(k)

print("--- %s seconds ---" % (time.time() - start_time))