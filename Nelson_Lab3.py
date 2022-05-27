from calendar import c
import datetime

#clase Cliente
class Cliente:
    def __init__(self, nombre, telefono, estado,numeroCedula):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.numeroCedula=numeroCedula
    #Metodo registrar clave
    def registrarse(self, clave):     
       
       clave=clave

    #Metodo iniciar secion con numero de cedula y clave
    def inicioSecion(self, usu,contra):
        usu=usu
        contra=contra

#clase tienda
class tienda:
    def __init__(self, nombreTienda, telefonoTienda, estadoTienda, gerenteTienda):
        self.nombreTienda=nombreTienda
        self.telefonoTienda=telefonoTienda
        self.estadoTienda=estadoTienda
        self.gerenteTienda=gerenteTienda
    

#menu principal
menuPrincipal=int(input("============================\n Menu Principal: \n 1-Cliente \n 2-Administrador \n 3-Salir  \n============================\n Ingrese una opcion: "))
while menuPrincipal != 3:
    
    if menuPrincipal ==1:
            #submenu2
            subMenu2=int(input("============================\n Sub Menu Clientes: \n 1-Registrarse \n 2-Ingresar sesion \n 3-Regresar \n============================\n Ingrese una opcion: ")) 
            while subMenu2 != 3:
                if subMenu2 ==1:
                     print("Registrarse ")
                     nombre=str(input("Ingrese su nombre: "))
                     telefono=str(input("Ingrese su telefono: "))
                     estado=str(input("Ingrese su estado: "))
                     numeroCedula=str(input("Ingrese su cedula: "))
                     clave=str(input("Ingrese clave para registrar: "))
                     z=Cliente(nombre, telefono, estado,numeroCedula,).registrarse(clave)       #instanciar cliente y metodo registrarse
                     print("usted se a registrado")

                elif subMenu2 ==2:
                     print("Inicie sesion")

                     print("A continuacion ingrese los datos: ")
                     #metodo iniciosesion comparar clave y numero de cedula ingresada para acceder
                     usu=str(input("Ingrese Numero de cedula ya registrado: "))
                     contra=str(input("Ingrese contraseña ya registrado: "))
                     if usu==numeroCedula and contra==clave:
                         print("Acceso concedido")
                         #submenu3
                         subMenu3=int(input("============================\n Sub Menu Clientes 2: \n 1-Registrarse en tienda \n 2- Historia vista por cliente \n 3-Estado \n 4-Regresar \n============================\n Ingrese una opcion: "))
                         while subMenu3 != 4:
                            if subMenu3 ==1:
                                print("============================\n Registrarse en una tienda ")
                                nombreTienda=str(input("Ingrese nombre de tienda: "))
                                telefonoTienda=str(input("Ingrese telefono de tienda: "))
                                estadoTienda=str(input("Ingrese el estado de tienda: "))
                                gerenteTienda=str(input("Ingrese nombre de Gerente: "))

                                print("______________________________________________\n")
                                print("               Tienda regsitrada: \n")
                                print("Nombre - telefono - estado - gerente: \n")
                                p=tienda(nombreTienda, telefonoTienda, estadoTienda, gerenteTienda)      #instanciar tienda
                                print(p.nombreTienda,"-",telefonoTienda,"-",estadoTienda,"-",gerenteTienda)
                                fechaActual=datetime.datetime.now()
                                fechaActual1=datetime.datetime.strftime(fechaActual, '%b %d %Y %H:%M:%S')
                                print(fechaActual1)
                                print("______________________________________________\n")
                                
                                

                            elif subMenu3 ==2:
                                print("______________________________________________\n")
                                print("Ver historial de tienda visitada del cliente ")
                                print(fechaActual1," - ",p.nombreTienda)
                                print("______________________________________________\n")

                            elif subMenu3 ==3:
                                print("\n El estado del cliente es :",estado)
                            elif subMenu3 ==4:
                                print("Regresar ")
                            else:
                                    print("Por favor ingrese una opcion correcta: ")
                            subMenu3=int(input("============================\n Sub Menu Clientes 2: \n 1-Registrarse en tienda \n 2- Historia vista por cliente \n 3-Estado \n 4-Regresar \n============================\n Ingrese una opcion: "))
                     else:
                         print("acceso denegado")
                elif subMenu2 ==3:
                     print("Regresar ")
                else:
                        print("Por favor ingrese una opcion correcta: ")
                subMenu2=int(input("============================\n Sub Menu Clientes: \n 1-Registrarse \n 2-Ingresar sesion \n 3-Regresar \n============================\n Ingrese una opcion: "))

       

    elif menuPrincipal ==2:
        #mostrar datos en administrador despues de registrar datos
        
        print("ADMININISTRADOR")
        print("Historial de visita")
        print("----------------------------------")
        print(fechaActual1,"-",nombre,"-",nombreTienda)
        print("----------------------------------")
        print("Lista de clientes")
        print(nombre,"-",telefono,"-",estado)
        print("----------------------------------")
        print("Lista de Tiendas visitada por administrador")
        print(nombreTienda,"-",telefonoTienda,"-",gerenteTienda,"-",estadoTienda)
        print("----------------------------------")

    elif menuPrincipal ==3:
        print("GRACIAS POR SU VISITA ")
    else:
        print("Por favor ingrese una opcion correcta: ")
    menuPrincipal=int(input("============================\n Menu Principal: \n 1-Cliente \n 2-Administrador \n 2-Salir  \n============================\n Ingrese una opcion: "))

