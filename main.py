import numpy as np
import cv2
import pyautogui
import time
import pytesseract


pyautogui.PAUSE = 0.01

def getTextFromImage(image)-> str:
    return (pytesseract.image_to_string(image, lang='eng'))


def typeString(string: str):
    for i in range(len(string)):
        pyautogui.press(string[i])

def main():
    print("running script...")
    time.sleep(3)
    string = "now that you know how to type with all ten fingers, lets work on your speed and then move on to other keys"

    typeString(string)


if __name__ == "__main__":
    main()

