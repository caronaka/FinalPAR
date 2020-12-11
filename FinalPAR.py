'''
Consignas

Usted ha sido contratado para realizar el software de una empresa de taxis para gestionar la facturación.
El programa debe cumplir con los siguientes requisitos:

1)Deberá tener un menú principal con las acciones disponibles.
2)Permitir la búsqueda de un cliente por su nombre (parcial o total) , mostrando todos sus datos.
3)Permitir obtener el total de usuarios por empresa, y todos sus datos.
4)Permitir obtener el total de dinero en viajes por nombre de empresa. Ejemplo:
5)Permitir obtener cantidad total de viajes realizados y monto total por documento, y mostrar los datos del empleado
y los viajes. Ejemplo:
6)Además se requiere que el sistema guarde las consultas en un archivo .log. Por ejemplo:

7) El csv que se cargue se considerará válido si:
Documento tiene entre 7 y 8 caracteres numéricos de largo
No hay campos vacios
Email contiene un @ y un .
Precio contiene dos decimales

'''
import csv


'''
El csv que se cargue se considerará válido si:
❏ Documento tiene entre 7 y 8 caracteres numéricos de largo
❏ No hay campos vacios
❏ Email contiene un @ y un .
❏ Precio contiene dos decimales

'''


def valida_entero(numero):
    try:
        entero = int(numero)
        return True
    except:
        return False

def valida_float(numero):
    try:
        float_num = float(numero)
        #print("True")
        return True
    except:
        #print("F")
        return False

#valida_float("555.222")



def validarCsvClientes(archivo):
    #campos= ["Nombre","Dirección","Documento","Fecha Alta","Correo Electrónico","Empresa" ]
    with open (archivo, 'r',encoding="utf8") as f:
        archivo_csv = csv.reader(f)
        next(archivo_csv) #saltea encabezado

        for linea in archivo_csv:
            #print(linea[0])
            for campo in linea:
                if campo == "":
                    print(f"\nError en archivo de Clientes. No puede haber campos vacios en la linea {linea}.")
                    return False

            if (len(linea[2]) < 7 ) or (len(linea[2]) > 8 ):
                print(f"\nError en archivo de Clientes. Documento de {linea[0]} debe tener entre 7 y 8 caracteres.")
                return False

            elif valida_entero(linea[2]) == False:
                print(f"\nError en archivo de Clientes. Documento de {linea[0]} debe tener solo caracteres numericos.")
                return False

            elif "@" not in linea[4] or "." not in linea[4]:
                print(f"\nError en archivo de Clientes. Correo electronico de {linea[0]} debe tener @ y .")
                return False

        #print("El archivo esta correcto.\n")
        return True

#validarCsvClientes("Clientes.csv")


def validarCsvViajes(archivo):
    #campos= ["Documento","fecha","monto" ]
    with open (archivo, 'r',encoding="utf8") as f:
        archivo_csv = csv.reader(f)
        next(archivo_csv)

        for linea in archivo_csv:

            precio_separado = linea[2].split(".") #separo la parte entera de la decimal del campo MONTO

            for campo in linea:
                if campo == "":
                    print(f"\nError en archivo de Viajes. No puede haber campos vacios  en la linea {linea}.")
                    return False

            if (len(linea[0]) < 7 ) or (len(linea[0]) > 8 ):
                print(f"\nError en archivo de Viajes. Documento {linea[0]} debe tener entre 7 y 8 caracteres.")
                return False

            elif valida_entero(linea[0]) == False:
                print(f"\nError en archivo de Viajes. Documento {linea[0]} debe tener solo caracteres numericos.")
                return False

            elif valida_float(linea[2]) == False:
                print(f"\nError en archivo de Viajes. Monto {linea[2]} debe ser tipo float.")
                return False


            elif len(precio_separado) == 2:
                    if len(precio_separado[1]) != 2:
                        print(f"\nError en archivo de Viajes. El monto del documento {linea[0]} debe tener dos decimales.")
                        return False


            elif len(precio_separado) < 2:
                print(f"\nError en archivo de Viajes. El monto del documento {linea[0]} debe tener 2 decimales separados por punto.")
                return False



        #print("El archivo esta correcto.\n")
        return True


#validarCsvViajes("viajes.csv")



def busquedaCliente():

    try:
        archivo = input("Ingrese el nombre del archivo de clientes sin extension: ")+".csv"
        campos = ["Nombre","Dirección","Documento","Fecha Alta","Correo Electrónico","Empresa"]

        if validarCsvClientes(archivo) == False:
            return

        else:

            with open(archivo, 'r',encoding="utf8") as clientesfile:
                clientescsv = csv.DictReader(clientesfile)

                cliente_buscado = input("Ingrese nombre total/parcial buscado: ")

                cliente = next(clientescsv, None)

                total_coincidencias = []

                print("----------------------------------------------------------------------------")
                print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]")

                while cliente:

                    while cliente and (cliente_buscado.lower() in cliente['Nombre'].lower()) :

                        print(f"[{cliente[campos[0]]}, {cliente[campos[1]]}, {cliente[campos[2]]}, {cliente[campos[3]]}, {cliente[campos[4]]}, {cliente[campos[5]]}]")

                        total_coincidencias.append(cliente)

                        cliente = next(clientescsv, None)
                    cliente = next(clientescsv, None)

                if len(total_coincidencias) == 0:
                    print("\nNo se encontraron coincidencias en la busqueda. Recuerde respetar las tildes.")
                    return

    except IOError:
        print("\nHubo un error al abrir el archivo/Archivo inexistente.")

#busquedaCliente()


#Permitir obtener el total de usuarios por empresa, y todos sus datos

def totalUsuariosEmpresa():

    try:
        archivo = input("Ingrese el nombre del archivo de clientes sin extension: ")+".csv"
        campos = ["Nombre","Dirección","Documento","Fecha Alta","Correo Electrónico","Empresa"]


        if validarCsvClientes(archivo) == False:
            return

        else:

            with open(archivo, 'r',encoding="utf8") as clientesfile:
                clientescsv = csv.DictReader(clientesfile)

                empresa_buscada = input("Ingrese nombre completo de empresa: ")

                cliente = next(clientescsv, None)

                total_clientes = 0
                lista_clientes = []

                while cliente:

                    while cliente and cliente['Empresa'].lower()==empresa_buscada.lower()  :
                        lista_clientes.append(cliente)
                        total_clientes += 1

                        cliente = next(clientescsv, None)
                    cliente = next(clientescsv, None)


                print("----------------------------------------------------------------------------")
                print(f"Empresa: {empresa_buscada} ")
                print(f"Total Usuarios: {total_clientes}")
                print("----------------------------------------------------------------------------")
                print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]")
                if len(lista_clientes) ==0:
                    print("\nNo se encontraron coincidencias en la busqueda.")
                    return
                for cliente in lista_clientes:  #pasar a lista como en el ejemplo de consola
                    print(f"[{cliente[campos[0]]}, {cliente[campos[1]]}, {cliente[campos[2]]}, {cliente[campos[3]]}, {cliente[campos[4]]}, {cliente[campos[5]]}]")


    except IOError:
        print("\nHubo un error al abrir el archivo/Archivo inexistente.")


#totalUsuariosEmpresa()



def totalGastoEmpresa():

    try:
        campos = ["Nombre","Dirección","Documento","Fecha Alta","Correo Electrónico","Empresa"]
        campos2 = ["Documento","fecha","monto"]
        archivo = input("Ingrese el nombre del archivo de clientes sin extension: ")+".csv"
        archivo2 = input("Ingrese el nombre del archivo de viajes sin extension: ")+".csv"

        if validarCsvViajes(archivo2) == False or validarCsvClientes(archivo) == False:

            return

        else:

            with open(archivo, 'r',encoding="utf8") as clientesfile:
                clientescsv = csv.DictReader(clientesfile)

                empresa_buscada = input("Ingrese nombre completo de empresa: ")

                cliente = next(clientescsv, None)
                acumulado_total = 0

                while cliente:

                    while cliente and cliente['Empresa'].lower() == empresa_buscada.lower():
                        #print(cliente['Empresa'],cliente['Nombre']) #recorre todo los empleados de nexos bien.
                        with open(archivo2, 'r',encoding="utf8") as viajesfile:
                            viajescsv = csv.DictReader(viajesfile)
                            viaje = next(viajescsv, None)
                            acumulador_cliente = 0
                            while viaje:
                                #print(viaje['Documento'])
                                #print([cliente['Documento']])
                                while viaje and viaje['Documento'] == cliente['Documento']:
                                    gastos_int = float(viaje['monto'])
                                    #print(gastos_int)
                                    acumulador_cliente += gastos_int

                                    viaje = next(viajescsv, None)
                                viaje = next(viajescsv, None)
                            #print(acumulador_cliente)

                        cliente = next(clientescsv, None)

                        acumulado_total += acumulador_cliente

                    cliente = next(clientescsv, None)

                print("----------------------------------------------------------------------------")
                print(f"{empresa_buscada}  ${acumulado_total:.2f}")
                print("----------------------------------------------------------------------------")

    except IOError:
        print("\nHubo un error al abrir el archivo/Archivo inexistente.")

#totalGastoEmpresa()



def totalGatosDni():

    try:
        campos = ["Nombre","Dirección","Documento","Fecha Alta","Correo Electrónico","Empresa"]
        campos2 = ["Documento","fecha","monto"]
        archivo = input("Ingrese el nombre del archivo de clientes sin extension: ")+".csv"
        archivo2 = input("Ingrese el nombre del archivo de viajes sin extension: ")+".csv"


        if validarCsvViajes(archivo2) == False or validarCsvClientes(archivo) == False:

            return

        else:

            with open(archivo, 'r',encoding="utf8") as clientesfile:
                clientescsv = csv.DictReader(clientesfile)

                dni_buscado = input("Ingrese DNI: ")

                while valida_entero(dni_buscado) == False or len(dni_buscado) > 8 or len(dni_buscado) < 7:

                    dni_buscado = input("Error en el formato del DNI. Ingrese DNI: ")

                cliente = next(clientescsv, None)
                lista_viajes = []
                valida_existencia = []


                while cliente:

                    while cliente and cliente['Documento'] == dni_buscado:
                        cliente_datos = []
                        valida_existencia.append("existe")
                        for campo in campos:
                            cliente_datos.append(cliente[campo])

                        with open(archivo2, 'r',encoding="utf8") as viajesfile:
                            viajescsv = csv.DictReader(viajesfile)
                            viaje = next(viajescsv, None)
                            acumulador_cliente = 0
                            contador_cliente = 0
                            while viaje:

                                while viaje and viaje['Documento'] == cliente['Documento']:
                                    gastos_int = float(viaje['monto'])

                                    acumulador_cliente += gastos_int
                                    contador_cliente += 1

                                    viaje_datos = []
                                    for campo in campos2:
                                        viaje_datos.append(viaje[campo])

                                    lista_viajes.append(viaje_datos)

                                    viaje = next(viajescsv, None)
                                viaje = next(viajescsv, None)


                        cliente = next(clientescsv, None)


                    cliente = next(clientescsv, None)

                print("----------------------------------------------------------------------------")
                print(f"Documento: {dni_buscado}")
                print("----------------------------------------------------------------------------")

                if len(valida_existencia) == 0:
                    print("No se encontraron viajes/gastos asociados a ese DNI.")
                    return

                else:

                    print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]")
                    print(f"[{cliente_datos[0]}, {cliente_datos[1]}, {cliente_datos[2]}, {cliente_datos[3]}, {cliente_datos[4]}, {cliente_datos[5]}]")
                    print("----------------------------------------------------------------------------")

                    print(f"Total viajes: {contador_cliente}, Monto:  ${acumulador_cliente:.2f}")
                    print("----------------------------------------------------------------------------")
                    print(f"[{campos2[0]}, {campos2[1]}, {campos2[2]}]")
                    for i in lista_viajes:
                        print(f"[{i[0]}, {i[1]}, {i[2]}]")
                    print("----------------------------------------------------------------------------")

    except IOError:
        print("\nHubo un error al abrir el archivo/Archivo inexistente.")

#totalGatosDni()

def menu():
    lista_acciones = []

    while True:
        print("\n\n--------------------------- FACTURACION TAXIS ------------------------------")
        print("MENU:\n\n1.Busqueda de cliente por nombre.\n2.Busqueda total de usuarios por empresa.\n3.Busqueda total gastos por empresa. \n4.Busqueda total viajes y gastos por usuario.\n5.Salir.\n")
        opcion = input("Ingrese una opcion: ")
        print("----------------------------------------------------------------------------")
        lista_acciones.append("Menu")
        if opcion == "1":

            busquedaCliente()
            lista_acciones.append("Busqueda de cliente por nombre")

        elif opcion == "2":

            totalUsuariosEmpresa()
            lista_acciones.append("Busqueda total de usuarios por empresa")

        elif opcion == "3":

            totalGastoEmpresa()
            lista_acciones.append("Busqueda total gastos por empresa")


        elif opcion == "4":

            totalGatosDni()
            lista_acciones.append("Busqueda total viajes y gastos por usuario")

        elif opcion == "5":

            print("Recuerde que las consultas se encuentran almacenadas en archivolog.txt.")
            print("Adios!")
            lista_acciones.append("Salir")
            break

        else:
            print("Ingrese una opcion valida.")

    #print(lista_acciones)
    try:
        with open("archivolog.txt", 'w', newline="") as f:
            for i in lista_acciones:
                f.write(f"{i}\n")


    except IOError:
        print("Error con el archivo")



menu()
