# Función para cargar un fragmento del búfer desde la entrada
def cargar_buffer(entrada, inicio, tamano_buffer):
    # Extrae una porción de la entrada desde el índice 'inicio' hasta el tamaño del búfer
    buffer = entrada[inicio : inicio + tamano_buffer]
    # Si la longitud del búfer es menor al tamaño especificado, agrega el carácter "eof"
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    # Devuelve el búfer cargado
    return buffer

# Función para procesar el búfer y extraer lexemas
def procesar_buffer(buffer):
    lexemas = []  # Lista para almacenar los lexemas encontrados
    lexema_actual = ""  # Almacena el lexema que se está construyendo
    for char in buffer:  # Itera sobre cada carácter del búfer
        # Si el carácter es un espacio o el marcador "eof"
        if char.isspace() or char == "eof":
            if lexema_actual:  # Si hay un lexema en construcción, lo agrega a la lista
                lexemas.append(lexema_actual)
                lexema_actual = ""  # Reinicia el lexema actual
            if char == "eof":  # Si encuentra el marcador "eof", detiene el procesamiento
                break
        else:
            # Si el carácter no es un espacio, lo añade al lexema actual
            lexema_actual = lexema_actual + char
    # Devuelve la lista de lexemas encontrados
    return lexemas

# Define la entrada como una lista de caracteres terminada en "eof"
entrada = list("Esto es un ejemplo eof")
inicio = 0  # Puntero inicial para el procesamiento del búfer
tamano_buffer = 10  # Tamaño fijo del búfer
tamano_total = len(entrada)  # Longitud total de la entrada

# Bucle para procesar la entrada en fragmentos de tamaño fijo
while inicio < tamano_total:
    # Carga el siguiente fragmento del búfer
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    # Procesa el búfer para obtener los lexemas
    lexemas = procesar_buffer(buffer)
    # Imprime cada lexema procesado
    for lexema in lexemas:
        print("Lexema procesado:", lexema)
    # Incrementa el puntero para cargar el siguiente fragmento del búfer
    inicio = inicio + tamano_buffer

# Procesa cualquier fragmento restante en el búfer
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
print("Lexema procesado:", procesar_buffer(buffer))



"""
char.isspace() es una función incorporada en Python que pertenece a los objetos de tipo str. 
Se utiliza para verificar si un carácter o cadena contiene únicamente caracteres de espacio 
en blanco. Este método devuelve True si el carácter es un espacio en blanco (como espacio, tabulación o nueva línea) 
y False en caso contrario.
"""