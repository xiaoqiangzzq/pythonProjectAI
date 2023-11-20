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

class Game():

    def __int__(self):
        print("hello")


    def getScreen(self):
        # 开始截图并处理
        max_win_width = GetSystemMetrics(SM_CXSCREEN)
        max_win_height = GetSystemMetrics(SM_CYSCREEN)
        img = self.windowshots(0, 0, max_win_width, max_win_height)
        cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO)
        cv2.setMouseCallback("image", self.on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        time.sleep(0.5)


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




if __name__ == '__main__':
    g = Game()
    g.getScreen()





