import cv2
from ultralytics import YOLO
import time
import subprocess

subprocess.Popen(["explorer.exe", "C:\\Users\\Administrator"])     #打开指定文件夹
model = YOLO('yolov8n.pt')  # 加载YOLOv8模型
cap = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\123.mp4")# 打开视频文件

while cap.isOpened():       #遍历视频帧
    success, frame = cap.read() #从视频中读取一帧
    if success:
        results = model.predict(frame,save=True)# 对帧运行YOLOv8推理
        #print(results)
        annotated_frame = results[0].plot(line_width=1)# 在帧上可视化结果

        boxes = results[0].boxes

        for index, cls_value in enumerate(boxes.cls):    #遍历id
            #print("如下:", (index, cls_value))
            cls_id = int(cls_value)  # 将类别ID转换为整数类型
            label = model.names[cls_id]  # 根据类别ID获取对应的标签名称
            #print("标签:", label) #输出标签
            if label =="person": #判断，如果是人，就进行截图
                #print("截图")
                timestamp = int(time.time())# 获取当前时间戳（Unix 时间戳）
                filename = f'frame_{timestamp}.png'# 生成文件名（以时间戳命名）
                cv2.imwrite(filename, frame)  # 将帧保存为 'frame.png' 文件
            
        if len(boxes) != 0:  #判断，检测到才进行绘制
        
            box = boxes[0]  # 返回一个框（box）  
            #print(box.xyxy)
            coordinates = box.xyxy
            x1, y1, _, _ = coordinates[0]  # 提取左上角坐标并忽略其他两个坐标
            x1 = int(x1)  # 将坐标转换为整数
            y1 = int(y1)  # 将坐标转换为整数
            print(f"x1: {x1}, y1: {y1}") #输出坐标
            #显示出来，带注释的帧
            cv2.imshow("YOLOv8", annotated_frame)
                # 将窗口移动到屏幕 0
            cv2.moveWindow("YOLOv8", 0, 0)
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