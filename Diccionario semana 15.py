# Definir la función para poder llamarla cuando se requiera modificar algo en un futuro
def modificar_informacion_personal(): # la funcion es donde se encasulara los datos del diccionario depues se realizara las operaciones necesarias. 


    # Crear un diccionario con información personal ficticia, en este caso mi informacion.
    # Se crea un diccionario con los datos de la persona (nombre, edad, ciudad, profesión).
    informacion_personal = {
        "nombre": "Alex David",  # Nombre de la persona
        "edad": 23,  # Edad de la persona
        "Ciudad": "Cuenca",  # Ciudad donde vive la persona
        "profesion": "Ingeniero de en TI"  # Profesión de la persona
    }

    # Acceder y modificar el valor de la clave "ciudad"
    # En este paso, cambiamos el valor de la clave "ciudad" de "Cuenca" a "Quito".
    informacion_personal["Ciudad"] = "Quito"  # se modifica la ciudad 

    # Agregar una nueva clave "profesion" si no existe
    # Verificamos si la clave "profesion" está presente en el diccionario.
    # Si no existe, la agregamos con el valor "Estudiante de TI".
    if "profesion" not in informacion_personal:
        informacion_personal["profesion"] = "Estudiante de TI"  # Si no existe, la agregamos
    else:
        # Si ya existe, la modificamos a "Diseñador Gráfico".
        informacion_personal["profesion"] = "Estudiante de TI"  # Modificamos la profesión

    # Verificar si la clave "telefono" existe en el diccionario
    # Si la clave "telefono" no está en el diccionario, la agregamos con un número ficticio.
    if "telefono" not in informacion_personal:
        informacion_personal["telefono"] = "+593 0777 777 777"  # Si no existe, la agregamos con un número de telefono ficticio

    # Eliminar la clave "edad" del diccionario
    # En este paso, eliminamos la clave "edad" .
    del informacion_personal["edad"]  # Eliminamos la clave "edad"

    # Imprimir el diccionario final
    # Finalmente, mostramos el diccionario con todas las modificaciones que hemos hecho hasta ahora.
    print(informacion_personal)  # Muestra el diccionario con las modificaciones realizadas

# Llamar a la función para ejecutar las operaciones
# Aquí estamos ejecutando la función que definimos anteriormente para ver el resultado final.
modificar_informacion_personal()
