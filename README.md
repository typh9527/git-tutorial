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

1. 配置mysql
2. 服务器端运行MyTcpserver.py文件接收服务端
3. 服务器端运行threadser.py 任务监听程序
4. 配置email.ini邮件服务器和账号
