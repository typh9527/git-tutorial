#!/usr/bin/python3 
#coding:utf-8 
import upload_task
import socketserver
import time
import os
import subprocess
import mylog

class MyTcpServer(socketserver.BaseRequestHandler):
    def recvfile(self, file_name, user_email):
        directory, filename = os.path.split(file_name)
        filename=str(time.time()).split('.')[0]+filename
        mylog.log("starting reve file!","MyTcpServer.recvfile")
        directory = os.path.join('workpath',user_email)
        if os.path.isdir(directory):
            pass
        else:
            os.makedirs(directory)

        filename=os.path.join(directory,filename)
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True:
            data = self.request.recv(4096)
            if data == 'EOF'.encode():
                mylog.log("recv file success!","MyTcpServer.recvfile")
                break
            f.write(data)
        f.close()
        upload_task.save_task(user_email,filename)
    def sendfile(self, filename):
        mylog.log("starting send file!","MyTcpServer.sendfile")
        self.request.send('ready'.encode())
        time.sleep(1)
        f = open(filename, 'rb')
        while True:
            data = f.read(4096)
            if not data:
                break
            self.request.send(data)
        f.close()
        time.sleep(1)
        self.request.send('EOF'.encode())
        mylog.log("send file success!","MyTcpServer.sendfile")
        #:delete the file
        code = subprocess.call(['rm',filename])
        if code == 0:
            mylog.log("delete zip success","MyTcpServer.sendfile")
        else:
            mylog.log("delete zip failed","MyTcpServer.sendfile")

    def recvtoweb(self, file_name):
        directory, filename = os.path.split(file_name)
        mylog.log("starting reve file!","MyTcpServer.recvtoweb")
        directory = '/var/www/html/'
        if os.path.isdir(directory):
            pass
        else:
            os.makedirs(directory)

        filename=os.path.join(directory,filename)
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True:
            data = self.request.recv(4096)
            if data == 'EOF'.encode():
                mylog("recv file success!","MyTcpServer.recvtoweb")
                break
            f.write(data)
        f.close()

    def handle(self):
        mylog.log("get data","MyTcpServer.handle")
        print("get connection from :",self.client_address)
        while True:
            try:
                data = self.request.recv(4096).decode()
                print("get data:", data)
                if not data:
                    mylog.log("break the connection!","MyTcoServer.handle")
                    break
                else:
                    action,user_email,filename= data.split()
                    if action == "put":
                        self.recvfile(filename,user_email)
                    elif action == 'get':
                        self.sendfile(filename)
                    elif action == 'sendtoweb':
                        self.recvtoweb(filename)
                    else:
                        mylog.error_log("MyTcpServer.handle",action,"msg error")
                        continue
            except Exception as e:
                mylog.error_log("MyTcpServer",str(e),"Exception")


if __name__ == "__main__":
    host = ''
    port = 23336
    s = socketserver.ThreadingTCPServer((host,port), MyTcpServer)
    s.serve_forever()

