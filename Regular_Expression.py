import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
def searchre(t):
    csv=open('hoteldetails.csv','a')
    html = urllib.request.urlopen(t).read()
    soup = BeautifulSoup(html, 'html.parser')
    k=[]
    l=[]
    tags=soup('h1')
    c=0
    for i in tags :
        z=re.findall('>([A-za-z -,0-9]+)<',str(i))
        c=0
        if len(z)!=0:
            print(z[0])
            c=c+1
            csv.write(z[0])
            break
        #csv.write(',')
        else:pass
    if c>0:
        csv.write(',')
        for line in soup:
        #x = re.findall('[<>/+]+([+0-9()-]+[0-9()]+)', str(line))
            x = re.findall('[CONTACTcontactNUMBERnumberoTELtelPHONEphone:+-][CONTACTcontactNUMBERnumberoTELtelPHONEphone:+-][CONTACTcontactNUMBERnumberoTELtelPHONEphone:+-]+([03-9:(-)+][0-9:(-)+]+)', str(line))
            y = re.findall('[a-zA-Z0-9]+@+[a-zA-Z0-9]+[.][a-zA-Z0-9]+', str(line))
            if len(x) > 0:
                for i in x:
                    if len(i) > 8:
                    #print(i)
                        if i not in k:
                            k.append(i)
            for i in y:
                if len(i) > 6:
                #print(i)
                    if i not in l:
                        l.append(i)
    
        for i in k:
            print(i)
            csv.write(i+';')
        csv.write(',')
        for i in l:
            print(i)
            csv.write(i+';')
        csv.write(',')
        #csv.write(t+',')
        csv.write('\n')
    
        csv.close()
