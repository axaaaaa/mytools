from socket import *
client=socket(AF_INET,SOCK_DGRAM)#建立一个socket对象
client.connect(("192.168.14.1",7788))#连接客户端
client.send("tttt".encode())#发送一些数据
