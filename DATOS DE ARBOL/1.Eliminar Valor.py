# ArbolBinarioBusqueda

def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None

        # 1. Buscar el nodo
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1 y 2: Sin hijos o con un solo hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: Dos hijos (encontramos el mínimo del subárbol derecho)
            actual = nodo.derecho
            while actual.izquierdo is not None:
                actual = actual.izquierdo
            
            # Reemplazamos el valor y eliminamos el duplicado a la derecha
            nodo.valor = actual.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, actual.valor)

        return nodo