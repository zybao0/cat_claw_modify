#coding=utf-8
import socket
import re
import threading
import base64
import os
import random
import string

def trans(str):
    str=str.replace("%3D","=")
    str=str.replace("%2B","+")
    str=str.replace("%20"," ")
    str=str.replace("%2F","/")
    str=str.replace("%3F","?")
    str=str.replace("%25","%")
    str=str.replace("%26","&")
    str=str.replace("%23","#")
    return str

class WSGIServer(object):
 
    def __init__(self, server_address):
        # 创建一个tcp套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.listen_socket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listen_socket.listen(128)
 
    def serve_forever(self):
        "循环运行web服务器，等待客户端的链接并为客户端服务"
        while True:
            # 等待新客户端到来
            client_socket, client_address = self.listen_socket.accept()
            print("______________client_address______________")
            print(client_address)
            print("______________client_address_finish______________")
            new_process = threading.Thread(target=self.handleRequest, args=(client_socket,))
            new_process.start()
 
            # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
            # client_socket.close()
 
    def handleRequest(self, client_socket):
        "用一个新的进程，为一个客户端进行服务"
        recv_data = client_socket.recv(1024).decode('utf-8')
        client_socket.close()
        url=trans(re.search("down_url=([^&]*)",recv_data).group(1));
        path=trans(re.search("path=([^&]*)",recv_data).group(1));
        print(url)
        print(path)
        url=base64.b64decode(url).decode("utf8","ignore")
        path=base64.b64decode(path).decode("utf8","ignore")
        print(url)
        print(path)
        comm="start ffmpeg -i "+url+" -vcodec copy -acodec copy "+path+"\\"+''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))+".mp4"
        print(comm)
        os.system(comm)

 
 
# 设定服务器的端口
SERVER_ADDR = (HOST, PORT) = "", 8888
# 设置服务器服务静态资源时的路径
# DOCUMENTS_ROOT = "./html"
DOCUMENTS_ROOT = "./"
 
 
def main():
    httpd = WSGIServer(SERVER_ADDR)
    print("web Server: Serving HTTP on port %d ...\n" % PORT)
    httpd.serve_forever()
 
if __name__ == "__main__":
    main()
 