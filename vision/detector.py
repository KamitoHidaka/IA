from ultralytics import YOLO

modelo = YOLO("yolov8n.pt")  # modelo ligero

def detectar_objetivos(frame):
    resultados = modelo(frame, verbose=False)

    detecciones = []

    for r in resultados:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            detecciones.append((x1, y1, x2, y2, cx, cy))

    return detecciones