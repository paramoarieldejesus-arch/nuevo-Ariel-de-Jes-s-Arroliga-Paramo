
import heapq


class SistemaGPS:
    def __init__(self):
        # Diccionario que almacena las ciudades y sus rutas
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        # Agrega una ciudad si todavía no existe
        if ciudad not in self.grafo:
            self.grafo[ciudad] = []
            return True
        return False

    def agregar_ruta(self, origen, destino, tiempo):
        # Validar que el tiempo sea positivo
        if tiempo <= 0:
            print("El tiempo debe ser mayor que cero.")
            return

        # Crear las ciudades si no existen
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)

        # Comprobar si la ruta ya existe
        for ciudad, minutos in self.grafo[origen]:
            if ciudad == destino:
                print("Esta ruta ya existe.")
                return

        # Agregar la ruta en ambas direcciones
        self.grafo[origen].append((destino, tiempo))
        self.grafo[destino].append((origen, tiempo))

        print("Ruta agregada correctamente.")

    def mostrar_ciudades(self):
        # Mostrar todas las ciudades registradas
        if not self.grafo:
            print("No hay ciudades registradas.")
            return

        print("\n--- CIUDADES Y RUTAS ---")

        for ciudad, rutas in self.grafo.items():
            print(f"\n{ciudad}:")

            if not rutas:
                print("  Sin rutas conectadas.")
            else:
                for destino, tiempo in rutas:
                    print(f"  -> {destino}: {tiempo} minutos")

    def dijkstra(self, origen, destino):
        # Comprobar que las ciudades existan
        if origen not in self.grafo or destino not in self.grafo:
            print("Una o ambas ciudades no existen.")
            return

        # Distancia mínima conocida desde el origen
        distancias = {
            ciudad: float("inf") for ciudad in self.grafo
        }
        distancias[origen] = 0

        # Guardar la ciudad anterior para reconstruir la ruta
        anteriores = {}

        # Cola de prioridad: (tiempo acumulado, ciudad)
        cola = [(0, origen)]

        while cola:
            tiempo_actual, ciudad_actual = heapq.heappop(cola)

            # Ignorar resultados que ya quedaron desactualizados
            if tiempo_actual > distancias[ciudad_actual]:
                continue

            # Si llegamos al destino, podemos terminar
            if ciudad_actual == destino:
                break

            # Revisar las rutas conectadas a la ciudad actual
            for vecino, tiempo in self.grafo[ciudad_actual]:
                nuevo_tiempo = tiempo_actual + tiempo

                if nuevo_tiempo < distancias[vecino]:
                    distancias[vecino] = nuevo_tiempo
                    anteriores[vecino] = ciudad_actual

                    heapq.heappush(
                        cola, (nuevo_tiempo, vecino)
                    )

        # Comprobar si existe una ruta
        if distancias[destino] == float("inf"):
            print("No existe una ruta entre esas ciudades.")
            return

        # Reconstruir el recorrido desde el destino
        ruta = []
        ciudad_actual = destino

        while ciudad_actual != origen:
            ruta.append(ciudad_actual)
            ciudad_actual = anteriores[ciudad_actual]

        ruta.append(origen)
        ruta.reverse()

        # Mostrar los resultados
        print("\n--- RUTA MÁS RÁPIDA ---")
        print("Origen:", origen)
        print("Destino:", destino)
        print("Recorrido:", " -> ".join(ruta))
        print("Tiempo total:", distancias[destino], "minutos")

    def menu(self):
        # Menú principal del sistema
        while True:
            print("\n===== SISTEMA DE NAVEGACIÓN GPS =====")
            print("1. Mostrar ciudades y rutas")
            print("2. Agregar una ciudad")
            print("3. Agregar una ruta")
            print("4. Buscar la ruta más rápida")
            print("5. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.mostrar_ciudades()

            elif opcion == "2":
                ciudad = input("Nombre de la ciudad: ").strip()

                if ciudad:
                    if self.agregar_ciudad(ciudad):
                        print("Ciudad agregada correctamente.")
                    else:
                        print("La ciudad ya existe.")
                else:
                    print("El nombre no puede estar vacío.")

            elif opcion == "3":
                origen = input("Ciudad de origen: ").strip()
                destino = input("Ciudad de destino: ").strip()

                try:
                    tiempo = float(
                        input("Tiempo de recorrido en minutos: ")
                    )

                    if not origen or not destino:
                        print("Los nombres son obligatorios.")
                    elif origen == destino:
                        print("Las ciudades deben ser diferentes.")
                    else:
                        self.agregar_ruta(origen, destino, tiempo)

                except ValueError:
                    print("Debe ingresar un tiempo numérico válido.")

            elif opcion == "4":
                origen = input("Ciudad de origen: ").strip()
                destino = input("Ciudad de destino: ").strip()

                self.dijkstra(origen, destino)

            elif opcion == "5":
                print("Gracias por utilizar el Sistema GPS.")
                break

            else:
                print("Opción inválida. Intente nuevamente.")


# Crear el sistema
gps = SistemaGPS()

# Agregar rutas de ejemplo
gps.agregar_ruta("Managua", "Masaya", 35)
gps.agregar_ruta("Managua", "Granada", 45)
gps.agregar_ruta("Masaya", "Granada", 20)
gps.agregar_ruta("Granada", "Rivas", 60)
gps.agregar_ruta("Masaya", "León", 75)
gps.agregar_ruta("León", "Managua", 50)

# Iniciar el menú
gps.menu()
