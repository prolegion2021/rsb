import win32con
import win32gui
import win32ui
from PIL import Image
import time
import cv2
import numpy as np
import random
import os
from configparser import ConfigParser
import ast

file = 'config.ini'
config = ConfigParser()
config.read(file)

emulator = ast.literal_eval(config['bs_check']['emulator'])
adbfolder = ast.literal_eval(config['bs_check']['adbfolder'])


class adb:
    def __init__(self, my_pos, my_x, my_y, my_time, my_random, my_device, my_size):
        self.pos = my_pos
        self.x = my_x
        self.y = my_y
        self.time = my_time
        self.random = my_random
        self.device = my_device
        self.size = my_size
        self.size = int(self.size)

    def tap(self):
        rand = random.randint(0, 2)
        rand_time = random.randint(40, 80)
        x = round(self.pos[0])
        y = round(self.pos[1])
        if self.size == 777:
            #print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           ((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           rand_time + self.time))
        if self.size == 1280:
            print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           ((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           rand_time + self.time))
        if self.size == 1281:
            print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x + (self.x/100*50)),
                                                                           ((y + rand) + self.y + (self.y/100*50)),
                                                                           ((x + rand) + self.x + (self.x/100*50)),
                                                                           ((y + rand) + self.y + (self.y/100*50)),
                                                                           rand_time + self.time))

    def long_tap(self):
        rand = random.randint(0, 2)
        rand_time = random.randint(40, 80)
        x = round(self.pos[0])
        y = round(self.pos[1])
        if self.size == 777:
            #print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           ((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           rand_time + self.time))
        if self.size == 1280:
            print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           ((x + rand) + self.x),
                                                                           ((y + rand) + self.y),
                                                                           rand_time + self.time))
        if self.size == 1281:
            print((x + rand), (y + rand))
            os.system('c:/adb/adb -s ' + str(self.device)
                      + ' shell input touchscreen swipe %d %d %d %d %d' % (((x + rand) + self.x + (x/100*50)),
                                                                           ((y + rand) + self.y + (y/100*50)),
                                                                           ((x + rand) + self.x + (x/100*50)),
                                                                           ((y + rand) + self.y + (y/100*50)),
                                                                           rand_time + self.time))

    def tap_drop(self):
        rand_x = random.randint(450, 700)
        rand_y = random.randint(-70, 250)
        x1 = round(self.pos[0] + self.x)
        y1 = round(self.pos[1] + self.y)
        if self.size == 777:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1) + ' '
                      + str(y1) + ' '
                      + str(x1 - rand_x) + ' '
                      + str(y1 - rand_y) + ' '
                      + str(self.time))
        if self.size == 1280:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1) + ' '
                      + str(y1) + ' '
                      + str(x1 - rand_x) + ' '
                      + str(y1 - rand_y) + ' '
                      + str(self.time))
        if self.size == 1281:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1 + (x1/100*50)) + ' '
                      + str(y1 + (y1/100*50)) + ' '
                      + str(x1 + (x1/100*50) - rand_x) + ' '
                      + str(y1 + (y1/100*50) - rand_y) + ' '
                      + str(self.time))

    def swipe(self):
        x1 = self.pos[0]
        y1 = self.pos[1]
        if self.size == 777:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1 - self.x) + ' '
                      + str(y1 - self.y) + ' '
                      + str(x1 - self.x) + ' '
                      + str(y1 + self.y) + ' '
                      + str(self.time))
        if self.size == 1280:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1 - self.x) + ' '
                      + str(y1 - self.y) + ' '
                      + str(x1 - self.x) + ' '
                      + str(y1 + self.y) + ' '
                      + str(self.time))
        if self.size == 1281:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input touchscreen swipe "
                      + str(x1 + (x1/100*50) - self.x) + ' '
                      + str(y1 + (y1/100*50) - self.y) + ' '
                      + str(x1 + (x1/100*50) - self.x) + ' '
                      + str(y1 + (y1/100*50) + self.y) + ' '
                      + str(self.time))

    def back_button(self):
        if self.size == 777:
            os.system("c:/adb/adb -s " + str(self.device) + " shell input keyevent 4")

    def kill_app(self):
        print("Закрываю игру")
        os.system("c:/adb/adb -s " + str(self.device) + " shell am force-stop com.jagex.runescape.android")

    def run_app(self):
        print("Запускаю новую игру")
        os.system("c:/adb/adb -s " + str(self.device) + " shell am start com.jagex.runescape.android/com.jagex.android.MainActivity")


class imgsearch:
    def __init__(self, image, res, winname, size, f_name, dev):
        self.my_image = image
        self.my_res = res
        self.my_winname = winname
        self.my_size = size
        self.my_f_name = f_name
        self.my_dev = dev

    def screen(self):
        try:
            if self.my_dev == 1:
                print('DEV: Обращение с функции: ' + self.my_f_name)
            time.sleep(.1)
            hwnd = win32gui.FindWindow(None, self.my_winname)
            window_rect = win32gui.GetWindowRect(hwnd)
            size = int(self.my_size)
            if size == 777:
                w = window_rect[2] - window_rect[0]
                h = window_rect[3] - window_rect[1]
                border_pixels = 3
                titlebar_pixels = 42
            if size == 1280:
                w = window_rect[2] - window_rect[0]
                h = window_rect[3] - window_rect[1]
                border_pixels = 16
                titlebar_pixels = 39
            if size >= 1281:
                w = window_rect[2] - window_rect[0]
                h = window_rect[3] - window_rect[1]
                border_pixels = 16
                titlebar_pixels = 39

            w = w - (border_pixels * 2)
            h = h - titlebar_pixels - border_pixels
            cropped_x = border_pixels
            cropped_y = titlebar_pixels

            hwnddc = win32gui.GetWindowDC(hwnd)
            mfcdc = win32ui.CreateDCFromHandle(hwnddc)
            savedc = mfcdc.CreateCompatibleDC()
            saveBitMap = win32ui.CreateBitmap()

            saveBitMap.CreateCompatibleBitmap(mfcdc, w, h)
            savedc.SelectObject(saveBitMap)
            savedc.BitBlt((0, 0), (w, h), mfcdc, (cropped_x, cropped_y), win32con.SRCCOPY)

            bmpinfo = saveBitMap.GetInfo()
            bmpstr = saveBitMap.GetBitmapBits(True)

            im = Image.frombuffer(
                'RGB',
                (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                bmpstr, 'raw', 'BGRX', 0, 1)

            win32gui.DeleteObject(saveBitMap.GetHandle())
            savedc.DeleteDC()
            mfcdc.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwnddc)

            img_rgb = np.array(im)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            #img_size = tuple(img_gray.shape[1::-1])
            #print(img_size)
            #cv2.imshow("cropped", img_gray)
            #cv2.waitKey(0)
            try:
                template = cv2.imread(self.my_image, cv2.IMREAD_GRAYSCALE)
                w, h = template.shape[::-1]
                result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                if max_val <= self.my_res:
                    return [-1, -1]
                x, y = max_loc
                #cv2.rectangle(img_gray, x, y, 255, 2)
                #rand_x = random.randint(0, 2)
                #rand_y = random.randint(0, 2)
                xy = round(x + (w / 2)), round(y + (h / 2))
                # cv2.imshow("cropped", img_gray)
                # cv2.waitKey(0)
                return xy
            except Exception:
                print('Не нашел подходящей области')
        except Exception:
            print('Не получилось сделать скрин')
            time.sleep(1)


class img_max:
    def __init__(self, screen, image, res, winname, size, f_name, dev):
        self.my_image = image
        self.my_res = res
        self.my_winname = winname
        self.my_size = size
        self.my_f_name = f_name
        self.my_dev = dev
        self.my_screen = screen

    def search_m(self):
        try:
            template = cv2.imread(self.my_image, cv2.IMREAD_GRAYSCALE)
            w, h = template.shape[::-1]
            result = cv2.matchTemplate(self.my_screen, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val <= self.my_res:
                return [-1, -1]
            x, y = max_loc
            rand_x = random.randint(0, w)
            rand_y = random.randint(0, h)
            xy = round(x + rand_x), round(y + rand_y)
            return xy
        except Exception:
            print('Не нашел подходящей области')