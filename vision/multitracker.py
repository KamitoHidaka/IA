import math

class MultiTracker:
    def __init__(self):
        self.objetos = {}
        self.id_actual = 0

    def actualizar(self, detecciones):
        nuevos_objetos = {}

        for cx, cy in detecciones:
            encontrado = False

            for obj_id, (px, py) in self.objetos.items():
                distancia = math.hypot(cx - px, cy - py)

                if distancia < 60:
                    nuevos_objetos[obj_id] = (cx, cy)
                    encontrado = True
                    break

            if not encontrado:
                nuevos_objetos[self.id_actual] = (cx, cy)
                self.id_actual += 1

        self.objetos = nuevos_objetos
        return self.objetos