from WebServer import *
from ReqHandler import *
from string import *

class Run():

    def __init__(self):
            self.__doc__="object to run the server"
            pass
    
    def control(self):
        host = '0.0.0.0'
        port = 80
        server_address = (host, port)
        server_class = WebServer()
        handler_class = ReqHandler()
        try:
            httpd = server_class.start(server_address, handler_class)
            start_msg = 'Httpd started, listening on port: ' + str(port)
            print start_msg
            print "Ctrl+c to stop service"
            httpd.serve_forever()
                
        except KeyboardInterrupt:
            print 'Httpd Stopped!'
            httpd.socket.close()
        return self
        pass
