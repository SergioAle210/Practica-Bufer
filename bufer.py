# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio : inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer


def procesar_buffer(buffer):

    pass


entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
print("Lexema procesado:", procesar_buffer(buffer))
