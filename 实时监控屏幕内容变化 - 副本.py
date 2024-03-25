from PIL import ImageGrab
import numpy as np
import time
import requests  # Import the requests library
 
def a(region):
    """
    获取屏幕指定区域的截图
    """
    
    return np.array(screenshot)
 
def b():
    """
    发送HTTP请求的函数
    """
    # 替换接收通知的Url，我这里使用的是iOS的Bark App
    url = "https://xxxxxxxxxxxxxxxx"
    payload = {"key": "value"}
    headers = {"Content-Type": "application/json"}
 
    response = requests.post(url, json=payload, headers=headers)
 
    # 打印结果
    print("HTTP Response:", response.text)
 

   

if __name__ == "__main__":

    region_to_monitor = (0, 0, 100, 100) # 替换为要监控的区域坐标 (left, top, right, bottom)

    while True:
        screenshot = ImageGrab.grab(bbox=region_to_monitor)   #监控屏幕指定区域的像素变化
 
        if not np.array_equal(screenshot, screenshot):
            print("指定区域的像素发生变化")
            # 发送HTTP请求
            #
            print("发生变化")

        time.sleep(1)
    