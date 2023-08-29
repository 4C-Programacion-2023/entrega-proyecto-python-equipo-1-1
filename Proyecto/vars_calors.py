import Menu, functions

comidas = []

diccionario_comidas = {
    'arroz' : 140,
    'atun' : 200,
    'banana' : 89,
    'batata' : 101,
    'berenjena' : 25,
    'brocoli' : 34,
    'canelones' : 158,
    'carne' : 143,
    'chocolate' : 539,
    'chorizo' : 455,
    'churros' : 481,
    'ensalada' : 65,
    'empanada' : 335,
    'flan' : 177,
    'frutilla' : 35,
    'galletas' : 460,
    'hamburguesa' : 220,
    'helado' : 209,
    'lentejas' : 310,
    'magdalena' : 397,
    'milanesa' : 192,
    'naranja' : 47,
    'ñoquis' : 133,
    'fideos' : 157,
    'pollo' : 89,
    'ravioles' : 106,
    'salchichas' : 367,
    'yogur' : 106,
    'zanahoria' : 41
}


def opciones_seg():
    functions.clear()
    print("="*functions.cant_caracter)
    print("Que deseas hacer?".center(functions.cant_caracter,' '))
    print("="*functions.cant_caracter)
    print("[1] Ingresar comidas del dia")
    print("[2] Ver calorías totales")
    print("[3] Volver al menú")
    print("="*functions.cant_caracter)

    opcion = input(">>> ")

    if opcion == "1":
        seguimiento_cal()
    elif opcion == "2":
        ver_calorias()
    elif opcion == "3":
        Menu.menu()
    else:
        print("Ingresa una opción correcta")
        opciones_seg()
        


def seguimiento_cal():
    print("Ingresa de a una, todas tus comidas del día (Ej: milanesa). Ingresa Salir para terminar el proceso:")
    while True:
        global comida
        comida = input()
        if not comida in diccionario_comidas and comida != 'salir' and comida != 'Salir' and comida != 'SALIR':
            print('Esa comida no la tenemos registrada.')            
        elif comida == "salir" or comida == "Salir" or comida == "SALIR":
            break
        else:
            comidas.append(comida.lower())


def ver_calorias():
    calorias = 0
    
    for i in comidas:
        if i in diccionario_comidas:
            calorias += diccionario_comidas.get(i)

    print("Las calorías totales son:", calorias)