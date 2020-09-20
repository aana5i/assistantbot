import time
import os, signal
import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import keyboard


# left x, second line from top Y, right X, bottom Y
gameCoords = [1350, 332, 1915, 793]

score = 0
previousLane = -1


def block_click(screen):
    global gameCoords, score, previousLane
    for y_ in range(5, len(screen) - 5, 5):
        for i in range(4):
            if previousLane == i:
                continue
            w = gameCoords[2] - gameCoords[0]
            x = i * w / 4 + w / 8
            y = len(screen) - y_
            if screen[y][round(x)] < 40:
                actualX = x + gameCoords[0]
                actualY = y + gameCoords[1]

                score += 1
                if score > 1000:
                    actualY += 10
                if score > 1250:
                    actualY += 10
                if score > 1450:
                    actualY += 10
                if score > 1600:
                    actualY += 20
                for k in range(1700, 2500):
                    if score > k:
                        actualY += 10
                    else:
                        break
                click(actualX, actualY)
                previousLane = i

                return
    # previousLane = -1


def launch():
    while True:
        if keyboard.is_pressed("f2"):
            break
        else:

            mousePos = queryMousePosition()
            # print('x: ', mousePos.x)
            # print('y: ', mousePos.y)
            # time.sleep(1)
            if gameCoords[2] > mousePos.x > gameCoords[0]:
                startTime = time.time()
                screen = np.array(ImageGrab.grab(bbox=gameCoords))
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                block_click(screen)
            else:
                if mousePos.x < 0:
                    score = 0
                    while True:
                        mousePos = queryMousePosition()
                        if gameCoords[2] < mousePos.x:
                            break
