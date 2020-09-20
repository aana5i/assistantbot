from PIL import ImageGrab
import time
from tkinter import *
import pyautogui
import keyboard

pyautogui.PAUSE = 0
locations = [50,150,250,350]


def begin():
    locations = [50,150,250,350]

    def GetWindow():
        xPos = window.winfo_x()+107
        yPos = window.winfo_y()+32
        locations = [50,150,250,350]
        window.destroy()

        while True:
            current = time.time()
            if keyboard.is_pressed("f2"):
                exit()
            else:
                img = pyautogui.screenshot(region=(xPos, yPos+310, 400, 1))
                imgD = round((time.time() - current),3)
                # print("Image delay:", imgD)
                current = time.time()
                for pos in locations:
                    color = img.getpixel((pos,0))
                    if color == (17,17,17):
                        pixelD = round((time.time() - current),3)

                        # print("Pixel delay:", pixelD)
                        current = time.time()
                        pyautogui.click(x=xPos+pos,y=yPos+350)
                        clickD = round((time.time() - current),3)
                        # print("Click delay:", clickD)
                        # print("Total delay:", imgD+pixelD+clickD)
                        break

    window = Tk()
    window.resizable(0,0)
    window.geometry("500x604")
    window.title("Piano Tiles")
    Button(text="Target", command=GetWindow, bg="red").pack(side=LEFT, anchor=N, fill=Y, ipadx=25)
    w = Canvas(window, width=500, height=600)
    w.create_rectangle((2,2,400,600),fill="green")
    w.pack(side=TOP,anchor=E)
    window.wm_attributes("-transparentcolor", "green")
    window.mainloop()


if __name__ == '__main__':
    begin()
