from PIL import ImageGrab
import numpy as np
import time


if __name__ == "__main__":
    xy = (0, 0, 100, 100) # 监控的区域坐标 (left, top, right, bottom)
    while True:
        screenshot1 = ImageGrab.grab(bbox=xy)   #获取指定屏幕区域的像素变化
        time.sleep(1)           #延迟
        screenshot2 = ImageGrab.grab(bbox=xy)   #获取指定屏幕区域的像素变化
        if not np.array_equal(screenshot1, screenshot2):  
            print("指定区域的像素发生变化")
       
  