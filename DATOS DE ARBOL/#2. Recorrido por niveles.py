# Recorrido por niveles

from collections import deque

def recorrido_niveles(self):
    """Retorna una lista con los valores del árbol recorridos por niveles (BFS)."""
    if self.raiz is None:
        return []
    
    resultado = []
    cola = deque([self.raiz])  # Inicializamos la cola con la raíz
    
    while cola:
        nodo_actual = cola.popleft()  # Sacamos el primer elemento de la cola
        resultado.append(nodo_actual.valor)
        
        # Si tiene hijo izquierdo, lo agregamos a la cola
        if nodo_actual.izquierdo is not None:
            cola.append(nodo_actual.izquierdo)
            
        # Si tiene hijo derecho, lo agregamos a la cola
        if nodo_actual.derecho is not None:
            cola.append(nodo_actual.derecho)
            
    return resultado