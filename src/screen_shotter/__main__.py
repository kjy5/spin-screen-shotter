import pyautogui as pg
from pyautogui import Point
from time import sleep

screen_size = pg.size()
center = Point(screen_size.width // 2, screen_size.height // 2)

if __name__ == '__main__':
    print(center)
