import socket
h = 'www.python.org'
ad = socket.gethostbyname(h)
print('{} 地址是{}'.format(h,ad))