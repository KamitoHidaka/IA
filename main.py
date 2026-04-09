import cv2
from vision.screencap import capturar_ventana
from vision.detector import detectar_objetivos, fgbg
from vision.multitracker import MultiTracker

NOMBRE_VENTANA = "Brave"

tracker = MultiTracker()

while True:
    frame = capturar_ventana(NOMBRE_VENTANA)

    if frame is None:
        print("Esperando ventana...")
        continue

    # Obtener detecciones (ya vienen con bounding box + centro)
    detecciones_raw = detectar_objetivos(frame)

    detecciones = []

    for x1, y1, x2, y2, cx, cy in detecciones_raw:
        detecciones.append((cx, cy))

        # Dibujar bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        # Dibujar centro
        cv2.circle(frame, (cx, cy), 4, (0,0,255), -1)

    # Tracking
    objetos = tracker.actualizar(detecciones)

    for obj_id, (cx, cy) in objetos.items():
        cv2.putText(frame, f"ID {obj_id}", (cx, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    # Mostrar frame
    cv2.imshow("Tracking de ventana", frame)

    # 🔧 DEBUG: mostrar máscara de movimiento
    mask_debug = fgbg.apply(frame)
    cv2.imshow("Movimiento (mask)", mask_debug)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()