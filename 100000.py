from bs4 import BeautifulSoup
import urllib
import socket
import time

start_time = time.time()

#url = " https://app.memrise.com/course/391903/5000-most-used-dutch-words/1/ "

url_source = " https://app.memrise.com/course/391903/5000-most-used-dutch-words/"

data = open("neerlandais.txt","w")

data2 = open("anglais.txt","w")

k = 1

target = 1

target_2 = 4

#273 car 273 pages url
for i in range(1,273,1):

  url = url_source + str(i)

  f = urllib.request.urlopen(url)

  html = f.read()

  soup = BeautifulSoup(html)

  div = soup.find('div', class_='things clearfix')

  for item in div.select("div.text"):

    if k == target:
      data.write(item.get_text()+"\n")
      target += 4

    if k == target_2:
      data2.write(item.get_text()+"\n")
      target_2 += 4
    k +=1




print("--- %s seconds ---" % (time.time() - start_time))