def inicioDeSesion():
    Usuario = "admin"
    Contraseña = "12345"
    i = 0
    while i < 3:
        usuario=str(input("Ingrese su usuario: "))
        contraseña=str(input("Ingrese su contraseña: "))
        if usuario == Usuario and contraseña==Contraseña:
            print("Ingreso al sistema correctamente")
            return
        else:
            i += 1
            print("Nombre de usuario o contraseña incorrectos.")
            print(f"Intentos restantes: {3 - i}")
    print("Has excedido el número máximo de intentos. Has sido expulsado del software.")
    
inicioDeSesion()
