import string,cgi,socket
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def get_Server_IP(hostname='default'):
        if hostname=='default':
                hostname=socket.gethostname()
                ips=socket.gethostbyname_ex(hostname)[2]
                return [i for i in ips if i.split('.')[0]!='127'][0]

class MyHandler(BaseHTTPRequestHandler):

        def do_GET(self):
                try:
                        #for html files
                        if self.path.endswith(".html")|self.path.endswith(".htm")|self.path.endswith(".shtml"):
                                f = open(curdir + sep + self.path)
                                self.send_response(200)
                                self.send_header('Content-type',        'text/html')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #got to have GET handler for css resources
                        if self.path.endswith(".css"):
                                f = open(curdir + sep + self.path)
                                self.send_response(200)
                                self.send_header('Content-type',        'text/css')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle javascript requests
                        if self.path.endswith(".js"):
                                f = open(curdir + sep + self.path)
                                self.send_response(200)
                                self.send_header('Content-type',        'text/javascript')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle xml
                        if self.path.endswith(".xml"):
                                f=open(curdir + sep + self.path)
                                self.send_response(200)
                                self.send_header('Content-type',        'text/xml')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle jpg formats
                        if self.path.endswith(".jpg")|self.path.endswith(".jpeg"):
                                f=open(curdir + sep + self.path, 'rb')
                                self.send_response(200)
                                self.send_header('Content-type',        'image/jpg')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle gif
                        if self.path.endswith(".gif"):
                                f=open(curdir + sep + self.path, 'rb')
                                self.send_response(200)
                                self.send_header('Content-type',        'image/gif')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle png
                        if self.path.endswith(".png"):
                                f=open(curdir + sep + self.path, 'rb')
                                self.send_response(200)
                                self.send_header('Content-type',        'image/png')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle favicon request
                        if self.path.endswith(".ico"):
                                f=open(curdir + sep + self.path, 'rb')
                                self.send_response(200)
                                self.send_header('Content-type',        'image/x-icon')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        #handle request when no file is specified for a directory, if index is present, use it
                        if self.path.endswith("/"):
                                f = open(curdir + sep + self.path + "index.html")
                                self.send_response(200)
                                self.send_header('Content-type',        'text/html')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return
                        return
                #error exeption handling for logging and interactive monitoring, needs to work in do_POST()
                except IOError:
                        self.send_error(404, '<h1>404 dude!</h1><br>File Not Found: %s' % self.path)
                        self.send_header('Content-type',        'text/html')
                        self.end_headers()
                        self.wfile.write('<html><body><h1>404 dude!</h1><br>File Not Found: %s</body></html>' % self.path)
                        
                        
ip = get_Server_IP()#we would like to know for reference what the address of the machine it's running on
host = '0.0.0.0' #open to any device for testing, for local only, use loopback address
port = 80 #standard http port, change for development environment, not safe to use on 80 or 8080

server_class = HTTPServer
handler_class = MyHandler
server_address = (host, port)

def main():
        try:
                httpd = server_class(server_address, handler_class)
                start_msg = 'Httpd started, listening on port: ' + str(port)
                ip_msg ='Server ip: '+ ip +' ...'
                print start_msg
                print ip_msg
                print "Ctrl+c to stop service"
                httpd.serve_forever()
                
        except KeyboardInterrupt:
                print 'Httpd Stopped!'
                httpd.socket.close()

if __name__=='__main__':
        main()





            

	
