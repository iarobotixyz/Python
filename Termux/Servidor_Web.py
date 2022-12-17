#qpy:webapp: Servidor Web Python
#qpy://127.0.0.1:8080/

from bottle import Bottle, ServerAdapter
from bottle import run, debug, route, error, static_file, template

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

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/sdcard')


######### WEBAPP ##############
@route('/')
def home():
    return template('<center><h1>Hola Mundo Web con {{name}} !</h1>'
    	'<a href="#3456">Ver código</a><br /><p> '
    	'Bienvenido al mundo HTML<p>'
    	'<a href="#roboticaxyz">>> Ejemplo link</a>',name='Python')

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

