Matlab Server
=============
基于ubuntu搭建的Matlab服务器程序
--------------------------------

###功能简介：

将需要长时间计算的matlab程序上传至服务器队列，服务器经过计算之后将结果返回。

###组成：
* matlab
* python3
* PyQt5
* mysql

###配置过程：

##服务器端

> 1.MyTcpServer.py
> 2.smtplib_build.py
> 3.task.py
> 4.ziptask.py
> 5.email.ini
> 6.ListenSer.py
> 7.threadser.py

1. 配置mysql
2. 服务器端运行MyTcpserver.py文件接收服务端
3. 服务器端运行threadser.py 任务监听程序
4. 配置email.ini邮件服务器和账号

###客户端

> 1.MyWindow.py
> 2.sendfile.py
> 3.upload_task.py

1.配置upload_task.py 中的服务器参数
2.运行MyWindow.py 上传任务 
