#https://iarobotxyz.blogspot.com/2022/10/haz-que-tu-telefono-te-lea-un-pdf-con.html?github=1
import PyPDF2
import androidhelper
droid=androidhelper.Android()
dir="scripts3/"
archivo="IDR_289_EyO.pdf"
pdfFileObj=open(dir+archivo, 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
i=pdfReader.numPages
print(i)
contador=0
while contador < i:
    print("Página Número: "+str(contador)+"\n")
    pageObj=pdfReader.getPage(contador)
    print(pageObj.extractText())
    result=droid.ttsSpeak(pageObj.extractText())
    contador+=1
pdfFileObj.close()
