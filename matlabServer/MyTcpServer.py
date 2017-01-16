#!/usr/bin/python3 
#coding:utf-8 
import upload_task
import socketserver
import time
import os

class MyTcpServer(socketserver.BaseRequestHandler):
    def recvfile(self, file_name, user_email):
        directory, filename = os.path.split(file_name)
        filename=str(time.time()).split('.')[0]+filename
        print("starting reve file!")
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
                print("recv file success!")
                break
            f.write(data)
        f.close()
        upload_task.save_task(user_email,filename)
    def sendfile(self, filename):
        print("starting send file!")
        self.request.send('ready'.encode())
        time.sleep(1)
        f = open(filename, 'rb')
        while True:
            data = f.read(4096)
            if not data:
                break
            self.request.send(data.encode())
        f.close()
        time.sleep(1)
        self.request.send('EOF'.encode())
        print("send file success!")

    def handle(self):
        print("get connection from :",self.client_address)
        while True:
            try:
                data = self.request.recv(4096).decode()
                print("get data:", data)
                if not data:
                    print("break the connection!")
                    break
                else:
                    action,user_email,filename= data.split()
                    if action == "put":
                        print(user_email)
                        self.recvfile(filename,user_email)
                    elif action == 'get':
                        self.sendfile(filename)
                    else:
                        print(action)
                        continue
            except Exception as e:
                print("get error at:",e)


if __name__ == "__main__":
    host = ''
    port = 23337
    s = socketserver.ThreadingTCPServer((host,port), MyTcpServer)
    s.serve_forever()

