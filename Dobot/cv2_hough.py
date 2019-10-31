import cv2
import numpy as np
import time
import os

locCoords = [
(374, 415, 560, 598),
(372, 228, 559, 418),
(373, 55, 550, 229),
(187, 417, 373, 600),
(184, 229, 374, 415),
(188, 54, 372, 228),
(7, 416, 187, 593),
(9, 229, 187, 417),
(8, 56, 184, 229)
]

def checkPlaced(game):
    os.remove("images/placed.png")

    cam = grabPos()
    time.sleep(2)
    img = cv2.imread("images/placed.png", 0)

    if game.player == "O":
        placedIndx = getAllCircles(img)
    else:
        placedIndx = getAllCrosses(img)

    if placedIndx == 0:
        return 10

    for indx in placedIndx:
        if game.board[indx] == "_":
            return indx


def grabPos():
    cap = cv2.VideoCapture(1)

    ret, frame = cap.read()

    img = cv2.resize(frame, (802, 599))

    cv2.imwrite('images/placed.png', img)
    cap.release()

def getAllCircles(img):

    img = cv2.medianBlur(img, 5)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=50, minRadius=30, maxRadius=70)

    if circles is None:
        return 0

    circles = np.uint16(np.around(circles))
    placedIndx=[]
    for i in circles[0, :]:

        indx=0
        for tup in locCoords:
            if i[0] > tup[0] and i[1] > tup[1] and i[0] < tup[2] and i[1] < tup[3]:
                placedIndx.append(indx)
            indx += 1

    return placedIndx

def getAllCrosses(img):

    placed = [0,0,0,0,0,0,0,0,0]
    grey_img = img

    template = cv2.imread("images/newest_cross.png", 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.4
    loc = np.where(res >= threshold)
    placedIndx=[]
    for pt in zip(*loc[::-1]):
        i = (pt[0]+int((w/2)), pt[1]+int((h/2)))
        indx=0
        for tup in locCoords:
            if i[0] > tup[0] and i[1] > tup[1] and i[0] < tup[2] and i[1] < tup[3]:
                if placed[indx] != 1:
                    placedIndx.append(indx)
                placed[indx] = 1
            indx += 1

    return placedIndx
