import urllib.request,urllib.parse,urllib.error
import time 
from bs4 import BeautifulSoup
import re
k=open('sensexreult.csv','w')
k.write('company,current market status'+'\n')
print( 'Today sensex shers of company ')
k.close()
c=0
while True:
    k=open('sensexreult.csv','a')
    due=urllib.request.urlopen("https://www.ndtv.com/business/marketdata/domestic-index-bse_sensex")
    soup=BeautifulSoup(due,"html.parser")
    print('Connected to the server wait a while ')
    ss=soup('a')
    print('fetching results')
    for i in ss:
        if re.search('[-0-9.]+[0-9]+%',str(i)):
            s=i.get("title",None)
            if s== None:
                continue
            print(s)
            j=re.findall('[-0-9.]+[0-9]+%',str(i))
            print(j)
            k.write(s+',')
            k.write(j[0]+'\n')
    k.close()
    if c==4:
        break
    c=c+1
    time.sleep(10)
