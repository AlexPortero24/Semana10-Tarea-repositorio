
# se Añadieron datos de las 4 semanas completas del mes de Febrero del 2025
# se añadio comentarios de sus funcionalidad en las lineas del codigo
# se realizo las especificaciones de la Tarea de la semana 13
# se puso la funcion que calcule la temperatura promedio de una ciudad durante un período de tiempo
# La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas

# Datos tomados de METRORED clima y de Toempo3.com, temperaturas por ciudad, día y semana

#Aquí se declara una lista de listas que almacena las temperaturas en tres dimensiones (temperaturas = [ ).
temperaturas = [
    [   # Quito, aqui se almacenan datos de las tempenraturas por dias.
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Guayaquil, aqui se almacenan datos de las tempenraturas por dias.
        [   # Semana 1
            {"day": "Lunes", "temp": 30},        # "day" se refiere a los dias y "temp" se refiere a los grados Celsius (°C).
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Cuenca, aqui se almacenan datos de las tempenraturas por dias.
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ]
    ]
]


# Función para calcular los promedios de temperatura de una ciudad por semana y mensual

def calcular_promedios(ciudad):
    ciudad = ciudad.capitalize()  # en esta linea se convierte la primera letra en mayúscula y el resto en minúsculas para aceptar cualquier formato de entrada

    if ciudad in ciudades:  # aqui verifica si la ciudad ingresada está en la lista de ciudades disponibles
        indice = ciudades.index(ciudad)  # aqui se obtiene el índice de la ciudad en la lista
        temperaturas_ciudad = temperaturas[indice]  # aqui se elecciona los datos de temperatura de la ciudad elegida

        # Aqui se va ha calcular el promedio semanal que corresponda
        for semana_idx, semana in enumerate(temperaturas_ciudad):  # semana_idx Recorre cada semana de la ciudad
            suma_semanal = sum(dia["temp"] for dia in
                               semana)  # A  qui se realiza la suma de las temperaturas de los 7 días de una semana
            promedio_semanal = suma_semanal / len(
                semana)  # Se calculara el promedio semanal dividiendo la suma total por 7 por los dias de la semana.
            print(
                f"Semana {semana_idx + 1}: {promedio_semanal:.2f} °C")  # por ultimo se imprime el promedio semanal con dos decimales

        # Ahora vamos ha alcular el promedio mensual que corresponda.
        suma_total = sum(dia["temp"] for semana in temperaturas_ciudad for dia in
                         semana)  # Se ahara la suma todas las temperaturas del mes
        promedio_mensual = suma_total / (
                    4 * 7)  # en esta linea vamos ha dividir la suma total entre 28 porque sin 4 semana y 7 dias(4 semanas * 7 días) esto es necesario para obtener el promedio mensual
        print(
            f"\nEl promedio mensual de temperatura en {ciudad} es: {promedio_mensual:.2f} °C")  # por ultimo vamos a imprime el promedio mensual

    else:
        print(
            "Ciudad no encontrada. Elija entre Quito, Guayaquil o Cuenca.")  # se va ha mostrar un mensaje de error si la ciudad no está en la lista analizada.


# Lista de ciudades disponibles en este caso solo son tres y 4 semanas cada una
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# En este apartado vamos a pedir al usuario elejir la ciudada para obtener los promedios de cada semna y del mes.
ciudad_usuario = input(
    "Ingrese una ciudad (Quito, Guayaquil, Cuenca): ").strip()  # Pide al usuario una ciudad y elimina espacios innecesarios
calcular_promedios(ciudad_usuario)  # Llama a la función para calcular los promedios de la ciudad ingresada
