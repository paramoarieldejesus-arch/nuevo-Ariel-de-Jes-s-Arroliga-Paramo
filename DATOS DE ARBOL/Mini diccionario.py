class NodoPalabra:
    def __init__(self, palabra, definicion):
        self.palabra = palabra.lower()
        self.definicion = definicion
        self.izquierdo = None
        self.derecho = None

class DiccionarioBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra, definicion):
        if self.raiz is None:
            self.raiz = NodoPalabra(palabra, definicion)
        else:
            self._insertar_rec(self.raiz, palabra.lower(), definicion)

    def _insertar_rec(self, nodo, palabra, definicion):
        if palabra < nodo.palabra:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoPalabra(palabra, definicion)
            else:
                self._insertar_rec(nodo.izquierdo, palabra, definicion)
        elif palabra > nodo.palabra:
            if nodo.derecho is None:
                nodo.derecho = NodoPalabra(palabra, definicion)
            else:
                self._insertar_rec(nodo.derecho, palabra, definicion)
        else:
            nodo.definicion = definicion  # Actualiza si ya existe

    def buscar(self, palabra):
        return self._buscar_rec(self.raiz, palabra.lower())

    def _buscar_rec(self, nodo, palabra):
        if nodo is None:
            return None
        if nodo.palabra == palabra:
            return nodo.definicion
        elif palabra < nodo.palabra:
            return self._buscar_rec(nodo.izquierdo, palabra)
        else:
            return self._buscar_rec(nodo.derecho, palabra)

    def buscar_por_prefijo(self, prefijo):
        resultado = []
        self._prefijo_rec(self.raiz, prefijo.lower(), resultado)
        return resultado

    def _prefijo_rec(self, nodo, prefijo, resultado):
        if nodo is not None:
            self._prefijo_rec(nodo.izquierdo, prefijo, resultado)
            if nodo.palabra.startswith(prefijo):
                resultado.append((nodo.palabra, nodo.definicion))
            self._prefijo_rec(nodo.derecho, prefijo, resultado)

    def mostrar_todo(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append((nodo.palabra, nodo.definicion))
            self._inorden_rec(nodo.derecho, resultado)


# ================= EJEMPLO DE PRUEBA =================
if __name__ == "__main__":
    diccionario = DiccionarioBST()

    # 1. Cargar palabras base
    palabras = [
        ("algoritmo", "Secuencia de pasos para resolver un problema."),
        ("bucle", "Instrucción que se repite varias veces."),
        ("clase", "Plantilla para crear objetos en POO."),
        ("dato", "Información procesada por un sistema."),
        ("funcion", "Bloque de código reutilizable."),
        ("git", "Control de versiones."),
        ("variable", "Espacio de memoria para almacenar valores.")
    ]

    for p, d in palabras:
        diccionario.insertar(p, d)

    # 2. Probar Búsqueda Exacta
    print("--- Búsqueda Exacta ---")
    termino = "git"
    print(f"'{termino}': {diccionario.buscar(termino)}")

    # 3. Probar Búsqueda por Prefijo (Autocompletar)
    print("\n--- Búsqueda por Prefijo ('bu') ---")
    for p, d in diccionario.buscar_por_prefijo("bu"):
        print(f" - {p.capitalize()}: {d}")

    # 4. Ver Diccionario Ordenado Alfabéticamente (Inorden)
    print("\n--- Diccionario Completo (Ordenado) ---")
    for p, d in diccionario.mostrar_todo():
        print(f" - {p.capitalize()}: {d}")