import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import search1 as h
def open1(link):
    url = link
    l1=[]
    l={}
    soup=False
    try :
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
    except:
        print('wait some time')
    if soup==False:
        print("Sorry ")
    else:
        #tags = soup('div')
        tags=soup('a')
        if tags!=None:
            for tag in tags:
                if re.search('property_title',str(tag)):
                    t=tag.get('href')
                    #print(t)
                    if 'http'not in t:
                        if '.in' in link:
                            s=link.split('.in')[0]+'.in'+t
                    else:
                        s=t
                    h.searchre(s)
                   # print('result is uploaded in exel')
'''                elif re.search('data-page',str(tag)):
                    t=tag.get('href')
                    #print(t)
                    if 'http'not in t:
                        if '.in' in link:
                            s=link.split('.in')[0]+'.in'+t
                    else:
                        s=t
                        open1(s)
                    #print('result is uploaded in exel')
               else:
                    for i in tags:
                        if i.get('class')==None:
                            continue
                        if len(i.get('class'))==1:
                            l1.append(i.get('class')[0])
                    for i in l1:
                        l[i]=l.get(i,0)+1
                    maxi=0
                    for i in l:
                        if l[i]>maxi:
                            maxi=l[i]
                            key=i
                    if re.search(key,str(tag)):
                        t=tag.get('href')
                    #print(t)
                        if 'http'not in t:
                            if '.in' in link:
                                s=link.split('.in')[0]+'.in'+t
                            elif '.com' in link:
                                s=link.split('.com')[0]+'.com'+t
                        else:
                            s=t
                        h.searchre(s)   
                
    #for tag in tgs '''
    
