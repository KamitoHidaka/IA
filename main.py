import cv2
from vision.screencap import capturar_ventana
from vision.detector import detectar_objetivos
from vision.tracker import obtener_centro
from vision.multitracker import MultiTracker

NOMBRE_VENTANA = "Brave"  # Cambia esto por el nombre de tu ventana

tracker = MultiTracker()

while True:
    frame = capturar_ventana(NOMBRE_VENTANA)

    if frame is None:
        print("Esperando ventana...")
        continue

    contornos = detectar_objetivos(frame)

    detecciones = []

    for cnt in contornos:
        area = cv2.contourArea(cnt)

        if area > 150:
            x, y, w, h, cx, cy = obtener_centro(cnt)

            detecciones.append((cx, cy))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    objetos = tracker.actualizar(detecciones)

    for obj_id, (cx, cy) in objetos.items():
        cv2.putText(frame, f"ID {obj_id}", (cx, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)

    cv2.imshow("Tracking de ventana", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()