#Funcion arbol bts 

def suma_elementos_bst(bst):

    def _sumar_rec(nodo):
        if nodo is None:
            return 0
        return nodo.valor + _sumar_rec(nodo.izquierdo) + _sumar_rec(nodo.derecho)
    
    return _sumar_rec(bst.raiz)