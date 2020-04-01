#!coding:utf8
from http.server import HTTPServer,CGIHTTPRequestHandler
# from CGIHTTPServer import CGIHTTPRequestHandler
 
port=8888
 
httpd=HTTPServer(('',port),CGIHTTPRequestHandler)
print("Starting simple_http on port:"+str(httpd.server_port))
httpd.serve_forever()