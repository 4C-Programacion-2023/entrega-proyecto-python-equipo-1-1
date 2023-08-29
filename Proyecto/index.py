import sqlite3,json,functions


def add():  
    functions.clear()
    conn = sqlite3.connect("usuarios.db") #Se conecta a la base de datos

    conn.execute('''CREATE TABLE IF NOT EXISTS user
    (edad INTEGER, peso INTEGER, medida REAL, genero VARCHAR, fechaHora DATETIME DEFAULT CURRENT_TIMESTAMP)''') #Crea la tabla user si no existe, con las siguientes columnas 

    user = {'edad': '', 'peso': '', 'medida': '', 'genero': ''} 

    cur = conn.cursor() # Creación de un objeto cursor para operaciones SQL
    query = cur.execute('''SELECT rowid, * FROM user''').fetchall() # Ejecución de una consulta para obtener todos los registros de la tabla 'user'
    cur.close()

    if len(query)!= 0:  # Verificación de si hay registros en la tabla
        ultimafila = query[-1]
    else:
        ultimafila = 0   # Verificación de si hay registros en la tabla

    generos = ["M","F","X"] #Lista de opciones de genero

    if ultimafila == 0:
        print("La tabla esta vacia")
        
        edad = input('Ingrese su edad > ')
        peso = input('Ingrese su peso > ')
        medida = input('Ingrese su medida > ')
        genero = input('Ingrese su genero (m para masculino - f para femenino - x para otros) > ') #Si la tabla esta vacia, pregunta los datos del usuario

        if genero.upper() not in generos: #Verificar si el genro ingresado es valido, de no serlo deja genero en blanco
            genero = ''
        conn.execute("INSERT INTO user (edad, peso, medida, genero) VALUES (?, ?, ?, ?)", ( edad, peso, medida, genero))   

    if ultimafila != 0 : 
        if ultimafila[1] != '' and ultimafila[2] != '' and ultimafila[3] != '' and ultimafila[4] != '':
        
            print("Edad: " + str(ultimafila[1]) +" Años - Peso: " +  str(ultimafila[2] )+" Kg - Medida: " +  str(ultimafila[3]) +" cm - Genero: " +  str(ultimafila[4]) ) # Imprimir información de la última fila
            edad = input('Ingrese su edad > ')
            peso = input('Ingrese su peso > ')
            medida = input('Ingrese su medida > ')
            genero = input ('Ingrese su genero (m para masculino - f para femenino - x para otros) > ') # Solicitar información actualizada al usuario

            if genero.upper() not in generos:
                genero = ''
            conn.execute("INSERT INTO user (edad, peso, medida, genero) VALUES (?, ?, ?, ?)", ( edad, peso, medida, genero)) # Insertar datos actualizados del usuario en la tabla "user"


        else:
            print("Ultima fila le faltan datos")
            print("Edad: " + str(ultimafila[1]) +" Años - Peso: " +  str(ultimafila[2] )+" Kg - Medida: " +  str(ultimafila[3]) +" cm - Genero: " +  str(ultimafila[4]) )
            if ultimafila[1] == '':   # Completar automáticamente los campos faltantes
                edad = input('Ingrese su edad > ')
            else:
                edad = ultimafila[1]

            if ultimafila[2] == '':
                peso = input('Ingrese su peso > ')
            else:
                peso = ultimafila[2]

            if ultimafila[3] == '':
                medida = input('Ingrese su medida > ')
            else:
                medida = ultimafila[3]

            if ultimafila[4] == '':
                genero = input('Ingrese su genero (m para masculino - f para femenino - x para otros) > ')
            else:
                genero = ultimafila[4]
            if genero.upper() not in generos:
                genero = ''
            with open('user.json', 'w') as f:
                json.dump(user, f, indent=4, sort_keys=True)
            conn.execute( "UPDATE user SET edad = ?, peso = ?, medida = ?, genero= ? WHERE rowid = ?", ( edad, peso, medida, genero, ultimafila[0])) # Actualizar la última fila con los datos completados
    conn.commit()
    conn.close() # Cerrar la conexión a la base de datos
