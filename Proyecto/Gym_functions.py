import functions, Menu
import webbrowser, calendar, json
from datetime import date

# Diccionario que almacena nombres de gimnasios y sus sitios web correspondientes
gym = {'Megatlon':'https://www.megatlon.com/', 
       'Briskbox':'https://www.briskbox.fit/', 
       'Zoom Fitness':'https://www.instagram.com/zoomfitnesscenter/', 
       'Pulso Gym':'https://www.facebook.com/PulsogGym/'}

values = gym.values()
gymlist = [*gym]
pagelist = list(values)

# Función para mostrar los gimnasios adheridos
def gym_ad():
    functions.clear()    
    values = gym.values()
    gymlist = [*gym]
    pagelist = list(values)

    print("="*functions.cant_caracter)
    print('Gimnasios adheridos - ¿Cuál desea ver?'.center(functions.cant_caracter,' '))
    print('='*functions.cant_caracter)
    for j in range(len(gym)):
        print(f'[{j+1}] {gymlist[j]}')
    print(f'[{len(gym)+1}] Volver al menú')
    print('='*functions.cant_caracter)

    opcion = input(">>> ")
        
    for i in range(len(gymlist)):
        if opcion == f"{i+1}":
            webbrowser.open_new_tab(f"{pagelist[i]}")
            Menu.menu()
        elif opcion == f"{len(gymlist)+1}":
            Menu.menu()
        elif int(opcion) > len(gymlist):
            print("Has ingresado una opción incorrecta. Intenta nuevamente.")

    input("\nPresiona cualquier tecla para continuar...")

# Función para agregar un gimnasio
def add_gym():
    functions.clear()
    print("="*functions.cant_caracter)
    print('Añadir tu gimnasio'.center(functions.cant_caracter,' '))
    print('Requisitos obligatorios'.center(functions.cant_caracter,' '))
    print('='*functions.cant_caracter)
    
    gym_name = input("Introduce el nombre del gimnasio:\n>>> ")
    gym_page = input("Introduce un sitio web del gimnasio:\nEjemplo: https://www.tugimnasio.com/\n>>> ")
    
    gym[gym_name] = gym_page

# Función para reservar un turno
def reserva():
    today = date.today()
    range_month = str(calendar.monthrange(today.year, today.month))
    rango_mes = int(range_month[4:6])
    while True:
        functions.clear()
        print("="*functions.cant_caracter)
        print("Reservar turno - Elige un gimnasio".center(functions.cant_caracter,' '))
        print("="*functions.cant_caracter)
        for j in range(len(gym)):
            print(f'[{j+1}] {gymlist[j]}')
        print(f'[{len(gym)+1}] Volver al menú')
        print("="*functions.cant_caracter)

        opcion = input(">>> ")
        
        for i in range(len(gymlist)):
            if opcion == f"{i+1}":
                print(calendar.month(today.year, today.month))
                print('\nElige un día para el turno')
                while True:
                    dia_turno = int(input('Abierto todos los días del mes\n>>> '))
                    if dia_turno > rango_mes or isinstance(dia_turno, str):
                        print("Has ingresado una opción incorrecta, prueba nuevamente")
                    else:
                        turno = f'> {dia_turno}/{today.month}/{today.year} - {gymlist[i]}'
                        with open('Proyecto/turnos.txt', 'a') as f:
                            json.dump(turno, f)
                        break
                    input("\nPresiona cualquier tecla para continuar...")   

            elif opcion == f"{len(gymlist)+1}":
                Menu.menu()
            elif int(opcion) > len(gymlist):
                print("Has ingresado una opción incorrecta. Intenta nuevamente.")

        input("\nPresiona cualquier tecla para continuar...")

# Función para ver los turnos reservados
def ver_turnos():
    print("="*functions.cant_caracter)
    print("Estos son tus turnos".center(functions.cant_caracter,' '))
    print("="*functions.cant_caracter)
    
    with open('Proyecto/turnos.txt', 'r') as f:
        contents = f.read()
    print(contents.rstrip().strip('"'))
