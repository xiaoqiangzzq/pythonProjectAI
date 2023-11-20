import cv2

# 打开摄像头（0表示默认摄像头）
cap = cv2.VideoCapture(0)
# 设置标志位和图像编号
flag = 1
num = 1

# 持续捕获摄像头图像并显示
while (cap.isOpened()):
    # 读取摄像头帧
    ret_flag, Vshow = cap.read()

    # 显示摄像头图像
    cv2.imshow("capture_test", Vshow)

    # 检测按键
    k = cv2.waitKey(1) & 0xFF

    # 按下 's' 键保存当前帧为图片
    if k == ord('s'):
        # 保存图像到指定路径，使用编号命名
        cv2.imwrite('C:/Users/14817/Pictures/Screenshots/' + str(num) + "zzq1" + ".jpg", Vshow)
        print("成功保存图片：" + str(num) + ".jpg")
        print("--------------------")
        num += 1
    # 按下空格键退出循环
    elif k == ord(' '):
        break

# 释放摄像头资源
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()
