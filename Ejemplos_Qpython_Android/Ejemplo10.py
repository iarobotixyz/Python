import os
import tornado.ioloop
import tornado.web
root=os.path.dirname(__file__)
port=8080
ini="index.html"
application=tornado.web.Application([
	(r"/(.*)",tornado.web.StaticFileHandler,
		{"path":root,"default_filename":ini})
])
if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
