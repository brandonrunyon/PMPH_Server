import string
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler

class ReqHandler(BaseHTTPRequestHandler):
    def __init__(self):
        self.__doc__="Class that inherits from BaseHTTPRequestHandler and handles GET and POST methods for HTTP"
        pass
    
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
                    f = open(curdir + sep + self.path, 'rb')
                    self.send_response(200)
                    self.send_header('Content-type',        'image/jpg')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                    return
            #handle gif
            if self.path.endswith(".gif"):
                    f = open(curdir + sep + self.path, 'rb')
                    self.send_response(200)
                    self.send_header('Content-type',        'image/gif')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                    return
            #handle png
            if self.path.endswith(".png"):
                    f = open(curdir + sep + self.path, 'rb')
                    self.send_response(200)
                    self.send_header('Content-type',        'image/png')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                    return
            #handle favicon request
            if self.path.endswith(".ico"):
                    f = open(curdir + sep + self.path, 'rb')
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
