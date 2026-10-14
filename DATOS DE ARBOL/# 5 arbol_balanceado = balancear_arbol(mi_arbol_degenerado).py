# 5.arbol_balanceado = balancear_arbol(mi_arbol_degenerado)

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
            
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado
        
    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

# --- 1. FUNCIÓN BALANCEAR (Va después de las clases) ---
def balancear_arbol(bst):
    elementos = bst.inorden()
    
    def construir_balanceado(lista):
        if not lista:
            return None
        medio = len(lista) // 2
        nodo = NodoArbol(lista[medio])
        nodo.izquierdo = construir_balanceado(lista[:medio])
        nodo.derecho = construir_balanceado(lista[medio+1:])
        return nodo

    nuevo_arbol = ArbolBinarioBusqueda()
    nuevo_arbol.raiz = construir_balanceado(elementos)
    return nuevo_arbol

# --- 2. PRUEBA (Va al final del todo) ---
arbol_degenerado = ArbolBinarioBusqueda()
for val in [1, 2, 3, 4, 5]:
    arbol_degenerado.insertar(val)

arbol_balanceado = balancear_arbol(arbol_degenerado)
print("¡Árbol balanceado con éxito!")