#3 

def imprimir_patron(n):
    # Caso Base
    if n == 0:
        return
    
    # Caso Recursivo
    imprimir_patron(n - 1)
    print("*" * n)

imprimir_patron(3)
# Salida:
# *
# **
# ***