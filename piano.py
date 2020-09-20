import pyautogui
from mss import mss
import time


start_x = 666
start_y = 561

# bbox de la zone a capturer
bbox = (start_x, start_y, start_x + 435, start_y + 1)

cords_x = [0, 145, 290, 434]


def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(190, 699)
        t2 = time.time()
        print(t2 - t1)  # 2.51 sec   => 2.38


def print_mouse_pos():
    """
    get the mouse position on screen
    :return:
    """
    # pyautogui.displayMousePosition()
    while True:
        print(pyautogui.position())
        time.sleep(1)


def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] == 75 and img.pixel(cord, 0)[1] == 159:
                    pyautogui.click(start_x + cord, start_y)
                    break
                elif img.pixel(cord, 0)[0] == 0 and img.pixel(cord, 0)[1] == 0:
                    pyautogui.click(start_x + cord, start_y)
                    break

# time.sleep(3)
print_mouse_pos()
