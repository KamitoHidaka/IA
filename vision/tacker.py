import cv2

def obtener_centro(contorno):
    x, y, w, h = cv2.boundingRect(contorno)
    cx = x + w // 2
    cy = y + h // 2
    return (x, y, w, h, cx, cy)