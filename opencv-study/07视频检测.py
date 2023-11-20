import cv2 as cv


# 人脸检测函数
def face_detect_demo(img):
    # 将图像转换为灰度图
    gray = cv.cvtColor(img, cv.COLOR_BGRA2BGR)

    # 加载人脸检测器（使用Haar级联分类器）
    face_detect = cv.CascadeClassifier('D:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    # 在灰度图上进行人脸检测
    faces = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 遍历检测到的人脸，并在图像上绘制矩形框
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

    # 显示结果图像
    cv.imshow('result', img)


# 读取摄像头
cap = cv.VideoCapture(0)



# 等待按键输入，按下 'q' 键退出程序
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(0):
        break

# 关闭所有窗口
cv.destroyAllWindows()

cap.release()
