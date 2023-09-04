# Importa los módulos necesarios
import Menu, functions, secrets, time, smtplib
from datetime import date as dt
import yagmail
import pickle

# Variable que almacena el estado VIP del usuario
estado_vip = False

# Lista para almacenar los tokens VIP generados
tokens = []

# Variable para verificar el envío de correo electrónico
verify = False

# Función que muestra el menú VIP
def menu_vip():
    while True:
        functions.clear()
        print("=" * functions.cant_caracter)
        print("¿Qué desea hacer?".center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        print("[1] Conseguir VIP")
        print("[2] Ya tengo VIP")
        print("[3] ¿Qué es el VIP?")
        print("[4] Soporte en línea")
        print("[5] Volver al menú")
        print("=" * functions.cant_caracter)

        opcion = input(">>> ")

        if opcion == "1":
            return menu_nuevo_vip()
        elif opcion == "2":
            return ingresar_token()
        elif opcion == "3":
            whatis_vip()
        elif opcion == "4":
            return soporte()
        elif opcion == "5":
            Menu.menu()
        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

# Función para el menú de obtención de VIP
def menu_nuevo_vip():
    functions.clear()
    while True:
        print("=" * functions.cant_caracter)
        print('¿Deseas conseguir VIP?'.center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        print("[1] Si, quiero VIP --[2.99 Dolars per month]")
        print("[2] No, volver al menú")
        print("=" * functions.cant_caracter)

        opcion = input(">>> ")

        if opcion == "1":
            return nuevo_vip()
        elif opcion == "2":
            if not estado_vip:
                return menu_vip()
            else:
                return menu_exis_vip()

        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

# Función para explicar qué es el VIP
def whatis_vip():
    while True:
        functions.clear()
        print("=" * functions.cant_caracter)
        print('El VIP es un servicio que te permite'.center(functions.cant_caracter, ' '))
        print('desbloquear las mejores funciones de la app.'.center(functions.cant_caracter, ' '))
        print('Por un precio muy bajo, podrás tener'.center(functions.cant_caracter, ' '))
        print('un seguimiento de tus alimentos y calorías,'.center(functions.cant_caracter, ' '))
        print('un ChatBot con el cual hablar y pedirle cosas,'.center(functions.cant_caracter, ' '))
        print('y nuevos comandos próximamente!'.center(functions.cant_caracter, ' '))
        print('También se incluye soporte al cliente.'.center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        print('[1] Volver al menú de VIP')
        print('[2] Volver al menú principal')
        print("=" * functions.cant_caracter)

        opcion = input(">>> ")

        if opcion == "1":
            if not estado_vip:
                menu_vip()
            else:
                menu_exis_vip()

        elif opcion == "2":
            Menu.menu()

        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

        input("\nPresiona cualquier tecla para continuar...")

# Función para obtener VIP
def nuevo_vip():
    while True:
        functions.clear()
        print("=" * functions.cant_caracter)
        print('El pago se realiza únicamente con tarjeta.'.center(functions.cant_caracter, ' '))
        print('Siendo un test, la tarjeta no debe ser real'.center(functions.cant_caracter, ' '))
        print('pero debe tener entre 13 y 18 dígitos.'.center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        print('Ingresa el número de la tarjeta:')
        num_tarjeta = input('>>> ')
        print("=" * functions.cant_caracter)
        print('Ingresa el código de seguridad:')
        codigo_seg = input('>>> ')
        print("=" * functions.cant_caracter)
        print('Ingresa el mes de expiración: Ej: 10')
        mes = input('>>> ')
        print("=" * functions.cant_caracter)
        
        if mes.isnumeric():
            if int(mes) > 12:
                print('Ingresaste una opción incorrecta, inténtalo nuevamente:')
                input("\nPresiona cualquier tecla para continuar...")
                return nuevo_vip()
        else:
            print('Ingresaste una opción incorrecta, inténtalo nuevamente:')
            input("\nPresiona cualquier tecla para continuar...")
            return nuevo_vip()
        
        if len(mes) < 1 or len(mes) > 2:
            print('Ingresaste una opción incorrecta, inténtalo nuevamente:')
            input("\nPresiona cualquier tecla para continuar...")
            return nuevo_vip()
        
        print('Ingresa el año de expiración: Ej: 21')
        año = input('>>> ')
        print("=" * functions.cant_caracter)
        
        if año.isnumeric():
            if len(año) < 2:
                print('Ingresaste una opción incorrecta, inténtalo nuevamente:')
                input("\nPresiona cualquier tecla para continuar...")    
                return nuevo_vip()
        else:
            print('Ingresaste una opción incorrecta, inténtalo nuevamente:')
            input("\nPresiona cualquier tecla para continuar...")            
            return nuevo_vip()
                    
        if len(mes) == 1:
            mes = f'0{mes}'
        
        '2023-07-01'
        date_exp = f'23{año}-{mes}-07'
        today = f'{dt.today()}'

        año_exp2 = int(date_exp[0:4])
        año_actual = int(today[0:4])
        
        if año_exp2 >= año_actual:
            verify = True
        else :
            verify = False
            
        if len(num_tarjeta) > 12 and len(num_tarjeta) < 19 and len(codigo_seg) > 2 and len(codigo_seg) < 5 and verify == True:
            return vip_pago()
        else:
            print('Ingresaste un método de pago incorrecto.')
            print('Intenta nuevamente.')
            time.sleep(1.5)

# Función para realizar el pago y obtener VIP
def vip_pago():
    while True:
        global mail
        mail = False
        print("=" * functions.cant_caracter)
        print('Ingresa tu correo electrónico y te enviaremos el token'.center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        dest_mail = [input('>>> ')]
        email = 'nutrifit765@gmail.com'
        try:
            message = secrets.token_hex(12)
            tokens.append(message)
            
            with open("Proyecto/tokens.pickle", "wb") as f:
                pickle.dump(tokens, f)

            contrasenia = 'Prueba1235'
            yag = yagmail.SMTP(user = email, password=contrasenia)
            asunto = 'Token VIP - NutriFit'
            mensaje = tokens
            yag.send = (dest_mail, asunto, mensaje)

            print("E-Mail exitosamente enviado a: %s:" % (dest_mail))
            print('Si surgen problemas, puedes usar nuestro soporte en línea')
            print(f'Debido a que la función de enviar Emails se encuentra desactivada, esta es tu clave:\n{tokens}')
            mail = True
        except:
            print("No se ha podido enviar el correo, intenta nuevamente.")
            mail = False
        
        if mail == True:
            return ingresar_token()
        else:
            pass

# Función para ingresar el token y obtener VIP
def ingresar_token():
    print("=" * functions.cant_caracter)
    print("Ingresa el token que se te envió por correo electrónico".center(functions.cant_caracter, ' '))
    print("Ingresa 'ayuda' si tu token no llegó".center(functions.cant_caracter, ' '))
    print("=" * functions.cant_caracter)

    global ingreso_token
    ingreso_token = input('>>> ')
    
    with open("Proyecto/tokens.pickle", "rb") as f:
        obj = pickle.load(f)
        
    if ingreso_token in obj:
        global estado_vip
        estado_vip = True
        print("¡Perfecto! ¡Ahora tienes VIP!")
    elif ingreso_token == 'ayuda' or ingreso_token == 'Ayuda' or ingreso_token == 'AYUDA':
        return vip_pago()
    else:
        return print("Token incorrecto, inténtalo nuevamente")

# Función para el menú VIP existente
def menu_exis_vip():
    while True:
        functions.clear()
        print("=" * functions.cant_caracter)
        print('Hola, usuario VIP. ¿Qué deseas hacer?'.center(functions.cant_caracter, ' '))
        print("=" * functions.cant_caracter)
        print("[1] Necesito un nuevo token")
        print("[2] Soporte en línea")
        print('[3] Volver al menú')
        print("=" * functions.cant_caracter)
        
        opcion = input(">>> ")

        if opcion == "1":
            return vip_pago()
        elif opcion == "2":
            soporte()
        elif opcion == "3":
            Menu.menu()
        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

# Función para proporcionar soporte en línea
def soporte():
    print("=" * functions.cant_caracter)
    print('Ingresa tu correo electrónico:\n(Ingresa "salir" para volver al menú)')
    print("=" * functions.cant_caracter)
    user_mail = input('>>> ')
    
    if user_mail == 'salir' or user_mail == 'Salir' or user_mail == 'SALIR':
        if not estado_vip:
            return menu_vip()
        else:
            return menu_exis_vip()
        
    email = 'nutrifit765@gmail.com'
    try:
        print("=" * functions.cant_caracter)
        print('Ingresa tu mensaje, y pronto te contactaremos:')
        print("=" * functions.cant_caracter)
        message = input()
        
        contrasenia = 'Prueba1235'
        yag = yagmail.SMTP(user = email, password=contrasenia)
        asunto = 'Token VIP - NutriFit'
        mensaje = tokens
        yag.send = (user_mail, asunto, mensaje)

        return print("Mensaje exitosamente enviado")
    except:
        return print('Hubo un error, prueba nuevamente más tarde.')
