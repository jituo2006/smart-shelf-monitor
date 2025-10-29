import cv2
from ultralytics import YOLO

# 加载预训练 YOLOv8 模型
model = YOLO('yolov8n.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Failed to open camera!")
    exit()

# 目标类别
target_classes = ["bottle", "chair", "orange", "cup", "laptop", "cell phone", "person"]

# 主循环
while True:
    # 读取摄像头画面
    ret, frame = cap.read()  
    if not ret:
        print("Failed to grab frame!")
        break

    # 模型推理，目标检测
    results = model(frame, verbose=False)

    for r in results:
        # 获取检测到的边界框
        boxes = r.boxes
        for box in boxes:  
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]

            if cls_name in target_classes:
                # 获取边界框坐标
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                x_center = int((x1 + x2) / 2)
                y_center = int((y1 + y2) / 2)

                # 画矩形框并标注
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                cv2.putText(frame, cls_name, (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                # 打印坐标信息
                print(f"检测到 {cls_name}，中心点坐标: ({x_center}, {y_center})")

    # 显示结果画面
    cv2.imshow("YOLOv8 Live Detection", frame)

    # 通过0xFF确保兼容性
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()

