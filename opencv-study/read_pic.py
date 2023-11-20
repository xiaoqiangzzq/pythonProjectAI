import cv2 as cv

img = cv.imread('face1.jpg')

# 检查图像是否成功加载
if img is not None:
    # 获取原始图像尺寸
    height, width = img.shape[:2]

    # 缩放图像为原始尺寸的50%
    scaled_img = cv.resize(img, (int(width/4), int(height/4)))

    # 显示缩放后的图像
    cv.imshow('Scaled Image', scaled_img)

    # 等待用户按下任意键后关闭窗口
    cv.waitKey(0)

    # 关闭所有窗口
    cv.destroyAllWindows()
else:
    print("无法加载图像")
