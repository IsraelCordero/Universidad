import funciones as fn
pasajeros = []
print("bienvenido a la linea aerea Flash ")
while True:
    print("""
    1) Comprar pasajes
    2) Mostrar ubicaciones disponibles
    3) Ver listado de pasajeros
    4) Buscar pasajero
    5) Reasignar asiento
    6) Mostrar ganancias totales 
    7) Salir
""")
    op=int(input("Ingrese una opcion "))
    if op==7:
        print("Ha salido del programa ")
        break
    if op==1:
        fn.comprar_pasajes(pasajeros)
    elif op==2:
        fn.mostrar_ubicaciones_disponibles(pasajeros)
    elif op==3:
        fn.listado_pasajeros(pasajeros)
    elif op==4:
        fn.buscar_pasajero(pasajeros)
    elif op==5:
        fn.reasignar_asiento(pasajeros)
    elif op==6:
        fn.mostrar_ganancias_totales(pasajeros)
    else:
        print("Ingrese una opcion valida ")

