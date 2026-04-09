import mss
import numpy as np
import cv2
import platform

# ===============================
# WINDOWS (pygetwindow)
# ===============================
def capturar_ventana_windows(nombre_ventana):
    import pygetwindow as gw

    ventanas = gw.getWindowsWithTitle(nombre_ventana)

    if len(ventanas) == 0:
        return None

    ventana = ventanas[0]

    if ventana.isMinimized:
        ventana.restore()

    left = ventana.left
    top = ventana.top
    width = ventana.width
    height = ventana.height

    return capturar_area(left, top, width, height)


# ===============================
# LINUX / RASPBERRY (wmctrl)
# ===============================
def obtener_ventana_linux(nombre):
    import subprocess

    resultado = subprocess.check_output("wmctrl -lG", shell=True).decode()

    for linea in resultado.splitlines():
        if nombre.lower() in linea.lower():
            partes = linea.split()
            x = int(partes[2])
            y = int(partes[3])
            w = int(partes[4])
            h = int(partes[5])
            return x, y, w, h

    return None


def capturar_ventana_linux(nombre_ventana):
    coords = obtener_ventana_linux(nombre_ventana)

    if coords is None:
        return None

    x, y, w, h = coords
    return capturar_area(x, y, w, h)


# ===============================
# CAPTURA GENERAL
# ===============================
def capturar_area(left, top, width, height):
    with mss.mss() as sct:
        monitor = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
        }

        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        return frame


# ===============================
# FUNCIÓN PRINCIPAL AUTOMÁTICA
# ===============================
def capturar_ventana(nombre_ventana):
    sistema = platform.system()

    if sistema == "Windows":
        return capturar_ventana_windows(nombre_ventana)
    else:
        return capturar_ventana_linux(nombre_ventana)