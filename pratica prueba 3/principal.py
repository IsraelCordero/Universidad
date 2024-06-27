import funciones as fn
trabajadores =[]

while True:
    print("""
          1. Registrar trabajador
          2. Listar los todos los trabajadores
          3. Imprimir planilla de sueldos
          4. Salir del Programa """)
    opcion=int(input("ingrese una opcion "))  
    if opcion==1:
        fn.registrarTrabajador(trabajadores)
    elif opcion==2:
        fn.listarTrabajador(trabajadores)
    elif opcion==3:
        fn.ImprimirPlanillaSueldos(trabajadores)
    elif opcion==4:
        print(" Ha salido del programa ")
        break
    else:
        print("Opcion no valida seleccione nuevamente ")            
        
    