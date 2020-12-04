from bs4 import BeautifulSoup
import urllib.request 
import requests

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
head2 = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')} 
url = 'https://datalab.naver.com/keyword/realtimeList.naver'
#res = urllib.request.Request(url,headers=head)
#response = urlopen('https://www.naver.com')
#response = urlopen(url)
#req = urllib.request.Request(url,headers=head)
#response = urllib.request.urlopen(req).read()
res = requests.get(url,headers = head2)
soup = BeautifulSoup(res.content,'html.parser')
data = soup.select('span.item_title')
#print(soup)
for item in data:
    print(item.get_text())

#for anchor in soup.select("span.keyword"):
#   print(anchor)
#i=1
#f=open("to.txt",'w')
#for anchor in soup.select("span.keyword"):
#    print(anchor)
    #data = str(i) + "위: " + anchor.get_text()
    #i=i+1
    #f.write(data)
#f.close()