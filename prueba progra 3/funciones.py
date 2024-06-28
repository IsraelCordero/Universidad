Asientos= ("Asiento común", "Espacio adicional para piernas", "No reclina")
asientoComun=60.000
EspacioAdicionalPiernas=80.000
NoReclina=50.000
asientosDisponibles=[ " A1=Disponible, A2=Disponible, A3=Disponible, A4=Disponible, A5=Disponible, A6=Disponible, A7=Disponible, A8=Disponible, A9=Disponible, A10=Disponible "]
total_asiento_comun=0
total_espacio_adicional=0
total_no_reclina=0
comun_asiento=0
adicional_espacio=0
reclina_no=0


def comprar_pasajes(pasajeros):
    pasajes_a_comprar=int(input("Ingrese la cantidad de pasajes que desea comprar"))
    while pasajes_a_comprar > 198:
        print("Hay un maximo de 198 asientos disponibles, intente nuevamente ")
        pasajes_a_comprar=int(input("Ingrese la cantidad de pasajes que desea comprar"))
    while pasajes_a_comprar < 0:
        print("ingrese un numero valido ")
        pasajes_a_comprar=int(input("Ingrese la cantidad de pasajes que desea comprar"))
    
        print("1) Asiento Comun 2)Espacion adicional para piernas 3)No reclina")
        seleccion_asiento=int(input("Seleccione su tipo de asiento "))
        if seleccion_asiento==1:
            comun_asiento=+1
            total_asiento_comun + asientoComun
            print("Asiento comun: $60.000 seleccionado ")   
        elif seleccion_asiento==2:
            adicional_espacio=+1
            total_espacio_adicional+EspacioAdicionalPiernas
            print("Espacion adicional para piernas: $80.000 seleccionado ")
        elif seleccion_asiento==3:
            reclina_no=+1
            total_no_reclina+NoReclina
            print("No reclina: $50.000 seleccionado ")   
        else:
            print("Ingrese una opcion valida") 

        print(asientosDisponibles)
        eleccionAsientos=input("Escoge un asiento ")
        if eleccionAsientos in asientosDisponibles:
            print("Asiento Seleccionado ")
            asientosUsados=[eleccionAsientos]
        elif eleccionAsientos in asientosUsados:
            print("Asiento no disponible X ")
        else:
            print("ingrese un asiento valido ")


    rut_pasajero=int(input("por favor ingrese su RUT sin guion ni puntos "))
    while "-" in rut_pasajero:
        print("Ingrese el rut sin guion por favor ")
        rut_pasajero=int(input("por favor ingrese su RUT sin guion ni puntos "))
    while "." in rut_pasajero:
        print("ingrese el rut sin puntos por favor ") 
        rut_pasajero=int(input("por favor ingrese su RUT sin guion ni puntos "))  
    
    pasajeros.append=[{
        "Rut Pasajero": rut_pasajero,
        "Asientos Seleccionados": seleccion_asiento,
    }]
    print("operacion realizada correctamente ")

def mostrar_ubicaciones_disponibles(pasajeros):
    print(f"Asientos disponibles:  {asientosDisponibles}")
    


def listado_pasajeros(pasajeros):
    print("Listado de pasajeros")
    for i in pasajeros:
        print(i)
        

def buscar_pasajero(pasajeros):
    rut_para_buscar_pasajero=int(input("ingrese el rut del pasajero que desea buscar "))
    if rut_para_buscar_pasajero in pasajeros:
        print(f"Rut encontrado {rut_para_buscar_pasajero}")
    else:
        print("Rut no encontrado ")

def reasignar_asiento(pasajeros):
    print()

def mostrar_ganancias_totales(pasajeros):
    print(f"""
    TIPO ASIENTO                              CANTIDAD                         TOTAL
    ASIENTO COMUN            $60.000          {comun_asiento}                 ${total_asiento_comun}
    ESPACIO PARA PIERNAS     $80.000          {adicional_espacio}             ${total_espacio_adicional}
    NO RECLINA               $50.000          {reclina_no}                    ${total_no_reclina}
    TOTAL
          
""")