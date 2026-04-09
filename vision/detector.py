import cv2
import numpy as np

def detectar_objeto(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 120, 70])
    upper = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    contornos, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contornos