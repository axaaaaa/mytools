from ultralytics import YOLO
 
# Load a model
model = YOLO('yolov8s.pt')  # pretrained YOLOv8n model
# Run batched inference on a list of images
results = model("C:\\Users\\Administrator\\Desktop\\12.mp4", conf=0.65)  # return a list of Results objects
label_counts = {}  # 用于记录每个label出现的次数的字典
 
for result in results:
    if result.boxes is not None:  # 检查是否存在边界框信息
        xyxy_boxes = result.boxes.xyxy  # 获取边界框的坐标信息
        conf_scores = result.boxes.conf  # 获取边界框的置信度信息
        cls_ids = result.boxes.cls  # 获取边界框的类别ID信息
 
        for box, conf, cls_id in zip(xyxy_boxes, conf_scores, cls_ids):
            x1, y1, x2, y2 = map(int, box)  # 将边界框的坐标转换为整数类型
            cls_id = int(cls_id)  # 将类别ID转换为整数类型
            label = model.names[cls_id]  # 根据类别ID获取对应的标签名称
 
            # 更新label_counts字典中对应label的计数
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1
            confidence = f"{conf:.2f}"  # 将置信度格式化为字符串
 
# 对label_counts字典按值进行排序，从大到小
sorted_labels = sorted(label_counts.items(), key=lambda x: x[1], reverse=True)
print(sorted_labels)
# 取出前三个种类及其对应的次数
top_three_labels = sorted_labels[:3]
 
# 分别将前三个种类赋值给两个变量
first_label = top_three_labels[0][0]
second_label = top_three_labels[1][0]
 
# 打印前三个种类及其对应的次数
for label, count in top_three_labels:
    print(f"{label}: {count}次")
 
print("出现次数前三的目标是：")
print(first_label)
print(second_label)
 
 
 
 
 