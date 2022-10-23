#https://iarobotxyz.blogspot.com
import PyPDF2
import androidhelper
def stem_text(text):
    text=text.split()
    temp = [word_list1[0] if i in word_list1 else i for i in text]
    text = ' '.join(temp)
    return text
droid=androidhelper.Android()
dir="scripts3/"
archivo="holy-bible-83800-spa"
pdfFileObj=open(dir+archivo+".pdf", 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
i=pdfReader.numPages
print(i)
contador=2100
while contador < i:
    print("Página Número: "+str(contador)+"\n")
    pageObj=pdfReader.getPage(contador)
    #print(pageObj.extractText())
    #result=droid.ttsSpeak(pageObj.extractText())
    with open(dir+archivo+".txt","a") as obj:
        if pageObj.extractText():
            obj.write("\n"+pageObj.extractText())
    contador+=1
pdfFileObj.close()
