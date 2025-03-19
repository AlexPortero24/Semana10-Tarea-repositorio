def calcular_descuento(monto: float, porcentaje_descuento: float = 10.0) -> float:
    """
    Calcula el descuento sobre un monto dado.
    :parametros monto: Monto total de la compra.
    :parametros porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """ # expicacion de la funcion en si se pone dos parametros y despues se retorna el calculo del descuento,
    if monto < 0:
        return 0.0  # Devolver 0 si el monto es negativo
    
    descuento = (monto * porcentaje_descuento) / 100 # esta es la formula para calcular el descuento
    return descuento # aqui se retorna el monto total del descuento...

# se solicita al usuario cual es el monto que debe pagar o calcenlar, ademas se verifica que el dato que nos de sea valido(positivo)
while True:
    try:
        monto_compra = float(input("Ingrese el monto total de la compra: ")) # el dato de entrada sera convertido a float (decimales)
        if monto_compra < 0:
            print("El monto es negativo, no es valido. Porfavor ingrese un monto positivo.") # se imprime un error si el monto es negativo o no valido
            continue # aqui vuelve a que el usuario ingrese un monto valido
        break # se usa break para salir del bucle si el monto es valido
    except ValueError:
        print("Entrada no válida . Porfavor ingrese un número.") # si la entrada no es un numero ocurre un error

# Aqui vamos a solicitar el porcentaje de descuento , donde podemos usar decimales
while True:
    try:
        porcentaje = input("Ingrese el porcentaje de descuento ( o presione Enter para usar el predeterminado del 10%): ")
        if porcentaje:
            porcentaje = float(porcentaje) # se convertira la entrada a float para permitir decimales
        else:
            porcentaje = 10.0  # Valor por defecto del descuento sera del 10 % si el usuario presiona enter se calculara el porcentaje predeterminado 
        if porcentaje < 0:
            print("El porcentaje de descuento no puede ser negativo. ingrese un porcentaje valido.")
            continue # se solicita que el porcentaje sea positivo ya que no debe ser negativo.
        break # si el porcentaje es positivo se sale del bucle.
    except ValueError:
        print("Entrada no válida . Porfavor ingrese un número.") # la entrada debe ser un numero 

# Aqui se calcula el descuento usando la funcion y se hace el calculo para obtener el monto final a pagar 
descuento_calculado = calcular_descuento(monto_compra, porcentaje)
monto_final = monto_compra - descuento_calculado # se resta el descuento al monto inicial

# se van imprimir para mostrar los resultados calculados al final del codigo 
print("\nResultados:")
print(f"Monto de la compra fue: {monto_compra:.2f}")# {monto_compra:.2f} se utilizo para usara dos decimales unicamnete y reducir decimales.
print(f" El Porcentaje de descuento aplicado fue de: {porcentaje:.2f}%") # se muestra el porcentaje con dos decimales
print(f"El Descuento aplicado fue del: {descuento_calculado:.2f}") # se mostrara el descuento calculado 
print(f"Monto final a pagar después del descuento es : {monto_final:.2f}") # por ultimo se mostrara el monto final que se debera pagar.