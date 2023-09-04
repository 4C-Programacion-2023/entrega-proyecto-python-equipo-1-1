import functions, function_vip, vars_calors, index

'''--------------------------------------'''

# Define una función llamada "menu" que muestra un menú de opciones al usuario.
def menu():
    while True:

        # Imprime una línea de igual (=) que abarca el ancho de la pantalla definido en "functions.cant_caracter".
        print('='*functions.cant_caracter)

        # Imprime "NutriFit" centrado en la pantalla, dentro de una línea de igual.
        print('NutriFit'.center(functions.cant_caracter,' '))

        # Imprime otra línea de igual para separar.
        print('='*functions.cant_caracter)

        # Muestra las opciones del menú numeradas.
        print('[1] Ingrese/Actualiza datos del usuario')
        print('[2] Empezar rutina de ejercicios')
        print('[3] Ver rutinas de ejercicio segun tu edad')
        print('[4] Ver Alimentacion recomendada segun tu edad ')
        print('[5] Ver seguimiento [VIP]')
        print('[6] Reproducir musica')
        print('[7] Opciones VIP ')
        print('[8] GYM adheridos')
        print('[9] Salir')

        # Solicita al usuario que ingrese una opción.
        opcion = int(input('>>>'))

        # Maneja diferentes opciones según lo que ingrese el usuario.
        if opcion == 1:
            index.add()
        elif opcion == 2:
            functions.menu_selec()
        elif opcion == 3:
            functions.ejercicios_recomendados_edad()
        elif opcion == 4:
            functions.al_recom()
        elif opcion == 5:
            if function_vip.estado_vip == False:
                print('Necesitas VIP para usar esta función')
            elif function_vip.estado_vip == True:
                vars_calors.opciones_seg()
        elif opcion == 6:
            functions.musica_menu()
        elif opcion == 7:
            if function_vip.estado_vip == False:
                print('Necesitas VIP para usar esta función')
        elif opcion == 8:
            if function_vip.estado_vip == False:
                function_vip.menu_vip()
            elif function_vip.estado_vip == True:
                function_vip.menu_exis_vip()
        elif opcion == 9:
            functions.menu_gym()
        elif opcion == 10:
            print('Gracias por usar nuestro programa y contar con nuestros servicios')
            break
        else:
            print(f'La opcion que ingreso es invalida, por favor vuelva a ingresar una opcion')

'''--------------------------------------'''
