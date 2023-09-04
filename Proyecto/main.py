#Para usar el programa se debe tener instalado el browser de SQLite (SQLiteDatabaseBrowserPortable_3.12.2_English.paf) y SQLite3

# Importa el módulo Menu que contiene la función para mostrar el menú principal.
import Menu

# Función principal que inicia la ejecución del programa.
def main():
    # Llama a la función menu() del módulo Menu para mostrar el menú principal.
    Menu.menu()

# Comprueba si este script se está ejecutando directamente, no importado como módulo.
if __name__ == "__main__":
    # Si se ejecuta directamente, llama a la función main() para iniciar el programa.
    main()
