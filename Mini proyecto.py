class ExploradorRecursivo:

    @staticmethod
    def imprimir_arbol(sistema: dict, nivel: int = 0):
        for nombre, contenido in sistema.items():
            indentacion = "  " * nivel

            # CASO RECURSIVO: Si el contenido es un diccionario, es una carpeta
            if isinstance(contenido, dict):
                print(f"{indentacion}📁 {nombre}/")
                ExploradorRecursivo.imprimir_arbol(contenido, nivel + 1)

            # CASO BASE: Si no es un diccionario, es un archivo
            else:
                print(f"{indentacion}📄 {nombre} ({contenido})")

    @staticmethod
    def buscar_archivo(sistema: dict, nombre: str, ruta_actual: str = "") -> str:
        for clave, contenido in sistema.items():
            nueva_ruta = f"{ruta_actual}/{clave}" if ruta_actual else clave

            # CASO RECURSIVO: Si es una carpeta, buscamos dentro de ella
            if isinstance(contenido, dict):
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido, nombre, nueva_ruta
                )

                if resultado is not None:
                    return resultado

            # CASO BASE: Si es un archivo y coincide con el nombre
            elif clave == nombre:
                return nueva_ruta

        # CASO BASE: No se encontró el archivo
        return None

    @staticmethod
    def contar_archivos(sistema: dict) -> int:
        total = 0

        for clave, contenido in sistema.items():

            # CASO RECURSIVO: Si es una carpeta, contamos su contenido
            if isinstance(contenido, dict):
                total += ExploradorRecursivo.contar_archivos(contenido)

            # CASO BASE: Si es un archivo, sumamos uno
            else:
                total += 1

        return total


# CÓDIGO DE PRUEBA

sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}

print("=== 1. IMPRIMIR ÁRBOL DE DIRECTORIOS ===")
ExploradorRecursivo.imprimir_arbol(sistema_archivos)

print("\n=== 2. BÚSQUEDA DE ARCHIVOS ===")
print("Ruta de perro.jpg:", ExploradorRecursivo.buscar_archivo(sistema_archivos, "perro.jpg"))
print("Ruta de apuntes.txt:", ExploradorRecursivo.buscar_archivo(sistema_archivos, "apuntes.txt"))
print("Ruta de archivo_inexistente.txt:", ExploradorRecursivo.buscar_archivo(sistema_archivos, "no_existe.txt"))

print("\n=== 3. CONTEO DE ARCHIVOS ===")
total = ExploradorRecursivo.contar_archivos(sistema_archivos)
print(f"Total de archivos encontrados: {total}")

