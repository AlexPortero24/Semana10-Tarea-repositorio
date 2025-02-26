# voy hacer como ejemplo una calculadora, solo usando (int,bool,float,cadenas de texto o str)
# para la suma 
a = input("introducir primer numero;")
b = input("introducir segundo numero;")

numero1 = float(a)
numero2 = float(b)

suma = numero1 + numero2
if suma.is_integer():
    suma = int(suma)

print(type(suma))
print(suma)

# resta
a = input("introducir primer numero;")
b = input("introducir segundo numero;")

numero1 = float(a)
numero2 = float(b)

resta = numero1 - numero2
if resta.is_integer():
    resta = int(resta)

print(type(resta))
print(resta)

# multiplicacion 
a = input("introducir primer numero;")
b = input("introducir segundo numero;")

numero1 = float(a)
numero2 = float(b)

multiplicacion = numero1 * numero2
if multiplicacion.is_integer():
    multiplicacion = int(multiplicacion)

print(type(multiplicacion))
print(multiplicacion)

# division
a = input("introducir primer numero;")
b = input("introducir segundo numero;")

numero1 = float(a)
numero2 = float(b)

division = numero1 / numero2
if division.is_integer():
    division = int(division)

print(type(division))
print(division)




# Ingresar las 5 notas para el cálculo del promedio
numero1 = float(input("Ingrese el primer número (máximo 10): "))
numero2 = float(input("Ingrese el segundo número (máximo 10): "))
numero3 = float(input("Ingrese el tercer número (máximo 10): "))
numero4 = float(input("Ingrese el cuarto número (máximo 10): "))
numero5 = float(input("Ingrese el quinto número (máximo 10): "))

