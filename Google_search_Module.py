import re
import urllib.request,urllib.parse,urllib.error
from googlesearch import search
from bs4 import BeautifulSoup
import Regular_Expression as h
import Tag_and_URL_Process
x=True
if x==True:
    csv=open('hoteldetails.csv','w')
    csv.write('hotel name,phone,email,link'+'\n')
    csv.close()
    k=open('urlresults.doc','w')
    d=input("enter your required search like hotel details ")
    print('i am seaching for google results')
    for url in search(d, tld='es', lang='es', stop=10):
    #print(url)
        k.write(url+'\n')
    k.close()
    k=open('urlresults.doc','r')
    print("Now i am opening each and every link")
    for i in k:
        Tag_and_URL_Process.open1(i)
        print('successfully compleated ')
    k.close()
else:
    import Sample_RPA_Apllication
        
