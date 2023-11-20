import cv2
import os

# 创建一个LBPH人脸识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()

# 从文件中加载训练好的人脸识别模型
recognizer.read('C:/Users/14817/Pictures/Screenshots/trainer.yml')

# 存储人物名称的列表
names = []


# 人脸检测及识别函数
def face_detect_demo(img):
    # 将图像转换为灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 加载人脸检测器（Haar级联分类器）
    face_detector = cv2.CascadeClassifier(
        'D:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    # 检测图像中的人脸
    faces = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))

    # 遍历检测到的人脸
    for x, y, w, h in faces:
        # 绘制人脸矩形框
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

        # 绘制人脸圆形框
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=1)

        # 进行人脸识别
        ids, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # 根据置信度判断是否为未知人物
        if confidence > 80:
            cv2.putText(img, 'unknown', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            # 根据识别出的ID获取人物名称
            cv2.putText(img, str(names[ids - 1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)

    # 显示结果图像
    cv2.imshow('result', img)


# 用于获取人物名称的函数
def name():
    path = 'C:/Users/14817/Pictures/Screenshots/'
    # 获取图像目录中所有以指定扩展名结尾的图像文件路径
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if
                  f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 从文件名中提取人物名称，并添加到names列表中
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.', 2)[1])
        names.append(name)


# 打开视频文件（可替换为摄像头索引，如0表示默认摄像头）
cap = cv2.VideoCapture('C:/Users/14817/Pictures/Screenshots/1.mp4')
print("start =======")

# 获取人物名称
name()

# 循环读取视频帧并进行人脸识别
while True:
    flag, frame = cap.read()
    if not flag:
        break

    # 调用人脸检测及识别函数
    face_detect_demo(frame)

    # 按空格键退出循环
    if ord(' ') == cv2.waitKey(10):
        break

# 释放内存+关闭视频
cv2.destroyAllWindows()
cap.release()
