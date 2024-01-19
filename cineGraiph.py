import os

listaAsientos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

#DICCIONARIO DE USUARIOS VACIO
usuarios = {}

#METODO MOSTRAR ASIENTOS
def mostrarAsientos():
    columnas_por_fila = 6

    print("         [PANTALLA]")
    # Imprimir la sala de cine
    for i, asiento in enumerate(listaAsientos, start=1):
        # Agregar una nueva línea después de imprimir cada fila
        if (i - 1) % columnas_por_fila == 0:    
            print()
        # Imprimir el número del asiento
        print(f"{asiento:2}", end=" ")

    print()

#METODO DE RESERVA
def realizarReserva(rutUsuario,asientosSeleccionados):
    #Si el usuario ya tiene registrado el rut agregamos los asientos
    if(rutUsuario in usuarios):
        for asiento in asientosSeleccionados:
            usuarios[rutUsuario]['asientos'].append(asiento)

    else:
        #SOLICITAMOS LOS DATOS DEL PASAJERO EN CASO DE SER NUEVO
        nombreCliente = input("Ingrese su nommbre : \n")
        telefonoCliente = input("Ingrese numero de telefono : \n")
        usuarios[rutUsuario]  = {
            "nombre"  : nombreCliente,
            "telefono": telefonoCliente,
            "asientos": asientosSeleccionados
        }

def ValidarAntesdeReservar(numAsiento):
    # REVISAMOS que el asiento que se desea reservar este disponible
    if numAsiento in listaAsientos:
        # Lo MARCAMOS como ocupado para que si el mismo usuario quiere seguir comprando no pueda elegir 2 veces el mismo asiento
        listaAsientos[numAsiento-1] = "X" 
        return True
    else:
        return False
    
def anularAsiento(rut):
    #Obtenemos los asientos correspondientes al rut del cliente
    asientosReservados = usuarios[rut]['asientos']
    print(f"Asientos que tiene reservados {asientosReservados}")
    asientoAnular = int(input("Ingrese el asiento que desea anular, en caso querer cancelar ingrese '0':\n"))
    while asientoAnular != 0: 
        if asientoAnular in asientosReservados:
            usuarios[rut]['asientos'].remove(asientoAnular)
            indice = asientoAnular - 1
            listaAsientos[indice] = asientoAnular
        else:
            print("EL ASIENTO QUE SE SELECCIONO NO ESTA RESERVADO!")

        print(f"Asientos que tiene reservados {asientosReservados}")
        asientoAnular = int(input("Ingrese otro asiento si lo desea, en caso querer cancelar ingrese '0':\n"))

# INICIO de la aplicacion y su MENU
print('***BIENVENIDO A CINE GRAIPH***')
menu=(input("1.-Ver Asientos Disponibles.\n2.-Reservar Asiento.\n3.-Anular Asiento.\n0.-Salir.\nIngrese opcion: "))

while menu != '0' :            
    if menu == '1' :
        os.system('cls')
        print('***ASIENTOS DISPONIBLES***')
        mostrarAsientos()
        
    elif menu == '2' :
        os.system('cls')
        print('***RESERVAR ASIENTO***')

        print('***ASIENTOS DISPONIBLES***')
        mostrarAsientos()

        listaAsientosReservar = []
        #PREGUNTO si desea seguir comprando mas asientos
        asientoReserva = int(input("Ingrese un asiento, en caso querer cancelar ingrese '0':\n"))
        while asientoReserva != 0: 
            if ValidarAntesdeReservar(asientoReserva):
                listaAsientosReservar.append(asientoReserva)
            else:
                print("EL ASIENTO QUE SE SELECCIONO NO ESTA DISPONIBLE!")
        
            asientoReserva = int(input("Ingrese otro asiento si lo desea, en caso de no querer ingrese '0':\n"))

        if len(listaAsientosReservar) != 0:    
            rutCliente = input("Ingrese su RUT para la información (sin puntos y Con '-' y digito verificador): \n")

            realizarReserva(rutCliente,listaAsientosReservar)
            
            mostrarAsientos()

            print(usuarios)
                 
    elif menu == '3' :
        os.system('cls')
        print('***ANULAR ASIENTO***')
        sRUT = input('Ingrese su RUT para la información : ')
        
        if sRUT in usuarios :
            anularAsiento(sRUT)
         
        else:
            print("NO EXISTE ESTE RUT EN LOS REGISTROS")

    elif menu == '6':
        print(usuarios)           
    else:
        print("Digite una opcion correcta!!")

    menu=(input("\n1.-Ver Asientos Disponibles.\n2.-Reservar Asiento.\n3.-Anular Asiento.\n0.-Salir.\nIngrese opcion: "))

if menu == '0' :
    os.system('cls')
    print("Se a terminado la aplicacion!!!")