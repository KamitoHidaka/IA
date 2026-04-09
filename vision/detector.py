import cv2

# Inicializar sustractor de fondo
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=100,
    varThreshold=50,
    detectShadows=False
)

def detectar_objetivos(frame):
    # Aplicar sustracción de fondo
    mask = fgbg.apply(frame)

    # Limpiar ruido
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Encontrar contornos
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detecciones = []

    for cnt in contornos:
        area = cv2.contourArea(cnt)

        # Filtrar ruido
        if area < 500:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        cx = x + w // 2
        cy = y + h // 2

        detecciones.append((x, y, x+w, y+h, cx, cy))

    return detecciones