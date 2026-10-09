#1

def multiplicar(a, b):
    # Caso Base
    if b == 0:
        return 0
    # Caso Recursivo
    return a + multiplicar(a, b - 1)

print(multiplicar(5, 4))  # 20