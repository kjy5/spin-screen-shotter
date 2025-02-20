from time import sleep
import pyautogui as pg
from pyautogui import Point

screen_size = pg.size()
center = Point(screen_size.width // 2, screen_size.height // 2)

PREFIX = "closer"
OUTPUT_DIR = "output"

if __name__ == "__main__":
    pg.moveTo(center)
    pg.click()
    
    sleep(1)
    
    for i in range(15):
        pg.moveTo(center)
        with pg.hold("shift"):
            pg.drag(200, 0, duration=0.25, button="left")

        pg.screenshot(f"{OUTPUT_DIR}/{PREFIX}_{i}.png")
