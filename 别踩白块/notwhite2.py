import cv2
import numpy as np
from matplotlib import pyplot as plt
from win32api import GetSystemMetrics
from win32con import SRCCOPY, SM_CXSCREEN, SM_CYSCREEN
from win32gui import FindWindow, GetWindowDC, DeleteObject, ReleaseDC, GetDesktopWindow
from win32ui import CreateDCFromHandle, CreateBitmap
import time
import pyautogui
import sys
import threading

class GameStart():
    def __init__(self):
        # 初始化坐标和计数器
        self.first_pointX = 0
        self.first_pointY = 0
        self.second_pointX = 0
        self.second_pointY = 0
        self.clock_number = 0
        self.center_post_list = []
    #
    # def on_EVENT_LBUTTONDOWN(self, event, x, y, flags, param):
    #     ：
    #
    #     定义了一个鼠标左键按下事件的回调函数。这个函数有五个参数，分别是event（事件类型）、x（鼠标点击位置的x坐标）、y（鼠标点击位置的y坐标）、
    #     flags（标志位，用于标识鼠标按下的一些状态，例如Shift、Ctrl等），以及param（用户传递的参数）。
    #
    # if self.clock_number > 1: ：
    #     如果clock_number大于1，说明已经完成了两次点击，此时关闭窗口。这是为了确保只能标定两个点。
    #
    # if event == cv2.EVENT_LBUTTONDOWN: ：
    #     判断事件是否为鼠标左键按下。
    #
    # xy = "%d,%d" % (x, y)：将鼠标点击的x和y坐标格式化为字符串。
    #
    # print(xy)：打印鼠标点击的坐标。
    #
    # if self.clock_number == 0: ：
    #     如果是第一次点击，记录第一个点的坐标。
    #
    # self.first_pointX = x：记录第一个点的x坐标。
    #
    # self.first_pointY = y：记录第一个点的y坐标。
    #
    # elif self.clock_number == 1:：如果是第二次点击，记录第二个点的坐标。
    #
    # self.second_pointX = x：记录第二个点的x坐标。
    #
    # self.second_pointY = y：记录第二个点的y坐标。
    #
    # self.clock_number += 1：递增clock_number，表示已经完成一次点击。
    def on_EVENT_LBUTTONDOWN(self, event, x, y, flags, param):
        if self.clock_number > 1:
            cv2.destroyWindow('image')

        # 左键按下
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            print(xy)

            if self.clock_number == 0:
                self.first_pointX = x
                self.first_pointY = y
            elif self.clock_number == 1:
                self.second_pointX = x
                self.second_pointY = y

            self.clock_number += 1

    def windowshots(self, x1, y1, x2, y2):
        # 截取指定区域的屏幕截图

        # 获取桌面窗口句柄
        hdesktop = GetDesktopWindow()
        # 获取桌面窗口的设备上下文DC（Divice Context）
        wDC = GetWindowDC(hdesktop)
        # 根据窗口的DC创建DC对象
        dcObj = CreateDCFromHandle(wDC)
        # 创建与窗口DC兼容的DC
        cDC = dcObj.CreateCompatibleDC()
        # 创建用于保存截图的Bitmap对象
        dataBitMap = CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, x2 - x1, y2 - y1)
        # 将Bitmap对象选入DC
        cDC.SelectObject(dataBitMap)
        # 通过BitBlt函数将屏幕内容拷贝到Bitmap中
        cDC.BitBlt((0, 0), (x2 - x1, y2 - y1), dcObj, (x1, y1), SRCCOPY)
        # 获取Bitmap中的像素数据
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        # 释放资源，删除对象
        DeleteObject(dataBitMap.GetHandle())
        cDC.DeleteDC()
        dcObj.DeleteDC()
        ReleaseDC(hdesktop, wDC)

        # 将像素数据转为NumPy数组
        screen = np.frombuffer(signedIntsArray, dtype='uint8')
        # 重塑数组形状，转换为BGR格式
        screen.shape = (y2 - y1, x2 - x1, 4)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

        return screen


    def press(self, key):
        # 处理按键事件
        print(key.char)

    def plt_show0(self, img):
        # 显示彩色图像
        b, g, r = cv2.split(img)
        img = cv2.merge([r, g, b])
        plt.imshow(img)
        plt.show()

    def plt_show(self, img):
        # 显示灰度图像
        plt.imshow(img, cmap="gray")
        plt.show()

    def get_pos(self, contours):
        # 获取轮廓的位置信息
        pos_list = []
        for contour in contours:
            rect = cv2.boundingRect(contour)
            x, y, weight, height = rect
            pos_list.append([x, y + height])
        return pos_list

    def speed_pos(self, contours, Min_Area=6500):
        # 过滤出大于指定面积的轮廓的位置信息
        chunk_contours = []
        for item in contours:
            if cv2.contourArea(item) > Min_Area:
                rect = cv2.boundingRect(item)
                x, y, weight, height = rect
                if height > 120:
                    for next_y in range(int(height / 120) + 1):
                        next_y += 1
                        chunk_contours.append([x + weight / 8, y + 120 * next_y])
                else:
                    chunk_contours.append([x + weight / 8, y + height])
        return chunk_contours

    def start(self):
        # 开始截图并处理
        max_win_width = GetSystemMetrics(SM_CXSCREEN)
        max_win_height = GetSystemMetrics(SM_CYSCREEN)
        img = self.windowshots(0, 0, max_win_width, max_win_height)
        cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO)
        cv2.setMouseCallback("image", self.on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        time.sleep(0.5)

        while True:
            img = self.windowshots(self.first_pointX, self.first_pointY, self.second_pointX, self.second_pointY)
            img = np.asarray(img)
            cv2.imwrite("image.png", img)
            img_gray = img.copy()
            img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
            ret, img_threshold = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY_INV)
            kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 7))
            image = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kernelY, iterations=1)
            kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            image = cv2.erode(image, kernelX)
            contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            self.center_post_list = self.speed_pos(contours)
            self.center_post_list = sorted(self.center_post_list, key=lambda tup: tup[1], reverse=True)
            if len(self.center_post_list) == 0:
                break

    def work(self):
        # 工作线程，处理鼠标点击
        while True:
            for pos in self.center_post_list:
                print(self.center_post_list)
                pyautogui.moveTo(int(pos[0] + self.first_pointX), int(pos[1] + self.first_pointY), duration=0)
                pyautogui.click()
                break

if __name__ == '__main__':
    Start = GameStart()
    t1 = threading.Thread(target=Start.start)
    t2 = threading.Thread(target=Start.work)
    t1.start()
    t2.start()
