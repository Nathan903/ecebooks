import http.server
import socketserver
from os.path import exists
import os
subfolders = [ f.path for f in os.scandir(".") if f.is_dir() ]
s=""
for i in subfolders:
    i=i[2:]
    s+=(f'<a href="{i}/index.html">{i}</a><br>')
indexfname = "aaa.html"
with open(indexfname, "w") as f:
    f.write(s)
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        syspath = self.path[1:]
        if self.path == '/':
            self.path = 'index.html'
        if self.path == '/en/':
            self.path = 'en/index.html'
        elif (not '.' in self.path):
            if self.path[-1] =="/":
                if exists(syspath+"index.html"):
                    self.path +="index.html"#= self.path[0:-1]+'.html'
                if exists(syspath[0:-1]+'.html'):
                    self.path= self.path[0:-1]+'.html'
            else:
                if exists(syspath+".html"):
                    self.path+='.html'
                if exists(syspath+"/index.html"):
                    self.path +="/index.html"
        print(self.path)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 322
my_server = socketserver.TCPServer(("", PORT), handler_object)
print(1)
# Star the server
import webbrowser
webbrowser.open("http://localhost:"+str(PORT)+"/"+indexfname)
my_server.serve_forever()

