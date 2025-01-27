from time import sleep

def cargar_buffer(entrada, inicio, tamano_buffer):
    """
    Carga un segmento del búfer con un tamaño fijo desde la entrada.
    Si la entrada restante es menor que el tamaño del búfer, se rellena con 'eof'.
    """
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer += ['eof'] * (tamano_buffer - len(buffer))
    return buffer

def procesar_buffer(buffer, lexema_incompleto):
    """
    Procesa el búfer para extraer y devolver lexemas (palabras).
    Maneja palabras partidas utilizando lexema_incompleto.
    """
    lexemas = []
    lexema = lexema_incompleto  # Inicia con el lexema incompleto, si existe

    for char in buffer:
        if char.isspace() or char == 'eof':  # Separar palabras
            if lexema:  # Si hay un lexema acumulado, agregarlo
                lexemas.append(lexema)
                lexema = ""
            if char == 'eof':  # Detener si se encuentra 'eof'
                break
        else:
            lexema += char

    return lexemas, lexema  # Retornar los lexemas y cualquier palabra incompleta

def imprimir_bienvenida():
    print("=" * 50)
    print("\tSimulador de Búfer de Entrada\n")
    print("Este programa procesa ejemplos directamente desde el código.\n")
    print("Tamaño del búfer: 10 caracteres\n")
    print("Presiona Enter para comenzar...")
    print("=" * 50)
    input()

def main():
    imprimir_bienvenida()

    ejemplos = [
        "Esto es un ejemplo",
        "Simulando un búfer de entrada",
        "Python es increíble",
        "Esto es un ejemplo de entrada con eof"
    ]

    for idx, linea in enumerate(ejemplos, start=1):
        entrada = list(linea.strip())
        entrada.append('eof')  # Añadir eof como centinela

        print(f"\nProcesando ejemplo {idx}: {linea.strip()}\n")
        inicio = 0
        tamano_buffer = 10

        lexemas_acumulados = []  # Para almacenar todos los lexemas de una línea
        lexema_incompleto = ""   # Para manejar palabras divididas entre búferes

        while inicio < len(entrada):
            buffer = cargar_buffer(entrada, inicio, tamano_buffer)
            lexemas, lexema_incompleto = procesar_buffer(buffer, lexema_incompleto)

            print(f"Buffer: {''.join(buffer)}")
            for lexema in lexemas:
                print(f"Lexema procesado: {lexema}")
                lexemas_acumulados.append(lexema)

            inicio += tamano_buffer
            sleep(0.5)  # Simulación de tiempo de procesamiento

        # Agregar lexema incompleto si existe al final del procesamiento
        if lexema_incompleto:
            lexemas_acumulados.append(lexema_incompleto)

        # Imprimir todos los lexemas procesados de una línea al final
        print("\nResumen de lexemas procesados en este ejemplo:")
        for lexema in lexemas_acumulados:
            print(f"Lexema procesado: {lexema}")

    print("\nProcesamiento completo. ¡Gracias por usar el simulador!")

if __name__ == "__main__":
    main()
