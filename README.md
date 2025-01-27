# Simulador de Búfer en Python

Este programa simula el manejo de un búfer de entrada con un tamaño fijo. Es útil para comprender cómo los compiladores procesan datos de manera eficiente mediante fragmentos.

## Descripción

El simulador implementa un sistema de procesamiento de texto por búfer, similar al utilizado en compiladores y analizadores léxicos. El programa lee la entrada en fragmentos de tamaño fijo (10 caracteres) y procesa estos fragmentos para extraer lexemas (palabras).

## Características Principales

- Procesa una cadena de entrada dividiéndola en fragmentos (buffers) de tamaño fijo
- Identifica y extrae "lexemas" (palabras) separados por espacios
- Maneja palabras que quedan divididas entre diferentes búferes
- Utiliza un marcador especial (`eof`) para indicar el final de la entrada
- Visualización paso a paso del proceso de búfer
- Incluye ejemplos predefinidos para demostrar el funcionamiento

## Estructura del Código

El programa está organizado en tres funciones principales:

1. `cargar_buffer(entrada, inicio, tamano_buffer)`:
   - Carga un segmento de la entrada al búfer
   - Rellena con 'eof' si el fragmento es menor que el tamaño del búfer

2. `procesar_buffer(buffer, lexema_incompleto)`:
   - Procesa el contenido del búfer para extraer lexemas
   - Maneja palabras incompletas entre búferes
   - Retorna los lexemas encontrados y cualquier lexema incompleto

3. `main()`:
   - Coordina el proceso completo
   - Maneja la interfaz de usuario
   - Procesa múltiples ejemplos secuencialmente

## Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SergioAle210/Practica-Bufer.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd Practica-Bufer
   ```

3. Ejecuta el simulador:
   ```bash
   python bufer.py
   ```

## Ejemplo de Uso

El programa incluye varios ejemplos predefinidos que demuestran su funcionamiento:

```python
ejemplos = [
    "Esto es un ejemplo",
    "Simulando un búfer de entrada",
    "Python es increíble",
    "Esto es un ejemplo de entrada con eof"
]
```

Para cada ejemplo, el programa:
1. Muestra el contenido actual del búfer
2. Identifica y muestra los lexemas encontrados
3. Proporciona un resumen final de todos los lexemas procesados

## Personalización

Para procesar tu propio texto, puedes modificar la lista `ejemplos` en el código fuente añadiendo nuevas cadenas de texto.

## Requisitos

- Python 3.x
- Módulo `time` (incluido en la biblioteca estándar de Python)

## Visualización

El programa incluye una interfaz de línea de comandos que muestra:
- El contenido actual del búfer
- Los lexemas procesados en tiempo real
- Un resumen final de todos los lexemas encontrados

