import cv2
from vision.camera import iniciar_camara
from vision.detector import detectar_objeto
from vision.tracker import obtener_centro

cap = iniciar_camara()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    contornos = detectar_objeto(frame)

    for cnt in contornos:
        area = cv2.contourArea(cnt)

        if area > 500:
            x, y, w, h, cx, cy = obtener_centro(cnt)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)

            print(f"Posición: {cx}, {cy}")

    cv2.imshow("Sistema de seguimiento", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()