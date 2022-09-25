import urllib.request
from bs4 import BeautifulSoup
url='https://iarobotxyz.blogspot.com/'
x=urllib.request.urlopen(url)
soup=BeautifulSoup(x.read(), 'html.parser')
dir="scripts3/"
archivo="links.txt"
for a in soup.find_all('a', href=True):
    print (a['href'])
    with open(dir+archivo,"a") as obj:
        obj.write("\n"+a['href'])
