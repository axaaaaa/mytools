import os
import win32api  #pip3 install pywin32
os.system(r"start E:\steam\steam.exe")
#os.system(r"start C:\Program Files\5EClient.exe")

win32api.ShellExecute(0, 'open', r'C:\\Program Files\\5EClient\\5EClient.exe', '','',1)