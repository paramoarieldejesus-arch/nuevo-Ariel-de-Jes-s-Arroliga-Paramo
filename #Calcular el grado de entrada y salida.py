#Calcular el grado de entrada y salida 
def calcular_grados(grafo):
    for nodo in grafo:
        entrada = 0
        salida = len(grafo[nodo])

        for vecinos in grafo.values():
            for vecino in vecinos:
                if vecino == nodo:
                    entrada += 1

        print(nodo, "- Entrada:", entrada, "| Salida:", salida)


# Crear un grafo dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

calcular_grados(grafo)
