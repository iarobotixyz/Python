import os, socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
FTP_PORT = 8023
FTP_DIRECTORY = os.getcwd()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 80))
IP = s.getsockname()[0]
s.close()
print(f'\nDIRECCION: FTP://{IP}:{FTP_PORT}')
print(f'DIRECTORIO RAIZ: {FTP_DIRECTORY}\n')
authorizer = DummyAuthorizer()
authorizer.add_anonymous(FTP_DIRECTORY, perm='elradfmw')
handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'Termux FTP Server RoboticaXYZ'
handler.passive_ports = range(50000, 55535)
address = ('', FTP_PORT)
server = FTPServer(address, handler)
server.max_cons = 256
server.max_cons_per_ip = 5
server.serve_forever()

