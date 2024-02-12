import pyautogui
import time
import datetime

while True:
    # 获取当前时间戳
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
     # 获取屏幕尺寸
    screenWidth, screenHeight = pyautogui.size()
    # 获取目标窗口的位置和尺寸
    targetWindow = pyautogui.getWindowsWithTitle('窗口标题')[0]
    left, top, width, height = targetWindow.left, targetWindow.top, targetWindow.width, targetWindow.height
     # 截取目标窗口的截图
    image = pyautogui.screenshot(region=(left, top, width, height))

    # 使用时间戳保存截图
    filename = f'{timestamp}.png'
    image.save(filename)
    time.sleep(1)
    print(filename)



    

   

    

   



