#!/usr/bin/python
#coding:utf-8
import socket
import time


def sendfile(s, filename):
    #:发送文件到服务器
    print("server ready,now client sending file~~")
    f = open(filename, 'rb')
    while True:
        data = f.read(4096)
        if not data:
            break
        s.sendall(data)
    f.close()
    time.sleep(1)
    s.sendall('EOF'.encode())
    print("send file success")

def confirm(s, client_command):
    s.send(client_command.encode())
    data = s.recv(4096).decode()
    if data == 'ready':
        return True
    else:
        return False

def sendtoweb(ip, filename):
    #:发送文件到html服务器
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 23336
        client_command = 'sendtoweb master@master.com ' + filename
        s.connect((ip,port))
        if confirm(s,client_command):
            sendfile(s,filename)
            return True
        else:
            print("server get error!")
            return False
    except socket.error as e:
        print("get error as ",e)
        return False
    finally:
        s.close()

if __name__ ==  "__main__":
    #send('127.0.0.1', 'joliu@s-an.org','web.txt')
    getfile('112.74.171.161','workpath/joliu@s-an.org/1487318818web.txt')
