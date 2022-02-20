import sys
import core2
from configparser import ConfigParser
import ast
import win32gui
import win32ui
import win32con
from PIL import Image
import time
import cv2
import numpy as np
import random
import argparse
from datetime import datetime
from threading import Thread
from subprocess import Popen, CREATE_NEW_CONSOLE
import os

parser = argparse.ArgumentParser(description='Пробная версия запуска')
parser.add_argument(
    '--title',
    type=str,
    default=''
)

my_namespace = parser.parse_args()
name = my_namespace.title

player_pos = 0
camera = 0
in_game = None
inv = 0
point = 0
pers = 0.9
state = 0
need_close = 0
tyrian_pers = 0.88

winname = name
file = 'config.ini'
config = ConfigParser()
config.read(file)


device = ast.literal_eval(config[winname]['ip'])
size = ast.literal_eval(config[winname]['size'])
typebot = ast.literal_eval(config[winname]['typebot'])
dev = ast.literal_eval(config[winname]['dev'])
timer_restart = ast.literal_eval(config[winname]['timer_restart'])
auto_relog = ast.literal_eval(config[winname]['auto_relog'])
lvl = ast.literal_eval(config[winname]['lvl'])
bs_bat = ast.literal_eval(config[winname]['bat'])


def real_time():
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime("%H:%M:%S")
    t = '[' + winname + ']' + ' ' + timeStr + ' '
    return t


def game_check():
    global in_game, camera, player_pos, size, inv
    ore_pic = ['sword.png']
    for x in ore_pic:
        pos = core2.imgsearch("./check/" + x, 0.93, winname, size, f_name='game_check', dev=dev)
        b = pos.screen()
        time.sleep(.5)
        if b[0] != -1:
            if x == 'sword.png':
                in_game = 2
                continue
        else:
            print(real_time() + 'Включаю вторую проверку')
            player_pos = 0
            camera = 0
            in_game = None
            ore_pic1 = ['play_now.png', 'play.png', 'teleport_offer.png', 'deposit_all.png']
            for y in ore_pic1:
                pos = core2.imgsearch("./check/" + y, 0.9, winname, size, f_name='game_check', dev=dev)
                b = pos.screen()
                time.sleep(.5)
                if b[0] != -1:
                    print(real_time() + 'Поток проверки 2, нашел', y)
                    if y == 'deposit_all.png':
                        print('Внутри проверки Застрял в сундуке ')
                        pos = core2.imgsearch("./img_tyrian/deposit_exit.png", 0.90, winname, size,
                                             f_name='check_tyrian_storage_use',
                                             dev=dev)
                        b = pos.screen()
                        if b[0] != -1:
                            print(real_time() + 'Закрываю сундук 2 ' + str(x))
                            c = core2.adb(b, 0, 0, 0, 0, device, size)
                            c.tap()
                            time.sleep(3)
                            player_pos = 2
                            inv = 0

                    if y == 'teleport_offer.png':
                        print('Внутри проверки teleport_offer ')
                        camera = 0
                        player_pos = 0
                        in_game = None
                        time.sleep(1.5)
                        pos = core2.imgsearch("./check/teleport_off.png", 0.93, winname, size, f_name='game_check',
                                             dev=dev)
                        b = pos.screen()
                        print(real_time() + 'Кликаю авто-отказ о урода с тпшкой')
                        c = core2.adb(b, 0, 0, 0, 0, device, size)
                        c.tap()
                        time.sleep(1.5)
                        pos = core2.imgsearch("./check/decline.png", 0.93, winname, size, f_name='game_check', dev=dev)
                        b = pos.screen()
                        print(real_time() + 'Кликаю Decline')
                        c = core2.adb(b, 0, 0, 0, 0, device, size)
                        c.tap()
                        time.sleep(1.5)
                    if y == 'play_now.png':
                        in_game = 1
                        camera = 0
                        player_pos = 0
                        pos = core2.imgsearch("./check/play_now.png", 0.93, winname, size, f_name='game_check', dev=dev)
                        b = pos.screen()
                        if b[0] != -1 and size == 777:
                            print(real_time() + 'Проверка 1: мы в лобби, ща зайдём обратно')
                            pos = core2.imgsearch("./check/favor.png", 0.93, winname, size,
                                                 f_name='game_check', dev=dev)
                            b = pos.screen()
                            if b[0] != -1:
                                time.sleep(1)
                                c = core2.adb(b, 50, 0, 0, 0, device, size)
                                c.tap()
                                print(real_time() + 'Вхожу обратно на избранный сервер')
                                i = 0
                                while i <= 20:
                                    time.sleep(2)
                                    pos = core2.imgsearch("./check/sword.png", 0.93, winname, size,
                                                         f_name='tyrian_inv_check', dev=dev)
                                    b = pos.screen()
                                    i += 1
                                    if b[0] != -1:
                                        print(real_time() + 'Мы в игре ...')
                                        camera = 0
                                        player_pos = 0
                                        time.sleep(3)
                                        break

                        if b[0] != -1 and size == 1280:
                            print(real_time() + '(МОБ) Проверка 1: мы в лобби, ща зайдём обратно')
                            pos = core2.imgsearch("./check/favor.png", 0.93, winname, size,
                                                 f_name='game_check', dev=dev)
                            b = pos.screen()
                            if b[0] != -1:
                                time.sleep(1)
                                c = core2.adb(b, 50, 0, 0, 0, device, size)
                                c.tap()
                                print(real_time() + '(МОБ) Вхожу обратно на избранный сервер')
                                while True:
                                    time.sleep(2)
                                    pos = core2.imgsearch("./check/sword.png", 0.93, winname, size,
                                                         f_name='tyrian_inv_check', dev=dev)
                                    b = pos.screen()
                                    if b[0] != -1:
                                        print(real_time() + 'Мы в игре ...')
                                        camera = 0
                                        time.sleep(3)
                                        break
                        if b[0] != -1 and size == 1281:
                            print(real_time() + 'Проверка 1: мы в лобби, ща зайдём обратно')
                            pos = core2.imgsearch("./check/play_now.png", 0.93, winname, size,
                                                 f_name='game_check', dev=dev)
                            b = pos.screen()
                            if b[0] != -1:
                                time.sleep(1)
                                c = core2.adb(b, 0, 0, 0, 0, device, size)
                                c.tap()
                                print(real_time() + 'Вхожу обратно в игру')
                                camera = 0
                                player_pos = 0
                                time.sleep(25)
                    if y == 'play.png':
                        in_game = 0
                        camera = 0
                        player_pos = 0
                        pos = core2.imgsearch("./check/play.png", 0.9, winname, size, f_name='game_check',
                                             dev=dev)
                        b = pos.screen()
                        if b[0] != -1:
                            print(real_time() + 'Проверка 2: вижу кнопку Login')
                            pos = core2.imgsearch("./check/play.png", 0.9, winname, size,
                                                 f_name='game_check', dev=dev)
                            b = pos.screen()
                            if b[0] != -1:
                                time.sleep(1)
                                c = core2.adb(b, 0, 0, 0, 0, device, size)
                                c.tap()
                                print(real_time() + 'Логинюсь обратно')
                                time.sleep(8)


def camera_swipe():
    global player_pos, camera
    time.sleep(2)
    rand = random.randint(1500, 1950)
    rand_x = random.randint(0, 300)
    rand_y = random.randint(220, 300)
    b = (1280 / 2, 720 / 2)
    c = core2.adb(b, rand_x, rand_y, rand, 0, device, size)
    c.swipe()
    time.sleep(3)
    camera = 1
    player_pos = 1


def rune_point_1():
    global player_pos
    pic = ['point_1.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.9, winname, size, f_name='rune_point_1', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Иду в первую точку')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            time.sleep(17)
            player_pos = 3
            break


def rune_point_1_altar():
    global player_pos
    pic = ['altar_0.png', 'altar_1.png', 'altar_1_1.png', 'altar_1_2.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.87, winname, size, f_name='rune_point_1_altar', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Вхожу в алтарь')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            time.sleep(2)
            i = 0
            while i <= 10:
                time.sleep(1)
                pos = core2.imgsearch("./runecraft_img/in_altar.png", 0.9, winname, size,
                                      f_name='rune_point_1_altar', dev=dev)
                b = pos.screen()
                i += 1
                if b[0] != -1:
                    print(real_time() + 'Я в данже')
                    player_pos = 4
                    break

            break


def rune_point_2_altar():
    global player_pos
    pic = ['altar_2.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.9, winname, size, f_name='rune_point_2_altar', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Иду к центру')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            time.sleep(4)
            player_pos = 5
            break


def rune_point_2_altar_craft():
    global player_pos
    pic = ['earth_talisman.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.87, winname, size, f_name='rune_point_2_altar_craft', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Talisman click')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            time.sleep(1.5)
            pic = ['altar_3.png']
            for x in pic:
                pos = core2.imgsearch('./runecraft_img/' + x, 0.87, winname, size, f_name='rune_point_2_altar_craft', dev=dev)
                b = pos.screen()
                if b[0] != -1:
                    print(real_time() + 'Altar click')
                    c = core2.adb(b, 0, 0, 0, 0, device, size)
                    c.tap()
                    time.sleep(1.5)
                    player_pos = 6
                    break
                else:
                    player_pos = 4
            break


def rune_altar_exit():
    global player_pos
    pic = ['altar_exit.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.9, winname, size, f_name='rune_altar_exit', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Нашел выход')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            time.sleep(2)
            i = 0
            while i <= 10:
                time.sleep(1)
                pos = core2.imgsearch("./runecraft_img/back_point.png", 0.9, winname, size,
                                      f_name='rune_altar_exit', dev=dev)
                b = pos.screen()
                i += 1
                if b[0] != -1:
                    print(real_time() + 'Я вышел из данжа')
                    player_pos = 7
                    break

            break


def rune_back_point():
    global player_pos
    pic = ['back_point.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.86, winname, size, f_name='rune_back_point', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Нашел точку, иду к сундуку')
            c = core2.adb(b, 130, 15, 0, 0, device, size)
            c.tap()
            time.sleep(17)
            player_pos = 1
            break


def rune_storage():
    global player_pos
    pic = ['storage.png']
    for x in pic:
        pos = core2.imgsearch('./runecraft_img/' + x, 0.9, winname, size, f_name='rune_storage', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            print(real_time() + 'Use storage')
            c = core2.adb(b, 0, 0, 0, 0, device, size)
            c.tap()
            i = 0
            while i <= 10:
                time.sleep(1)
                pos = core2.imgsearch("./runecraft_img/preset_1.png", 0.9, winname, size,
                                      f_name='rune_storage', dev=dev)
                b = pos.screen()
                i += 1
                if b[0] != -1:
                    print(real_time() + 'Cундук открыл')
                    print(real_time() + 'Use preset 1')
                    c = core2.adb(b, 0, 0, 0, 0, device, size)
                    c.tap()
                    time.sleep(4)
                    player_pos = 2
                    break
            break


def rune_teleport_back():
    global player_pos, camera, inv, camera, point
    rand1 = random.randint(3, 5)
    pos = core2.imgsearch("./check/sword.png", 0.93, winname, size, f_name='rune_teleport_back', dev=dev)
    b = pos.screen()
    if b[0] != -1:
        c = core2.adb(b, 0, 0, 0, 0, device, size)
        c.tap()
        print(real_time() + 'Типа жму кнопку панели скилов')
        time.sleep(rand1)
        pos = core2.imgsearch("./check/book.png", 0.93, winname, size, f_name='rune_teleport_back', dev=dev)
        b = pos.screen()
        if b[0] != -1:
            c = core2.adb(b, -90, 0, 0, 0, device, size)
            print(real_time() + 'Жму книжку)')
            c.tap()
            while True:
                time.sleep(rand1)
                print(real_time() + 'Ищу Duel Arena')
                pos = core2.imgsearch("./runecraft_img/duel_arena.png", 0.9, winname, size, f_name='rune_teleport_back', dev=dev)
                b = pos.screen()
                c = core2.adb(b, 0, 0, 0, 0, device, size)
                c.tap()
                time.sleep(10)
                pos = core2.imgsearch("./check/sword.png", 0.90, winname, size, f_name='rune_teleport_back', dev=dev)
                b = pos.screen()
                if b[0] != -1:
                    c = core2.adb(b, 0, 0, 0, 0, device, size)
                    c.tap()
                    print(real_time() + 'Типа жму кнопку панели скилов')
                    break


def main():
    global player_pos, camera, size
    size = int(size)
    print(real_time() + 'Добро пожаловать // Скрипт 1.0 ( RuneCrafting )')
    time.sleep(1)
    q = 0
    while True:
        try:
            time.sleep(.5)
            q += 1
            if q >= 15:
                # print('делаю проверку состояния клиента')
                game_check()
                q = 0

            if in_game == 2:
                # print('Player pos: ', player_pos, ' - Camera: ', camera)

                if camera == 0 and player_pos == 0:
                    camera_swipe()
                    rune_teleport_back()
                    rune_back_point()
                elif camera == 0 and player_pos == 1:
                    camera_swipe()
                elif camera == 1 and player_pos == 1:
                    rune_storage()
                elif camera == 1 and player_pos == 2:
                    rune_point_1()
                elif camera == 1 and player_pos == 3:
                    rune_point_1_altar()
                elif camera == 1 and player_pos == 4:
                    rune_point_2_altar()
                elif camera == 1 and player_pos == 5:
                    rune_point_2_altar_craft()
                elif camera == 1 and player_pos == 6:
                    rune_altar_exit()
                elif camera == 1 and player_pos == 7:
                    rune_back_point()
        except Exception:
            print(real_time() + 'Исключение сработало')
            continue
if __name__ == '__main__':
    main()