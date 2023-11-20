import cv2 as cv


# 人脸检测函数
def face_detect_demo():
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


# 读取原始图像
org_img = cv.imread('face1.jpg')

# 获取原始图像尺寸
height, width = org_img.shape[:2]

# 缩放图像为原始尺寸的50%
img = cv.resize(org_img, (int(width / 4), int(height / 4)))

# 调用人脸检测函数
face_detect_demo()

# 等待按键输入，按下 'q' 键退出程序
while True:
    if ord('q') == cv.waitKey(0):
        break

# 关闭所有窗口
cv.destroyAllWindows()
