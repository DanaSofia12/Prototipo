# La "base de datos"
clientes = []
agendarTrabajos = []
trabajosRealizados = []
# Funcion para mostrar menu principal
def menuPrincipal():
    print("----- Menú Principal -----")
    print("1. Datos de Cliente")
    print("2. Agendar Trabajos")
    print("3. Trabajos Realizados")
    print("4. Cerrar Sesión")
    print("-----------------------")


# Funcion para mostrar menu de los datos de cliente
def menuDatosCliente():
    print("-----Menú Datos de Cliente-----")
    print("1. Crear Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Buscar Cliente")
    print("5. Volver al Menú Principal")
    print("-----------------------")


# Funciones para gestionar los datos de cliente

# Funcion para crear los datos de un cliente
def crearCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion}
    clientes.append(cliente)
    print("Cliente creado con éxito.")

# Funcion para eliminar algun cliente
def eliminarCliente():
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    telefono = input("Ingrese el número de teléfono del cliente a eliminar: ")
    direccion = input("Ingrese la dirección del cliente a eliminar: ")
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
        }
    if cliente in clientes:
        clientes.remove(cliente)
        print("Cliente eliminado con éxito.")
    else:
        print("El cliente no existe.")

# Funcion para modificar algun cliente
def modificarCliente():
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    telefono = input("Ingrese el número de teléfono del cliente a modificar: ")
    direccion = input("Ingrese la dirección del cliente a modificar: ")
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
        }
    if cliente in clientes:
        nuevoNombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevoTelefono = input("Ingrese el nuevo número de teléfono del cliente: ")
        nuevaDireccion = input("Ingrese la nueva dirección del cliente: ")
        nuevoCliente = {
            "nombre": nuevoNombre,
            "telefono": nuevoTelefono,
            "direccion": nuevaDireccion}
        buscarParaModificar = clientes.index(cliente)
        clientes[buscarParaModificar] = nuevoCliente
        print("Cliente modificado con éxito.")
    else:
        print("El cliente no existe.")

# Funcion para buscar algu cliente
def buscarCliente():
    nombre = input("Ingrese el nombre del cliente a buscar: ")
    telefono = input("Ingrese el número de teléfono del cliente a buscar: ")
    direccion = input("Ingrese la dirección del cliente a buscar: ")
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }
    if cliente in clientes:
        print("Cliente encontrado:")
        print("Nombre: " + cliente["nombre"])
        print("Teléfono: " + cliente["telefono"])
        print("Dirección: " + cliente["direccion"])
    else:
        print("El cliente no existe.")
# Hasta aqui funciones de gestionar datos de cliente

# Funcion para mostrar el menu principal
def menu():

    while True:
        menuPrincipal()
        opcionMenuPrincipal = input("Seleccione una opción: ")

        if opcionMenuPrincipal == "1":
            while True:
                menuDatosCliente()
                opcionDatosCliente = input("Seleccione una opción: ")
                if opcionDatosCliente == "1":
                    crearCliente()
                elif opcionDatosCliente == "2":
                    modificarCliente()
                elif opcionDatosCliente == "3":
                    eliminarCliente()
                elif opcionDatosCliente == "4":
                    buscarCliente()
                elif opcionDatosCliente == "5":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")            

        elif opcionMenuPrincipal == "2":
                print("Agendar trabajos")
        elif opcionMenuPrincipal == "3":
                print("Trabajos realizados")
        elif opcionMenuPrincipal == "4":
            print("Sesión a sido cerrada correctamente.")
            print("¡Vuelva pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def inicioDeSesion():
    Usuario = "admin"
    Contraseña = "12345"
    i = 0
    while i < 3:
        usuario=str(input("Usuario: "))
        contraseña=str(input("Contraseña: "))
        if usuario == Usuario and contraseña==Contraseña:
            print("Ingreso al sistema correctamente")
            menu()
            return
        else:
            i += 1
            print("Nombre de usuario o contraseña incorrectos.")
            print(f"Intentos restantes: {3 - i}")
    print("Has excedido el número máximo de intentos. Has sido expulsado del software.")

inicioDeSesion()