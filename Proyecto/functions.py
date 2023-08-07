import json, os, webbrowser, Menu, gym_fuctions, function_vip
from pathlib import Path
'''
NutriFit
'''

cant_caracter = 48
user = {'edad': '', 'peso_actual': '', 'medida': '', 'genero': ''}

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
     os.system("clear")

def add():
    clear()
    print('Estos son los datos actuales/cargados del usuario')
    print(user)

    print("Introduce tu edad:")
    user['edad'] = int(input())

    print("Introduce tu peso actual en KG:")
    user['peso_actual'] = float(input())

    print("Introduce tu medida en CM: (Ej: 170)")
    user['medida'] = float(input())

    print("Introduce tu sexo: (F (Femenino) o M (Masculino))")
    user['genero'] = str(input())

    with open ('Proyecto/user.json', 'w') as f:
        json.dump(user, f, indent = 4, sort_keys= True)
    return 

def al_recom():
    try:
        with open('Proyecto/user.json') as f:
            data = json.load(f)
        with open('Proyecto/alimentacion.json') as ff:
            data_2 = json.load(ff)
    except:
        print("Archivo no encontrado")
    
    print("Alimentación recomendada:\n(Puede variar dependiendo de cada persona)")
    if data['edad'] <= 16:
        print(data_2["m_16"])
    elif data['edad'] > 16 and data['edad'] <= 30:
        print(data_2["m_30"])
    elif data['edad'] > 30 and data['edad'] <= 65:
        print(data_2["m_65"])
    elif data['edad'] > 65:
        print(data_2["mm_65"])
        
def ejercicios_recomendados_edad():
    clear()
    try:
        with open('Proyecto/user.json', 'r') as f:
            data = json.load(f)
        with open('Proyecto/ejercicios.json', 'r') as ff:
            data_2 = json.load(ff)
    except:
        print('El archivo no fue encontrado')

    print("Rutina de ejercicios recomendada:")
    if data['edad'] <= 16:
        print(data_2["m_16"])
    elif data['edad'] > 16 and data['edad'] <= 30:
        print(data_2["m_30"])
    elif data['edad'] > 30 and data['edad'] <= 65:
        print(data_2["m_65"])
    elif data['edad'] > 65:
        print(data_2["mm_65"])

def media_intensidad():
    clear()
    print('Elija la intensidada del ejercicio: \n[1] Baja\n[2] Media\n[3] Alta')
    opcion = int(input('<<<'))
    try:
        with open('Proyecto/ejercicios.json', 'r') as f:
            ejer = json.load(f)
    except:
        print('El archivo no fue encontrado')
    if opcion == 1:
        clear()
        print('Esta es la rutina orientada en una dificutad baja:')
        print(ejer["abdominales_principiante"])
    elif opcion == 2:
        clear()
        print('Esta es la rutina orientada en una dificultad media:')
        print(ejer["abodminales_intermedio"])
    elif opcion ==3:
        clear()
        print('Esta es la rutina orientada en una dificultad alta:')
        print(ejer["abdominales_dificil"])

def baja_intensidad():
    clear()
    print('Elija la intensidada del ejercicio:\n[1] Baja\n[2] Media\n[3] Alta')
    opcion = int(input('<<<'))
    try:
        with open('Proyecto/ejercicios.json', 'r') as ff:
            ejer = json.load(ff)
    except:
        print('El archivo no fue encontrado')
    if opcion == 1:
        clear()
        print('Esta es la rutina orientada en una dificutad baja:')
        print(ejer["inferiro_principiante"])
    elif opcion == 2:
        clear()
        print('Esta es la rutina orientada en una dificultad media:')
        print(ejer["inferior_intermedio"])
    elif opcion ==3:
        clear()
        print('Esta es la rutina orientada en una dificultad alta:')
        print(ejer["inferior_difici"])

def alta_intensidad():
    clear()
    print('Elija la intensidada del ejercicio:\n[1] Baja\n[2] Media\n[3] Alta')
    opcion = int(input('<<<'))
    try:
        with open('Proyecto/ejercicios.json', 'r') as fff:
            ejer = json.load(fff)
    except:
        print('El archivo no fue encontrado')
    if opcion == 1:
        clear()
        print('Esta es la rutina orientada en una dificutad baja:')
        print(ejer["superior_principiante"])
    elif opcion == 2:
        clear()
        print('Esta es la rutina orientada en una dificultad media:')
        print(ejer["superior_intermedio"])
    elif opcion ==3:
        clear()
        print('Esta es la rutina orientada en una dificultad alta:')
        print(ejer["superior_dificil"])

def menu_selec():
    clear()
    print('Elija la zona a trabajar:\n[1] Zona media\n[2] Tren inferior\n[3] Tren superior')
    opcion = int(input('<<<'))
    if opcion == 1:
        media_intensidad()
    elif opcion ==2:
        baja_intensidad()
    elif opcion ==3:
        alta_intensidad()
    else:
        print('La opcion es incorrecta.')

def musica_menu():
    while True:
        clear()
        print("="*cant_caracter)
        print("¿Qué género musical desea escuchar?".center(cant_caracter,' '))
        print("="*cant_caracter)
        print("[1] Rock")
        print("[2] Blues")
        print("[3] Pop")
        print("[4] Trap")
        print("[5] Música Clásica")
        print("[6] Jazz")
        print("[7] Reggae")
        print("[8] Reggaeton")
        print("[9] Metal")
        print("[10] Electronica")
        print("[11] Volver al menú")
        print("="*cant_caracter)

        opcion = input(">>> ")

        playlists = {
            '1' : 'https://www.youtube.com/watch?v=1w7OgIMMRc4&list=PLZZPTrJOTP4avStrG1pC_bBURXoYr23Mj',
            '2' : 'https://www.youtube.com/watch?v=71Gt46aX9Z4&list=PLZZPTrJOTP4b3FNZzZ5ZvJFxnO6CNbYPZ',
            '3' : 'https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLZZPTrJOTP4YbDhmXiJTHJgfALsNjd4vj',
            '4' : 'https://www.youtube.com/watch?v=OWoMlr4bUQ4',
            '5' : 'https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PLZZPTrJOTP4bI1764qbCNwiew-DwOIoRR',
            '6' : 'https://www.youtube.com/watch?v=CWzrABouyeE&list=PLZZPTrJOTP4ZJ_flu1awpPRwXniwaq8FD',
            '7' : 'https://www.youtube.com/watch?v=OcaPu9JPenU&list=PLZZPTrJOTP4Yvl-VfPnqXeYC7R9dlbfpq',
            '8' : 'https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PLZZPTrJOTP4alwfy9KHudq6kzIYGn5ujX',
            '9' : 'https://www.youtube.com/watch?v=9d4ui9q7eDM&list=PLZZPTrJOTP4aRFhkb4VJA0ipWTEMD5xPu',
            '10' : 'https://www.youtube.com/watch?v=60ItHLz5WEA&list=PLZZPTrJOTP4bJN7CnJdMPWF0LnJobWvqk'
        }

        if opcion == "1":
            webbrowser.open_new_tab("{}".format(playlists['1']))
            Menu.menu()
        elif opcion == "2":
            webbrowser.open_new_tab("{}".format(playlists['2']))
            Menu.menu()
        elif opcion == "3":
            webbrowser.open_new_tab("{}".format(playlists['3']))
            Menu.menu()
        elif opcion == "4":
            webbrowser.open_new_tab("{}".format(playlists['4']))
            Menu.menu()
        elif opcion == "5":
            webbrowser.open_new_tab("{}".format(playlists['5']))
            Menu.menu()
        elif opcion == "6":
            webbrowser.open_new_tab("{}".format(playlists['6']))
            Menu.menu()
        elif opcion == "7":
            webbrowser.open_new_tab("{}".format(playlists['7']))
            Menu.menu()
        elif opcion == "8":
            webbrowser.open_new_tab("{}".format(playlists['8']))
            Menu.menu()
        elif opcion == "9":
            webbrowser.open_new_tab("{}".format(playlists['9']))
            Menu.menu()
        elif opcion == "10":
            webbrowser.open_new_tab("{}".format(playlists['10']))
            Menu.menu()
        elif opcion == "11":
            Menu.menu()
        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

def ShowProfile():
    clear()
    try:
        with open('Proyecto/user.json') as f:
            data = json.load(f)
    except:
        print('El archivo no fue encontrado')
    print(f'Su edad es ---{data["edad"]}---\nSu genero es ---{data["genero"]}---\nSu altura es de ---{data["medida"]}---\nSu peso actual es de ---{data["peso_actual"]}---')

def menu_gym():
    while True:
        clear()
        print("="*cant_caracter)
        print("¿Qué desea hacer?".center(cant_caracter,' '))
        print("="*cant_caracter)
        print("[1] Ver gimnasios adheridos")
        print("[2] Adherir tu gimnasio a HomeFitness [VIP]")
        print("[3] Reservar turno")
        print("[4] Ver mis turnos")
        print("[5] Volver al menú")
        print("="*cant_caracter)

        opcion = input(">>> ")

        if opcion == "1":
            gym_fuctions.gym_ad()
        elif opcion == "2":
            if function_vip.estado_vip == False:
                print('Necesitas VIP para usar esta función')
            elif function_vip.estado_vip == True:
                gym_fuctions.add_gym()
        elif opcion == "3":
            gym_fuctions.reserva()
        elif opcion == "4":
                gym_fuctions.ver_turnos()
        elif opcion == "5":
            Menu.menu()
        else:
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")
        
        input("\nPresiona cualquier tecla para continuar...")