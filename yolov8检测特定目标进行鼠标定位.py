import cv2
import pyautogui
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # 加载YOLOv8模型
cap = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\123.mp4")# 打开视频文件

while cap.isOpened():       #遍历视频帧
    success, frame = cap.read() #从视频中读取一帧
    if success:
        results = model.predict(frame)# 对帧运行YOLOv8推理
        #print(results)
        annotated_frame = results[0].plot(line_width=1)# 在帧上可视化结果
        boxes = results[0].boxes
        if len(boxes) != 0:  #判断，检测到才进行绘制
            box = boxes[0]  # 返回一个框（box）  
            #print(box.xyxy)
            coordinates = box.xyxy
            x1, y1, x2,y2 =coordinates[0]  # 提取左上角坐标

            x1 = int(x1)  # 将坐标转换为整数
            y1 = int(y1)  # 将坐标转换为整数
            x2 = int(x2)  # 将坐标转换为整数
            y2 = int(y2)  # 将坐标转换为整数

            #print(f"x1: {x1}, y1: {y1}") #输出坐标
           #q print(f"x2: {x2}, y2: {y2}") #输出坐标
            kuan = x2 - x1   #宽度 = 右下角坐标x - 左上角坐标x
            gao = y2 - y1   #高度 = 右下角坐标y - 左上角坐标y
            
            zhongxinX = x1 + kuan / 2  #中心点坐标x = 左上角坐标x + 宽度 / 2
            zhongxinY = y1 + gao /2 # 中心点坐标y = 左上角坐标y + 高度 / 2

            pyautogui.moveTo(zhongxinX,zhongxinY)
            
            
            #显示出来，带注释的帧
            cv2.imshow("YOLOv8", annotated_frame)
 
            # 将鼠标移动到指定位置q
            # pyautogui.moveTo(x1+100, y1+100)
                # 如果按下 'q' 键，中断循环
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        # 如果达到视频末尾，中断循环
        break

# 释放视频捕获对象并关闭显示窗口
cap.release()
cv2.destroyAllWindows()
