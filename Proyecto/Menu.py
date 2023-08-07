import functions, function_vip, vars_calors

'''--------------------------------------'''
def menu():
    functions.clear()
    while True:    
        print('='*functions.cant_caracter)
        print('NutriFit'.center(functions.cant_caracter,' '))
        print('='*functions.cant_caracter)
        print('[1] Ingrese/Actualiza datos del usuario')
        print('[2] Empezar rutina de ejercicios')
        print('[3] Ver rutinas de ejercicio segun tu edad')
        print('[4] Ver Alimentacion recomendada segun tu edad ')
        print('[5] Ver datos del usuario')
        print('[6] Ver seguimiento [VIP]')
        print('[7] Reproducir musica')
        print('[8] Chat Bot - **** [En proceso]')
        print('[9] Opciones VIP ')
        print('[10] GYM adheridos')
        print('[0] Salir')
        
        opcion = int(input('>>>'))

        if opcion == 1:
            functions.add()
        elif opcion == 2:
            functions.menu_selec()
        elif opcion == 3:
            functions.ejercicios_recomendados_edad()
        elif opcion == 4:
            functions.al_recom()
        elif opcion == 5:
            functions.ShowProfile()
        elif opcion == 6:
            if function_vip.estado_vip == False:
                print('Necesitas VIP para usar esta función')
            elif function_vip.estado_vip == True:
                vars_calors.opciones_seg()
        elif opcion == 7:
            functions.musica_menu()
        elif opcion == 8:
            if function_vip.estado_vip == False:
                print('Necesitas VIP para usar esta función')
        elif opcion == 9:
            if function_vip.estado_vip == False:
                function_vip.menu_vip()
            elif function_vip.estado_vip == True:
                function_vip.menu_exis_vip()
        elif opcion == 10:
            functions.menu_gym()
        elif opcion == 0:
            print('Gracias por usar nuestro programa y contar con nuestros servicios')
            break
        else:
            print(f'La opcion que ingreso es invalida, por favor vuelva a ingresar una opcion')
'''--------------------------------------'''