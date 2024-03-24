import zipfile #导入zipfile模块
import threading #导入多线程模块
def a(f,password):
    try:#异常捕捉，下面的语句错误，就代表密码错误，就将执行except中的代码
    f.extractall(pwd=password.encode('utf-8'))
    print("破解成功，密码为:",password)
    except:
    print("密码错误")
    
def main():
    f = zipfile.ZipFile('D:/1.zip')#需要的zip
    print(f)
    zidian=open('D:/1.txt')#打开的字典
    for line in zidian.readlines():
        password=line.strip('\n')#减去回车键
        t=threading.Thread(target=a,args=(f,password))#多线程，a是函数,后面接 参数
        t.start()
main()