"""
TP fin curso inicial
Cristian Alderete - Patricio Noce - Javier Monzon
Preentrega 24-6-22
"""
import os
import json

#CAMBIAR SEGUN SISTEMA OPERATIVO
#sistema='clear' #Limpieza pantalla Linux o Mac
sistema='cls' #Limpieza pantalla Windows

from colorama import Fore, Style, Back, init
init(autoreset=True)

def cargar_json(nombre_archivo):
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    datos = json.load(archivo)
    archivo.close()
    return datos

def guardar_json(nombre_archivo, datos):
    archivo = open(nombre_archivo, 'w') # Abrimos el archivo en modo escritura
    json.dump(datos, archivo) # Volcamos los datos de la lista al archivo JSON
    archivo.close() # Cerramos el archivo

#Diccionarios
datos = cargar_json('TrabajoFinal/archivos.json') #Carga desde el archivo
lista_usuarios = datos["lista_usuarios"]
peliculas = datos["peliculas"]
alquilado = datos["alquilado"]

#Peliculas alquiladas (Javier)
#alquilado=[{'usuario': '22555888', 'peliculas': ['El Padrino', 'Toy Story', 'Titanic']}, {'usuario': '42555888', 'peliculas': ['El Rey León', 'Toy Story', 'El Padrino']}]

#Lista administradores(Javier)
adminAcceso=[
                {"dni":"29298661", "nombre_apellido":"Javier Monzon", "psw":"123456"},
                {"dni":"35759988", "nombre_apellido":"Cristian Alderete", "psw":"123456"},
                {"dni":"33246329", "nombre_apellido":"Patricio Noce", "psw":"123456"},
                {"dni":"admin", "nombre_apellido":"ADMINISTRADOR", "psw":"admin"}]

# Muestra la lista de películas. (Patricio)
def lista(peliculas): 
    for pelicula in peliculas:
            print(f"Cod:{pelicula['codigo_pelicula']:3} Titulo: {pelicula['titulo_pelicula']:15} Genero: {pelicula['genero_pelicula']:15} Año: {pelicula['año_pelicula']}")
            print(f"Descripcion: {pelicula['descripcion_pelicula']}")
            print()

# Añade una nueva pelicula a la lista. (Patricio)
def alta(peliculas):
    pelicula = {}
    ultima_pelicula = 4 # Comienza en 4 porque ya hay 4 películas en la lista inicial
    ultima_pelicula += 1
    pelicula = {
        "codigo_pelicula": ultima_pelicula,
        "titulo_pelicula": input("Titulo: "),
        "genero_pelicula": input("Genero: "),
        "año_pelicula": int(input("Año: ")),
        "descripcion_pelicula": input("Descripcion: ")
    }
    peliculas.append(pelicula)
    reasignar_codigos(peliculas)
    print("El Alta se realizó correctamente")

# Elimina una pelicula de la lista por su codigo. (Patricio)
def baja(codigo, peliculas):
    for pelicula in peliculas:
        if pelicula["codigo_pelicula"] == codigo:
            peliculas.remove(pelicula)
            print("La Baja se realizó correctamente")
            reasignar_codigos(peliculas)
            return
    print("No se encontró el titulo")

# Modifica una pelicula de la lista por su codigo. (Patricio)
def modificar(codigo, peliculas):
    for pelicula in peliculas:
        if pelicula["codigo_pelicula"] == codigo:
            pelicula["genero_pelicula"] = input("Genero: ")
            pelicula["año_pelicula"] = int(input("Año: "))
            pelicula["descripcion_pelicula"] = input("Descripcion: ")
            print("La Modificación se realizó correctamente")
            reasignar_codigos(peliculas)
            return
    print("No se encontró el titulo")

# Reasigna el codigo de la lista de peliculas nuevamente. (Patricio)
def reasignar_codigos(peliculas):
    ultima_pelicula = 0  # Reiniciar el contador
    for pelicula in peliculas:
        ultima_pelicula += 1
        pelicula["codigo_pelicula"] = ultima_pelicula

#Autenticacion de usuario (Javier)
def autorizacion(usuarios, tipo):
    intento=3
    usu=False #Variable para validacion de usuario
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+f'INGRESA TU DNI Y CONTRASEÑA PARA ACCEDER COMO {tipo} ! ! !'.center(90,' '))
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print()
    while intento!=0: #Busca en el diccionario de usuarios si se encuentra el DNI
        dni=input('Ingrese su DNI: ')
        i=0
        for usuario in usuarios:
            if usuario["dni"]==dni:
                print()
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+f'BIENVENIDO {usuario["nombre_apellido"]}!!!'.center(90,' '))
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                print()
                usu=True
                intento=0
                break
            i+=1
        if usu==False: #Si al buscar no coincide el DNI da 3 intentos para la busqueda
            intento-=1
            print()
            print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
            print(Back.RED+Fore.WHITE+Style.BRIGHT+'EL DNI NO COINCIDE CON NINGUN USUARIO'.center(90,' '))
            print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LE QUEDAN {intento} INTENTOS'.center(90,' '))
            print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
            print()
    if usu==True:
        usu=False
        intento=3
        while intento!=0: #Comprueba si la contraseña es correcta
            clave=input('Ingrese su contraseña: ')
            if usuarios[i]["psw"]==clave:
                print()
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+'¡ ¡ ¡ CONTRASEÑA CORRECTA ! ! !'.center(90,' '))
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
                intento=0
                usu=True
            else:
                intento-=1
                print()
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.RED+Fore.WHITE+Style.BRIGHT+'CONTRASEÑA INCORRECTA!'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LE QUEDAN {intento} INTENTOS'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
    
    if usu==False: 
        print()
        print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
        print(Back.RED+Fore.WHITE+Style.BRIGHT+'NO SE PUDO AUTENTICAR USUARIO'.center(90,' '))
        print(Back.RED+Fore.WHITE+Style.BRIGHT+'VOLVIENDO AL MENU PRINCIPAL'.center(90,' '))
        print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
        print()
    
    return usu,i #Retorna si se pudo aprobar el acceso y en que posicion del diccionario esta el usuario

#Alquiler de peliculas (Javier)
def menuAlquiler(posUsuario, usuario, peliculas, alquilado):
    #Javier
    peli=False
    listaPelis=[]
    print()
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+f'¿{usuario[posUsuario]["nombre_apellido"]} QUE QUIERES VER HOY?'.center(90,' '))
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+' '*90)
    print()
    lista(peliculas)
    while peli==False:
        try:
            i=0
            print()
            op=int(input(Fore.WHITE+Style.BRIGHT+'Elije por numero de pelicula: '))
            for pelicula in peliculas:
                if pelicula["codigo_pelicula"]==op:
                    print()
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+f'Usted esta por alquilar la pelicula {pelicula["titulo_pelicula"]}'.center(90,' '))
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                    peli=True
                    listaPelis.append(pelicula["titulo_pelicula"])
                    break
                i+=1
            if peli==False: 
                print()
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' *90')
                print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LA OPCION {op} NO PERTENECE A UNA PELICULA'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+'INTENTE NUEVAMENTE'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
            else:
                while True:
                    try:
                        print()
                        agregar=input(Fore.WHITE+Style.BRIGHT+'¿Desea agregar otra pelicula mas? (S/N): ')
                        agregar=agregar.upper()
                        match agregar:
                            case "S":
                                peli=False
                                break
                            case "N":
                                break
                            case _:
                                print()
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'OPCION INVALIDA PRESIONE S o N'.CENTER(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'INTENTE NUEVAMENTE'.CENTER(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print()
                    except AttributeError:
                        print()
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE S o N'.center(90,' '))
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO NUMEROS!'.center(90,' '))
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        except AttributeError:
            print()
            print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
            print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO PARA SELECCIONAR LA PELICULA'.center(90,' '))
            print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO CARACTERES!'.center(90,' '))
            print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
    print()
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+'Usted se llevara la(s) pelicula(s):'.center(90,' '))
    for cod in listaPelis:
        print(Back.WHITE+Fore.BLUE+Style.BRIGHT+f"{cod}".center(90,' '))
    print()
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+'¡ ¡ ¡ QUE DISFRUTE DEL ESPECTACULO ! ! !'.center(90,' '))
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    alquilado.append({"usuario":usuario[posUsuario]["dni"], "peliculas":listaPelis})

#Menu de peliculas (Patricio)
def menuPeliculas():
    opcion = 0
    while opcion != "5":
        print(Back.BLUE+Fore.WHITE +" "*90)
        print(Back.BLUE+Fore.WHITE + Style.BRIGHT+"LISTADO DE PELICULAS".center(90,' '))
        print(Back.BLUE+Fore.WHITE +" "*90)
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print(Back.YELLOW+Fore.BLACK+"1- Alta".center(90,' '))
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print(Back.YELLOW+Fore.BLACK+"2- Baja".center(90,' '))
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print(Back.YELLOW+Fore.BLACK+"3- Lista".center(90,' '))
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print(Back.YELLOW+Fore.BLACK+"4- Modificación".center(90,' '))
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print(Back.YELLOW+Fore.RED+"5- Salir".center(90,' '))
        print(Back.YELLOW+Fore.BLACK+" "*90)
        print()
        opcion = input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: ")
        if opcion == "1":
            print(Back.BLUE+Fore.BLACK+' '*90)
            print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'ALTA DE PELICULA'.center(90,' '))
            print(Back.BLUE+Fore.BLACK+' '*90)
            print()
            alta(peliculas)
        elif opcion == "2":
            print(Back.BLUE+Fore.BLACK+' '*90)
            print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'BAJA DE PELICULAS'.center(90,' '))
            print(Back.BLUE+Fore.BLACK+' '*90)
            print()
            lista(peliculas)
            codigo = int(input("Escribe el Codigo de la Pelicula a eliminar: "))
            baja(codigo, peliculas)
        elif opcion == "3":
            print(Back.BLUE+Fore.BLACK+' '*90)
            print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'LISTA DE PELICULAS'.center(90,' '))
            print(Back.BLUE+Fore.BLACK+' '*90)
            print()
            lista(peliculas)
        elif opcion == "4":
            print(Back.BLUE+Fore.BLACK+' '*90)
            print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'MODIFICAR PELICULA'.center(90,' '))
            print(Back.BLUE+Fore.BLACK+' '*90)
            print()
            lista(peliculas)
            codigo = int(input("Escribe el Codigo de la Pelicula a modificar: "))
            modificar(codigo, peliculas)
        elif opcion == "5":
            print("Salir")
            print("Cerrando el programa... Adiós")
        else:
            print("Opción incorrecta")

# Función para ver la lista de usuarios (Cristian)
def ver_lista_usuario(lista_usuarios):
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT +' '*90)
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT +'LISTA DE USUARIOS'.center(90,' '))
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT +' '*90)
    print()
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT + f"ID  Nombre y apellido         DNI        Telefono        Domicilio".ljust(90,' '))
    for lista in lista_usuarios:
        print(Fore.CYAN + f"{lista['id_usuario']:3}",end=' ')
        print(Fore.CYAN + f"{lista['nombre_apellido']:25}",end=' ')
        print(Fore.CYAN + f"{lista['dni']:10}",end=' ')
        print(Fore.CYAN + f"{lista['contacto']:15}",end=' ')
        print(Fore.CYAN + f"{lista['Domicilio']}")
    print()

# Función para agregar un usuario (Cristian)
def agregar_usuario(lista_usuarios):
    lista_usuario = {}
    ultimo_usuario = lista_usuarios[-1]["id_usuario"]
    lista_usuario["id_usuario"] = ultimo_usuario + 1
    lista_usuario["dni"] = input("Ingrese DNI: ")
    lista_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
    lista_usuario["contacto"] = input("Ingrese numero de telefono: ")
    lista_usuario["Domicilio"] = input("Ingrese domicilio: ")
    lista_usuario["psw"] = input("Ingrese su contraseña: ")
    lista_usuarios.append(lista_usuario)

# Función para eliminar un usuario (Cristian)
def eliminar_usuario(usuario, lista_usuarios):
    for usuario_eliminar in lista_usuarios:
        if usuario_eliminar["id_usuario"] == usuario:
            lista_usuarios.remove(usuario_eliminar)
            print("La baja se realizo correctamente")
            return
    print("No se encontro el usuario")

# Función para modificar los datos de un usuario (Cristian)
def modificar_lista_usuario(usuario, lista_usuarios):
    print()
    for modificar_usuario in lista_usuarios:
        if modificar_usuario["id_usuario"] == usuario:
            modificar_usuario["dni"] = input("Ingrese DNI: ")
            modificar_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
            modificar_usuario["contacto"] = input("Ingrese numero de telefono: ")
            modificar_usuario["Domicilio"] = input("Ingrese domicilio: ")
            print(Back.GREEN+Style.BRIGHT+Fore.WHITE+' '*90)
            print(Back.GREEN+Style.BRIGHT+Fore.WHITE+"LOS DATOS SE MODIFICARON CORRECTAMENTE ! ! !".center(90,' '))
            print(Back.GREEN+Style.BRIGHT+Fore.WHITE+' '*90)
            return
    print()
    print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
    print(Back.RED+Fore.WHITE+Style.BRIGHT+"NO SE ENCONTRO USUARIO".center(90,' '))
    print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
    print()

#Menu usuarios(Cristian)
def regUsuarios(lista_usuarios):
    while True:
        print(Back.BLUE+Fore.WHITE + " " * 90)
        print(Back.BLUE+Fore.WHITE + Style.BRIGHT+ "GESTIÓN DE USUARIOS".center(90, ' '))
        print(Back.BLUE+Fore.WHITE + " " * 90)
        print(Back.YELLOW+" "*90)
        print(Back.YELLOW+Fore.BLACK + "1. Ver Usuarios".center(90, ' '))
        print(Back.YELLOW+" "*90)
        print(Back.YELLOW+Fore.BLACK + "2. Agregar Usuario".center(90, ' '))
        print(Back.YELLOW+" "*90)
        print(Back.YELLOW+Fore.BLACK + "3. Eliminar Usuario".center(90, ' '))
        print(Back.YELLOW+" "*90)
        print(Back.YELLOW+Fore.BLACK + "4. Modificar Usuario".center(90, ' '))
        print(Back.YELLOW+" "*90)
        print(Back.YELLOW+Fore.RED + "5. Volver al menú principal".center(90, ' '))
        print(Back.YELLOW+Fore.BLACK + " " * 90)
        print()
        opcion_usuario = int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
        if opcion_usuario == 1:
            ver_lista_usuario(lista_usuarios)
        elif opcion_usuario == 2:
            agregar_usuario(lista_usuarios)
        elif opcion_usuario == 3:
            usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(usuario, lista_usuarios)
        elif opcion_usuario == 4:
            usuario = int(input("Ingrese el ID del usuario a modificar: "))
            modificar_lista_usuario(usuario, lista_usuarios)
        elif opcion_usuario == 5:
            break
        else:
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print(Back.RED + Fore.WHITE + Style.BRIGHT + 'Por favor, ingrese una opción válida'.center(90, ' '))
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print()

#Devolucion de peliculas por usuario (Javier)
def devolucionPeliculas(posUsu, usuarios, alquilado):
    print(Back.BLUE+Fore.WHITE + " " * 90)
    print(Back.BLUE+Fore.WHITE + Style.BRIGHT+ "DEVOLUCION DE PELICULAS".center(90, ' '))
    print(Back.BLUE+Fore.WHITE + " " * 90)
    print()
    i=0
    enc=0
    docu=usuarios[posUsu]["dni"] #Toma el dni del usuario registrado
    nom=usuarios[posUsu]["nombre_apellido"] #Toma el nombre y apellido
    for alquiler in alquilado:
        if alquiler["usuario"]==docu: 
            posalq=i
            enc+=1
        i=+1
    if enc>0:
        print()
        cant=len(alquilado[posalq]["peliculas"])
        if cant==1:
            print(f'{nom} La pelicula alquilada que tenes es ',end='')
            for pelicula in alquilado[posalq]["peliculas"]:
                print(pelicula)
        elif cant>1:
            print(f'{nom} tenes alquiladas las peliculas:'.center(90,' '))
            for pelicula in alquilado[posalq]["peliculas"]:
                print(pelicula.center(90,' '))
            print()
        while True:
            
            print()
            dev=input('Desea realizar la devolucion? (S o N): ')
            print()
            dev=dev.upper()
            match dev:
                case 'S':
                    alquilado.pop(posalq)
                    print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                    print(Back.GREEN+Fore.WHITE+Style.BRIGHT+'DEVOLUCION EXITOSA ! ! !'.center(90,' '))
                    print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                    break
                case 'N':
                    print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                    print(Back.WHITE+Fore.BLUE+Style.BRIGHT+'NO SE DEVOLVIO NINGUNA PELICULA ! ! !'.center(90,' '))
                    print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                    print()
                    break
                case _:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                    print(Back.RED+Fore.WHITE+Style.BRIGHT+'CARACTER INVALIDO!!!'.center(90,' '))
                    print(Back.RED+Fore.WHITE+Style.BRIGHT+'Ingrese S o N'.center(90,' '))
                    print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                    print()
    else:
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+' '*90)
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+f'{nom} no tenes ninguna pelicula alquilada ! ! !'.center(90,' '))
        print(Back.WHITE+Fore.BLACK+Style.BRIGHT+' '*90)
        print()

#Menu principal(Javier)
os.system(sistema)
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+'GRUPO 14'.center(90,' '))
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #######  #####  #    # ######  #     #  #####  ####### ####### ######   ')
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #     #  ') 
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     # #          #    #       #     #  ') 
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #     # #       ###    ######  #     #  #####     #    #####   ######   ')
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     #       #    #    #       #   #    ')
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #    #   ')
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  ####### #######  #####  #    # ######   #####   #####     #    ####### #     #  ')
print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+' '*90)
print(Back.YELLOW+Fore.BLUE+Style.BRIGHT+f'by Cristian Alderete, Patricio Noce, Javier Monzon '.rjust(90,' '))

while True:
    print()
    print(Back.BLUE+Fore.BLACK+' '*90)
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'BIENVENIDOS A NUESTRO CLUB EN LINEA'.center(90,' '))
    print(Back.BLUE+Fore.BLACK+' '*90)
    print(Back.YELLOW+Fore.BLACK+' '*90)
    print(Back.YELLOW+Fore.BLACK+'1 - ¿Sos usuario?'.center(90,' '))
    print(Back.YELLOW+Fore.BLACK+' '*90)
    print(Back.YELLOW+Fore.BLACK+'2 - ¿Como no sos usuario? Vamos a registrarte!!!'.center(90,' '))
    print(Back.YELLOW+Fore.BLACK+' '*90)
    print(Back.YELLOW+Fore.BLACK+'3 - Acceso para administradores'.center(90,' '))
    print(Back.YELLOW+Fore.BLACK+' '*90)
    print(Back.YELLOW+Fore.RED+'4 - SALIR'.center(90,' '))
    print(Back.YELLOW+Fore.BLACK+' '*90)
    print()
    try:
        op=int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
        print()
        match op:
            case 1:
                os.system(sistema)
                usuEncontrado, pos = autorizacion(lista_usuarios, "USUARIO")
                if usuEncontrado==True:
                    while True:
                        print()
                        print(Back.BLUE+Fore.BLACK+' '*90)
                        print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'MENU DE USUARIO'.center(90,' '))
                        print(Back.BLUE+Fore.BLACK+' '*90)
                        print(Back.YELLOW+Fore.BLACK+' '*90)
                        print(Back.YELLOW+Fore.BLACK+'1 - Alquilar'.center(90,' '))
                        print(Back.YELLOW+Fore.BLACK+' '*90)
                        print(Back.YELLOW+Fore.BLACK+'2 - Devolucion'.center(90,' '))
                        print(Back.YELLOW+Fore.BLACK+' '*90)
                        print(Back.YELLOW+Fore.RED+'3 - VOLVER AL MENU ANTERIOR'.center(90,' '))
                        print(Back.YELLOW+Fore.BLACK+' '*90)
                        print()
                        ad=int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
                        match ad:
                            case 1:
                                menuAlquiler(pos, lista_usuarios, peliculas, alquilado)
                                True
                            case 2:
                                devolucionPeliculas(pos, lista_usuarios,alquilado)
                                True
                            case 3:
                                break
                            case _:
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'CARACTER INVALIDO!!!'.center(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'Ingrese S o N'.center(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print()
                print()
            case 2:
                os.system(sistema)
                print(Back.BLUE+Fore.BLACK+' '*90)
                print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'REGISTRESE PARA UTILIZAR NUESTROS SERVICIOS'.center(90,' '))
                print(Back.BLUE+Fore.BLACK+' '*90)
                print()
                agregar_usuario(lista_usuarios)
            case 3:
                os.system(sistema)
                usuEncontrado, pos = autorizacion(adminAcceso, "ADMINISTRADOR")
                if usuEncontrado==True:
                    print()
                    print(Back.BLUE+Fore.BLACK+' '*90)
                    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'MENU ADMINISTRADOR'.center(90,' '))
                    print(Back.BLUE+Fore.BLACK+' '*90)
                    print(Back.YELLOW+Fore.BLACK+' '*90)
                    print(Back.YELLOW+Fore.BLACK+'1 - Usuarios'.center(90,' '))
                    print(Back.YELLOW+Fore.BLACK+' '*90)
                    print(Back.YELLOW+Fore.BLACK+'2 - Peliculas'.center(90,' '))
                    print(Back.YELLOW+Fore.BLACK+' '*90)
                    print(Back.YELLOW+Fore.BLACK+'3 - VOLVER AL MENU ANTERIOR'.center(90,' '))
                    print(Back.YELLOW+Fore.BLACK+' '*90)
                    print()
                    ad=int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
                    match ad:
                        case 1:
                            os.system(sistema)
                            regUsuarios(lista_usuarios)
                        case 2:
                            os.system(sistema)
                            menuPeliculas()
                        case 3:
                            break
                        case _:
                            pass
            case 4:
                os.system(sistema)
                print()
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+'GRUPO 14'.center(90,' '))
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #######  #####  #    # ######  #     #  #####  ####### ####### ######   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #     #  ') 
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     # #          #    #       #     #  ') 
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #     # #       ###    ######  #     #  #####     #    #####   ######   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     #       #    #    #       #   #    ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #    #   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  ####### #######  #####  #    # ######   #####   #####     #    ####### #     #  ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+' '*90)
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'LOS PARTICIPANTES DEL GRUPO 14 AGRADECEN LA UTILIZACION DE NUESTRA PLATAFORMA'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'ESPERAMOS QUE VUELVA PRONTO!!!'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'ALUMNOS: Cristian Alderete, Patricio Noce, Javier Monzon'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'CAC INICIAL 2024 Comision 24093'.center(90,' '))
                print()
                
                datos["lista_usuarios"]=lista_usuarios
                datos["peliculas"]=peliculas
                datos["alquilado"]=alquilado
                guardar_json('archivos.json', datos)
                
                break
            case _:
                print()
                print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO ENTRE EL 1 Y EL 4'.center(90,' '))
                print(Back.RED+Style.BRIGHT+Fore.WHITE+f'EL NUMERO {op} NO ES UNA OPCION!'.center(90,' '))
                print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                print()
    except ValueError:
        print()
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO ENTRE EL 1 Y EL 4'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO CARACTERES!'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print()
    except KeyboardInterrupt:
        print()
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'NA NA NA NA NAAAAAAAAA'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'PARA SALIR UTILICE EL 4!'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print()
