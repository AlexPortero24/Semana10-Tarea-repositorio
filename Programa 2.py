#Programa 2: Ordenación de Arreglo Multidimensional
# Definimos una matriz 3x3 de numeros 
# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [8, 2, 5],
    [3, 9, 4],
    [1, 7, 6]
]

 #3.	Implementa una función que ordene una fila específica de la matriz 
# Funcion para ordenar una fila con  Bubble Sort
def bubble_sort_fila(matriz, fila_ordenar):
    fila = matriz[fila_ordenar]  # Obtener la fila específica
    n = len(fila)

    # Algoritmo Bubble Sort
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos

    matriz[fila_ordenar] = fila  # Actualizar la matriz con la fila ordenada


#4.	Muestra la matriz original y la matriz con la fila ordenada.
# Mostrar la matriz original
print("La matriz sin ordenar :")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar en este caso la fila (0)
fila_a_ordenar = 0
bubble_sort_fila(matriz, fila_a_ordenar)

# se muetra la fila (0) ordenada.
print("\nLa fila (0) de la matriz ordenada es :")
for fila in matriz:
    print(fila)
