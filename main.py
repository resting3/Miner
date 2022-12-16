#import numpy as np
import os
import time
# python3 -m http.server
import keyboard
import pyautogui
import pydirectinput
import pyscreenshot
import asyncio
from skimage.metrics import structural_similarity
import cv2
import numpy as np
import json






def control(file1, file2):
    before = cv2.imread(file1)
    after = cv2.imread(file2)
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between the two images
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print(f"Image Similarity: {score * 100}%")

    a = score * 100
    return a

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1]
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")
    diff_box = cv2.merge([diff, diff, diff])

    # Threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    mask = np.zeros(before.shape, dtype='uint8')
    filled_after = after.copy()

    for c in contours:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.drawContours(mask, [c], 0, (255, 255, 255), -1)
            cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)

print("Benvenuto nel nuovo TecnoMiner \nCurrent Version: 3.1\nUna creazione di Resting")

spacebar = 1


x1 = 690
x2 = 750

a = 0
time.sleep(3)
while True:

    with open("coord.json","r") as f:
        data = json.load(f)
    # intera barra 1050 750 il primo va avanti di 60
    pic = pyscreenshot.grab(bbox=(x1, int(data["x"]), x2, int(data["y"])))
    pic.save("void.png")

    pyautogui.mouseDown(button='left')
    if keyboard.is_pressed('g'):
        pyautogui.mouseUp(button='left')
        pydirectinput.keyUp('shift')
        exit()
    r_control = control("void.png", "base.png")
    if r_control > 70.0:
        spacebar = spacebar + 1
        x1 = x1 + 60
        x2 = x2 + 60
        pyautogui.mouseUp(button='left')
        pydirectinput.press('9')
        pyautogui.mouseDown(button='right')
        pyautogui.sleep(3.5)
        pyautogui.mouseUp(button='right')
        pydirectinput.press(f"{spacebar}")
        pyautogui.mouseDown(button='left')
    if spacebar > 6:
        pyautogui.mouseDown(button='left')
        exit()


















