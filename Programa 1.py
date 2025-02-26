# Definimos una matriz 3x3 de números
matriz = [
    [4, 9, 3],
    [2, 8, 5],
    [6, 1, 7]
]

# Valor a encontrar
valor_encontrar = 8

# Variables para almacenar la posición del valor
fila_encontrar = -1
columna_encontrar = -1

# Función para encontrar el valor en la matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_encontrar:
            fila_encontrar = fila  # Aquí se asigna la fila correcta
            columna_encontrar = columna
            break  # Para salir del bucle interno al encontrar el valor
    if fila_encontrar != -1:
        break  # Para salir del bucle externo también si se encontró el valor

# Mensaje de resultado
if fila_encontrar != -1:
    print(f"Se encontró el valor {valor_encontrar} en la fila {fila_encontrar} y en la columna {columna_encontrar}")
else:
    print(f"{valor_encontrar} no se encontró en la matriz.")


