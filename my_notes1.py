# Tarea: Trabajo con Archivos de Texto en Python
# En esta tarea, realizaremos operaciones de lectura y escritura en archivos de texto en Python.

# ----------------- Escritura de Archivo de Texto -----------------

# Definimos el nombre del archivo donde se guardarán las notas
file_name = "my_notes.txt"

# Abrimos el archivo en modo escritura ('w'), lo que sobrescribirá cualquier contenido anterior
file_escritura = open(file_name, "w", encoding="utf-8")

# Escribimos al menos tres líneas de notas personales en el archivo
file_escritura.write("línea 1: Hola, me llamo Alex. Ejemplo de escritura.\n")
file_escritura.write("línea 2: Este es el ejemplo de la tarea.\n")
file_escritura.write("línea 3: Aprendiendo a manejar archivos en Python.\n")

# Cerramos el archivo después de escribir para liberar recursos
file_escritura.close()

# ----------------- Lectura de Archivo de Texto -----------------

# Abrimos el archivo en modo lectura ('r')
file_lectura = open(file_name, "r", encoding="utf-8") # Se usa encoding="utf-8" para asegurar compatibilidad con caracteres especiales

# Posicionamos el cursor al inicio del archivo por seguridad
file_lectura.seek(0)

# Leemos y mostramos cada línea del archivo utilizando readline()
print("\nContenido línea por línea usando readline():")
linea_1 = file_lectura.readline()
linea_2 = file_lectura.readline()
linea_3 = file_lectura.readline()

# Imprimimos el contenido de cada línea eliminando los saltos de línea adicionales
print("Línea 1:", linea_1.strip())
print("Línea 2:", linea_2.strip())
print("Línea 3:", linea_3.strip())

# Cerramos el archivo después de leerlo para liberar recursos
file_lectura.close()
