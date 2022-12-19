#qpy:webapp: Análisis de WhatsApp con Python
#qpy://127.0.0.1:8080/
from bottle import Bottle, ServerAdapter
from bottle import run, debug, route, error, static_file, template
####Analis de WhatsApp #########
dir="scripts3/"
archivo="Chat de WhatsApp con Berenice Col.txt"
#########RoboticaXYZ############
word_list1=["",'el','la','los','las','un','una','unos',
'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 
'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 
'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya',
 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 
 'son', 'solo', 'tengo', 'muy']
def stem_text(text):
    text = text.split()
    temp = [word_list1[0] if i in word_list1 else i for i in text]
    text = ' '.join(temp)
    return text
with open(dir+archivo) as f:
    lin=f.readlines()
    save=lin
    lin=str(lin).replace ("\\n", "")
    lin=str(lin).replace ("'", "")
    lin=str(lin).replace (",", "")
    lin=str(lin).replace (".", "")
    lin=str(lin).replace ("[", "")
    lin=str(lin).replace ("]", "")
    print(lin)
    lin=lin.lower()
    lin=stem_text(lin)
    print(lin)
save =str(save)
cadPa =str(lin)
######### SERVIDOR WEB PYTHON ###############
class MyWSGIRefServer(ServerAdapter):
    server = None
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        import threading
        threading.Thread(target=self.server.shutdown).start()
        self.server.server_close()
######### BUILT-IN ROUTERS ###############
@route('/__exit', method=['GET','HEAD'])
def __exit():
    global server
    server.stop()

@route('<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/sdcard')
######### WEBAPP WhatsApp##############
@route('/')
def home():
    head='<center><h1>Análisis de conversaciónes de '
    head+='WhatsApp con {{name}}!</h1><table border="1">'
    head+='<tr><td width="100%" bgcolor="green"><h1>'
    head+='Servidor Web localhost:8080</h1></td></tr></table>'
    head+='<hr><h1>Conversación Original:</h1><p>'+save
    head+='<hr><h1>'
    resultado=head+'Conversación Resumido:</h1><p>'+cadPa
    listPa = cadPa.split()
    frePalab = []
    orden=[]
    for i in listPa:
        frePalab.append(listPa.count(i))
    orden=str(list(zip(listPa, frePalab)))
    anal=orden
    resultado+='<hr><h1>Conteo de palabras:</h1><p>'+orden
    sepa=str('\n'.join(map(str, orden)))
    #sep=str('<br>'.join(map(str, orden)))
    resultado+='<hr><h1>Orden de palabras:</h1><p>'+sepa
    resultado+='<hr>Separado<p>---'
    return template(resultado+' <p>'
    	'<a href="RoboticaXYZ.com">RoboticaXYZ.com</a><br /><p> '
    	'Bienvenido al mundo HTML<p>'
    	'<a href="/'+'">>> Ejemplo RoboticaXYZ.com/WhatsApp/</a>',name='Python')
######### WEBAPP ROUTERS ###############
app = Bottle()
app.route('/', method='GET')(home)
app.route('/__exit', method=['GET','HEAD'])(__exit)
app.route('/assets/<filepath:path>', method='GET')(server_static)
try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8080")
    app.run(server=server,reloader=False)
except Exception as ex:
    errs = "Exception: %s" % repr(ex)
    print(errs)
#-*-coding:utf8;-*-
#qpy:console
