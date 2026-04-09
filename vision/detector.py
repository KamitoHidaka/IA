import cv2
import numpy as np

def detectar_objetivos(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ajusta según tu objetivo real
    lower = np.array([0, 120, 70])
    upper = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # Reducir ruido
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contornos