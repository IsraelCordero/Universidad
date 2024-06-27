CARGOS= ["ceo", "desarrollador", "analista de datos"]

def registrarTrabajador(trabajadores):
    nombre=input("ingrese nombre y apellido del trabajador ").lower()
    cargo=input("ingrese cargo del trabajador CEO/DESARROLLADOR/ANALISTA DE DATOS ").lower()
    while cargo not in CARGOS:
        print("ingrese un cargo valido ")
        cargo=input("ingrese cargo del trabajador CEO/DESARROLLADOR/ANALISTA DE DATOS ").lower()
    sueldoBruto=int(input("ingrese sueldo bruto "))
    descSalud= sueldoBruto*0.07
    descAFP= sueldoBruto*0.12
    liquidoAPagar= sueldoBruto-descAFP-descSalud
    
    trabajadores.append({
        "nombre": nombre,
        "cargo": cargo,
        "sueldo bruto": sueldoBruto,
        "descuento salud": descSalud,
        "descuento afp": descAFP,
        "liquido a pagar": liquidoAPagar,
    })
    
    
def listarTrabajador(trabajadores):
     print("Lista de trabajadores ")
     for trabajador in trabajadores:
        print(trabajador)

def ImprimirPlanillaSueldos(trabajadores):
    cargoSeleccionado=input("ingrese el cargo que desea imprimir o presione ENTER para imprimirlos todos ").lower()
    if cargoSeleccionado=="":
        trabajadores_a_imprimri=trabajadores
        nombreArchivo="planilla_todos_.txt"
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimri=[]
        for trabajador in trabajadores:
            if trabajador ["cargo"]==cargoSeleccionado:
                trabajadores_a_imprimri.append(trabajador)
        nombreArchivo= f"planilla {cargoSeleccionado}.txt "        
    else:
        print("Cargo no valido ")
        return
    
    with open(nombreArchivo, "w") as archivo:
        for trabajador in trabajadores_a_imprimri:
            archivo.write(f"Nombre y Apellido: {trabajador["nombre"]}\n" )
            archivo.write(f"Cargo: {trabajador["cargo"]}\n" )
            archivo.write(f"Sueldo Bruto: {trabajador["sueldo bruto"]}\n" )
            archivo.write(f"Descuento Salud: {trabajador["descuento salud"]}\n" )
            archivo.write(f"Descuento AFP: {trabajador["descuento afp"]}\n" )
            archivo.write(f"Liquido a Pagar: {trabajador["liquido a pagar"]}\n" )
            