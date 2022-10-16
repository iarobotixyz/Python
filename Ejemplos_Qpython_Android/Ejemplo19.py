import urllib.request
from bs4 import BeautifulSoup
import wget
url='https://roboticaxyz.com/'
x=urllib.request.urlopen(url)
soup=BeautifulSoup(x.read(), 'html.parser')
dir="scripts3/"
archivo="imagenes.txt"
all_imgs=soup.find_all('img', src=True)
with open(dir+archivo,"w") as obj:
    for image in all_imgs:
        print (image['src']+"\n")
        obj.write("\n"+str(image['src']))
        filename=wget.download(str(image['src']))
        print(filename)