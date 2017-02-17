#!/usr/bin/python
#coding:utf-8
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sendfile(filename):
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

def send(ip, user_email, filename):
    try:
        port=23336
        client_command = 'put '+user_email+' '+filename
        s.connect((ip, port))
        if confirm(s, client_command):
            sendfile(filename)
            return True
        else:
            print("server get error!")
            return False
    except socket.error as e:
        print("get error as ", e)
        return False
    finally:
        s.close()
if __name__ ==  "__main__":
    send('192.168.1.8', 'joliu@s-an.org','web.txt')
