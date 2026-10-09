#2

def contar_vocales(texto):
    # Caso Base
    if texto == "":
        return 0
    
    # Caso Recursivo
    es_vocal = 1 if texto[0].lower() in "aeiou" else 0
    return es_vocal + contar_vocales(texto[1:])

print(contar_vocales("Recursividad"))  # 5