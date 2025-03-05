# Datos tomados de METRORED clima, temperaturas por ciudad, dia y semana

temperaturas = [
    [   # Quito
        [   # Semana 1 (3 al 9 de marzo)
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1 (3 al 9 de marzo)
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1 (3 al 9 de marzo)
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ]
    ]
]

# Nombres de las ciudades que fueron elegidas para la tarea
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")