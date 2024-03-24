from socket import *
udp=socket(AF_INET,SOCK_DGRAM)#1.创建套接字，SOCK_STREAM为TCP协议，SOCK_DGRAM为UDP协议
addr=('',7788)#''代表本地所有地址，7788为本地端口
udp.bind(addr)#2.绑定
data=udp.recvfrom(1024)#3.接受数据1024字节
print(data)#打印