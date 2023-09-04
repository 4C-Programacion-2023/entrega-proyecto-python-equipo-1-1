# Importa los módulos necesarios desde los archivos Menu y functions.
import Menu, functions

# Lista para almacenar las comidas ingresadas por el usuario.
comidas = []

# Diccionario que contiene los valores calóricos de algunas comidas.
diccionario_comidas = {
    'arroz': 140,
    'atun': 200,
    'banana': 89,
    'batata': 101,
    'berenjena': 25,
    'brocoli': 34,
    'canelones': 158,
    'carne': 143,
    'chocolate': 539,
    'chorizo': 455,
    'churros': 481,
    'ensalada': 65,
    'empanada': 335,
    'flan': 177,
    'frutilla': 35,
    'galletas': 460,
    'hamburguesa': 220,
    'helado': 209,
    'lentejas': 310,
    'magdalena': 397,
    'milanesa': 192,
    'naranja': 47,
    'ñoquis': 133,
    'fideos': 157,
    'pollo': 89,
    'ravioles': 106,
    'salchichas': 367,
    'yogur': 106,
    'zanahoria': 41
}

# Función que muestra las opciones de seguimiento de calorías.
def opciones_seg():
    # Limpia la pantalla.
    functions.clear()
    
    # Muestra el menú de opciones.
    print("=" * functions.cant_caracter)
    print("¿Qué deseas hacer?".center(functions.cant_caracter, ' '))
    print("=" * functions.cant_caracter)
    print("[1] Ingresar comidas del día")
    print("[2] Ver calorías totales")
    print("[3] Volver al menú")
    print("=" * functions.cant_caracter)

    # Lee la opción ingresada por el usuario.
    opcion = input(">>> ")

    # Realiza acciones en función de la opción seleccionada.
    if opcion == "1":
        seguimiento_cal()
    elif opcion == "2":
        ver_calorias()
    elif opcion == "3":
        Menu.menu()
    else:
        print("Ingresa una opción correcta")
        opciones_seg()

# Función para realizar el seguimiento de comidas del día.
def seguimiento_cal():
    print("Ingresa de a una, todas tus comidas del día (Ej: milanesa). Ingresa 'Salir' para terminar el proceso:")
    while True:
        global comida
        comida = input()
        # Verifica si la comida no está en el diccionario de comidas.
        if not comida in diccionario_comidas and comida != 'salir' and comida != 'Salir' and comida != 'SALIR':
            print('Esa comida no la tenemos registrada.')            
        elif comida.lower() == "salir":
            break
        else:
            comidas.append(comida.lower())

# Función para calcular y mostrar las calorías totales de las comidas ingresadas.
def ver_calorias():
    calorias = 0
    
    for i in comidas:
        if i in diccionario_comidas:
            calorias += diccionario_comidas.get(i)

    print("Las calorías totales son:", calorias)