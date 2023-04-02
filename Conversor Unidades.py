def convertir(valor, unidad_origen, unidad_destino):
    # Agrega tu código para convertir las unidades aquí
    pass
def convertir(valor, unidad_origen, unidad_destino):
    if unidad_origen == "metro" and unidad_destino == "pies":
        return valor * 3.28084
    elif unidad_origen == "pies" and unidad_destino == "metro":
        return valor / 3.28084
    elif unidad_origen == "kilogramo" and unidad_destino == "libra":
        return valor * 2.20462
    elif unidad_origen == "libra" and unidad_destino == "kilogramo":
        return valor / 2.20462
    else:
        return None
while True:
    print("\nMenu:")
    print("1. Convertir unidades")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        valor = float(input("Ingrese el valor a convertir: "))
        print("Unidades disponibles: metros, pies, pulgadas, kilogramos, libras")
        unidad_origen = input("Ingrese la unidad de origen: ")
        unidad_destino = input("Ingrese la unidad de destino: ")
        resultado = convertir(valor, unidad_origen, unidad_destino)
        if resultado is not None:
            print("{} {} equivale a {} {}.".format(valor, unidad_origen, resultado, unidad_destino))
        else:
            print("No se pudo realizar la conversión.")
    elif opcion == "2":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
