import wget
url='https://iarobotxyz.blogspot.com/'
archivo='index.html'
filename=wget.download(url+archivo)
print(filename)
