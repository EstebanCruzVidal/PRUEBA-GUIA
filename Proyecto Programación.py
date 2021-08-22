""" PSEUDOCODIGO

ENTRADAS
    Informacion del Usuario
    Informacion para los analisis

SALIDAS
    Lista de personas 
    Analisis de creditos
    Sin Graficas para apoyo visual


Definir usuarioNuevo
    listaUsuario[nombreUsuario] = {
        "nombreUsuario" : nombreUsuario,
        "edadUsuario" : edadUsuario,
        "correoUsuario" : correoUsuario,
        "capital" : capital,
        "plazo" : plazo,
        "tasa" : tasa,
    }
    regresar verdad

Definir borrarUsuario 
    Escribir "Dame el nombre de usuario que quieres borrar"
    Borrar de lista de usuario
Definir menuUsuarios 

Definir editarUsuarios 
    Pedir nombre
    Pedir edad
    Pedir correo
    Pedir capital
    Pedir el plazo
    Pedir tasa de intereses
    
Definir analisis
    Preguntar que opcion quiere realizar
    Si opcion es 1
        Mostrar el capital de el usuario que introduzca
        Escribir "Por cuanto tiempo es tu inversion en meses"
        Escribir "¿Cuanto tiempo llevas en tu inversión?"
        Escribir "Dame el plazo que mantendras tu inversión"
        Escribir "Dame la tasa que tiene tu inversión(mensual)"
        Calcular inversion1
        Escribir ""Tu capital final es de ", inversion1, ",lo que recibiras mensualmente es", inversion, " ,lo que falta para que termine es ", restante, "meses, tus ganancias totales son de ", profit"
    Sino
    si opcion es 2
        Escribir "Dame el capital inicial de tu crédito"
        Escribir "Dame la tasa que tendrá tu crédito mensual"
        Escribir "Dame el plazo que tendrá tu crédito en meses"
        Escribir "Cuantos meses llevas de credito"
        Calcular analisis1
        Escribir "El capital de tu credito es de ", credito, "lo que pagaras de intereses es de ", intereses1, ",lo que pagaras mensualmente es de", intereses, "te falta ", plazocredito1, "por pagar, el valor total de tu credito es de ", creditoFinal"
    Fin Si
Definir Salir
    Escribir "Gracias por utilizar mi programa, ojalá te haya sido util")

Escribir "Hola, bienvenido a mi programa, elige la opción que quieras, \n\t1 - Crear un Usuario Nuevo\n\t2 - Borrar Usuario\n\t3 - Mostrar Usuarios\n\t4 - Editar Usuarios\n\t5 - Hacer analisis de Inversión o Crédito\n\t6 - Salir\n"
    Mientras opcion es diferente a "123456"
        Escribir "Ingresa una opcion valida"
    Si opcion empieza con "1"
       Escribir "Hola, dame tu nombre"  
        Escribir "Dame tu edad"
        Escribir "Dame tu correo electronico
            Si correo no tiene "@" o ".com" o ".mx"
                Escribir "Introduce un @ o recuerda agregar un .com o un .mx"
            Fin Si
        Escribir "¿Con cuanto capital cuentas?"
        Escribir "Dame el plazo que deseas mantener tu inversión o crédito en meses"
        Escribir "Dame la tasa que consideras que tiene tu inversión o tu crédito mensual"
    Registrar usuarioNuevo()
Sino 
    Si opcion empieza "2"
        Llamar borrarUsuario
Sino 
    Si opcion empieza "3"
        Llamar menuUsuarios
Sino 
    Si opcion empieza "4"
        Llamar editarUsuarios
Sino
    Si opcion empieza "5"
        Llamar analisis
Sino 
    Si opcion empieza "6"
         Llamar salir


"""
def usuarioNuevo ():#Creamos el diccionario donde guardaremos informacion de los usuarios y se podran guardar diferentes usuarios
    listaUsuarios[nombreUsuario] = {
        "nombreUsuario" : nombreUsuario,
        "edadUsuario" : edadUsuario,
        "correoUsuario" : correoUsuario,
        "capital" : capital,
        "plazo" : plazo,
        "tasa" : tasa,
    }
    return True

def borrarUsuario ():#Podremos borrar un usuario iterando para encontrar el nombre del usuario
        global listaUsuarios

        borrar = input("Dame el nombre de usuario que quieres borrar\n")
        for k in tuple(listaUsuarios.keys()):
            if k == borrar:
                del listaUsuarios[k]

def menuUsuarios ():#Podemos ver todos los usuarios que tenemos en forma de menu
    global listaUsuarios
    listaUsuarios
    while True:
        for each_key in listaUsuarios:
            print(each_key, '=>', listaUsuarios[each_key])
        break

def editarUsuarios ():#En esta funcion podemos editar la informacion de un usuario, combinando las dos anteriores funciones para iterar y modificar la informacion
    global listaUsuarios
    listaUsuarios

    while True:
        for each_key in listaUsuarios:
            print(each_key, '=>', listaUsuarios[each_key])
        editar = input("Dime el nombre del usuario que quieres editar\n")
        for k in tuple(listaUsuarios.keys()):
            if k == editar:
                nombreUsuario = ""#Volvemos a pedir todos los datos
                while True:
                    nombreUsuario= input("Hola, dame tu nombre:\n")
                    if nombreUsuario.isdigit() or not nombreUsuario != "":
                        print("Por favor solo introduce caracteres")
                    else:
                        break
            
                edadUsuario=""
                while True:
                    edadUsuario=input("Dame tu edad:\n")
                    if edadUsuario.isalpha() or not edadUsuario != "":
                        print("Por favor introduce solo digitos")
                    else:
                        break
                
                correoUsuario=""
                while True:
                    correoUsuario=input("Dame tu correo electronico:\n")
                    if (correoUsuario.find("@") == -1) or (correoUsuario.find(".com") == -1) and (correoUsuario.find(".mx") == -1) or not correoUsuario != "":
                        print("Introduce un @ o recuerda agregar un .com o un .mx")
                    else:
                        break
                
                capital=""
                while True:
                    capital=int(input("¿Con cuanto capital cuentas?:\n"))
                    if type(capital) is not int:
                        print("Introduce solo digitos")
                    else:
                        break
                
                plazo=""
                while True:
                    plazo=input("Dame el plazo que deseas mantener tu inversión o crédito en meses:\n")
                    if plazo.isalpha() or not plazo != "":
                        print("Introduce solo digitos")
                    else:
                        break
                
                tasa=""
                while True:
                    tasa=input("Dame la tasa que consideras que tiene tu inversión o tu crédito mensual:\n")
                    if tasa.isalpha() or not tasa != "":
                        print("Introduce solo digitos")
                    else:
                        break
                    tasa=tasa/100
                listaUsuarios[k] = {
                    "nombreUsuario" : nombreUsuario,
                    "edadUsuario" : edadUsuario,
                    "correoUsuario" : correoUsuario,
                    "capital" : capital,
                    "plazo" : plazo,
                    "tasa" : tasa,    
                }
        break

def analisis ():#Con esta funcion, se hacen los analisi de credito e inversion
    global listaUsuarios

    while True:
        opcion1 = input("Dime que opción quieres utilizar: \n\t1 - Hacer Anlisis de una Inversión\n\t2 - Hacer Analisis de un Crédito\n")

        while "12".find(opcion1[0]) == -1:
            opcion1 = input("Ingreso una opción valida\n")

        if opcion1.startswith("1"):
            while True:
                buscarUsuario = input("Dame el nombre del usuario que quieres que se le haga el analisis de inversión:\n")
                for k in tuple(listaUsuarios.keys()):#Iteramos para encontrar al usuario y trabajar con la informacion que dio en un principio
                    if k == buscarUsuario:
                       capital = listaUsuarios[k]['capital']
                       break
                    else:
                        print("Usuario no encontrado\n")                    
                        break

                tiempo1=""
                while True:
                    tiempo1 = int(eval(input("Por cuanto tiempo es tu inversión en meses:\n")))
                    if type(tiempo1) is not int:
                        print("Ingresa solo digitos")
                    else:
                        break

                tiempo2=""
                while True:
                    tiempo2= int(eval(input("¿Cuanto tiempo llevas en tu inversión?:\n")))
                    if type(tiempo2) is not int:
                        print("Ingresa solo digitos")
                    else:
                        break
                restante = tiempo1 - tiempo2

                """plazo1 = ""
                while True:
                    plazo1 = eval(input("Dame el plazo que mantendras tu inversión:\n"))
                    if plazo.isalpha():
                        print("Ingresa solo digitos")
                    else:
                        break"""

                tasa1 = ""
                while True:
                    tasa1 = int(eval(input("Dame la tasa que tiene tu inversión(mensual):\n")))
                    if type(tasa1) is not int:
                        print("Introduce solo digitos")
                    else:
                        break
                
                tasa1 = tasa1/100#Hacemos las operaciones correspondientes
                inversion= tasa1 * capital #rendimientos mensuales
                profit = inversion * tiempo1 #rendimientos totales
                inversion1 = capital + profit #total inversion

                analisis = print("Tu capital final es de ", inversion1, ",lo que recibiras mensualmente es", inversion, " ,lo que falta para que termine es ", restante, "meses, tus ganancias totales son de ", profit)
                ejeX = [capital,inversion1]#Aqui insertamos una grafica con los datos proporcionados
                ejeY = [restante,tiempo1]
                plt.plot(ejeX,ejeY)
                plt.ylabel('Plazo')
                plt.xlabel('Inversión')
                plt.show()
                break
        
        elif opcion1.startswith("2"):
            credito = ""
            while True:#Pedimos informacion para hacer el analisis del credito
                credito = int(input("Dame el capital inicial de tu crédito:\n"))
                if type(credito) is not int:
                    print("Ingresa solo digitos")
                else:
                    break

            credito1 = ""
            while True:
                credito1 = int(eval(input("Dame la tasa que tendrá tu crédito mensual:\n")))
                if type(credito1) is not int:
                    print("Ingresa solo digitos")
                else:
                    break
            
            credito2 = ""
            while True:
                credito2 = int(input("Dame el plazo que tendrá tu crédito en meses:\n"))
                if type(credito2) is not int:
                    print("Ingresa solo digitos")
                else:
                    break
            
            plazocredito=""
            while True:
                plazocredito = int(input("Cuantos meses llevas de credito\n"))
                if type(plazocredito) is not int:
                    print("Ingresa solo digitos")
                else:
                    break
                
            credito1 = credito1/100
            intereses = credito1 * credito #Credito mensual
            intereses1 = intereses * credito2 #Credito final
            creditoFinal = intereses1 + credito #Total a pagar del credito
            plazocredito1 = credito2 - plazocredito 

            analisis1 = print("El capital de tu credito es de ", credito, "lo que pagaras de intereses es de ", intereses1, ",lo que pagaras mensualmente es de", intereses, "te falta ", plazocredito1, "por pagar, el valor total de tu credito es de ", creditoFinal)
            
            ejeX = [credito,creditoFinal]#Insertamos una grafica para tener apoyo visual
            ejeY = [plazocredito,credito2]
            plt.plot(ejeX,ejeY)
            plt.ylabel('Plazo')
            plt.xlabel('Crédito')
            plt.show()
            break
            

def salir ():#Con esta funcion acaba el programa
    print("Gracias por utilizar mi programa, ojalá te haya sido util")
    exit()


global listaUsuarios
listaUsuarios = dict()#Definimos nuestra variable como diccionario
import matplotlib.pyplot as plt#importamos las librerias correspondientes
opcion = ""
while True:#Agregamos un menu
    opcion = input("Hola, bienvenido a mi programa, elige la opción que quieras, \n\t1 - Crear un Usuario Nuevo\n\t2 - Borrar Usuario\n\t3 - Mostrar Usuarios\n\t4 - Editar Usuarios\n\t5 - Hacer analisis de Inversión o Crédito\n\t6 - Salir\n")

    while "123456".find(opcion[0]) == -1: #Checamos que el usuario solo introduzca ciertos numeros del menu
        opcion = input("Ingresa una opcion valida\n")

    if opcion.startswith("1"):
        nombreUsuario = ""
        while True:#Pedimos informacion al usuario para poder crear un usuario nuevo
            nombreUsuario= input("Hola, dame tu nombre:\n")
            if nombreUsuario.isdigit() or not nombreUsuario != "":#En cada variable se hacen las reviciones correspondientes y se verifica que coloque algo
                print("Por favor solo introduce caracteres")
            else:
                break
    
        edadUsuario=""
        while True:
            edadUsuario=input("Dame tu edad:\n")
            if edadUsuario.isalpha() or not edadUsuario != "":
                print("Por favor introduce solo digitos")
            else:
                break
        
        correoUsuario=""
        while True:
            correoUsuario=input("Dame tu correo electronico:\n")
            if (correoUsuario.find("@") == -1) or (correoUsuario.find(".com")) == -1 and (correoUsuario.find(".mx") == -1) or not correoUsuario != "":
                print("Introduce un @ o recuerda agregar un .com o un .mx")
            else:
                break
        
        capital=""
        while True:
            capital=int(input("¿Con cuanto capital cuentas?:\n"))
            if type(capital) is not int:
                print("Introduce solo digitos")
            else:
                break
        
        plazo=""
        while True:
            plazo=input("Dame el plazo que deseas mantener tu inversión o crédito en meses:\n")
            if plazo.isalpha() or not plazo != "":
                print("Introduce solo digitos")
            else:
                break
        
        tasa=""
        while True:
            tasa=input("Dame la tasa que consideras que tiene tu inversión o tu crédito mensual:\n")
            if tasa.isalpha() or not tasa != "":
                print("Introduce solo digitos")
            else:
                break
            tasa=tasa/100
        usuarioNuevo()#Llamamos a nuestra funcion para que la informacion se guarde en la libreria

    elif opcion.startswith("2"):
        borrarUsuario()
    elif opcion.startswith("3"):
        menuUsuarios()
    elif opcion.startswith("4"):
        editarUsuarios()
    elif opcion.startswith("5"):
        analisis()
    elif opcion.startswith("6"):
        salir()
        break
