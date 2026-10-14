#método `es_completo()`

def es_completo(self):
        """Valida si todos los nodos internos tienen exactamente dos hijos."""
        return self._es_completo_rec(self.raiz)

def _es_completo_rec(self, nodo):
        # Si el nodo está vacío, es válido
        if nodo is None:
            return True
        
        # Si es una hoja (sin hijos), es válido
        if nodo.izquierdo is None and nodo.derecho is None:
            return True
        
        # Si tiene ambos hijos, revisamos recursivamente por ambos lados
        if nodo.izquierdo is not None and nodo.derecho is not None:
            return self._es_completo_rec(nodo.izquierdo) and self._es_completo_rec(nodo.derecho)
        
        # Si tiene un solo hijo (uno es None y el otro no), retorna False
        return False