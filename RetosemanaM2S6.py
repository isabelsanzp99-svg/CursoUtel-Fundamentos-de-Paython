intentos = 0
max_intentos = 3
contraseña_valida = False
contraseña = ""

while intentos < max_intentos:
    if not contraseña_valida:
        contraseña = input("Ingrese una contraseña:")

        if len(contraseña) > 0 and contraseña[0].isdigit():
            contraseña_valida = True
        else:
            intentos += 1
            if intentos < max_intentos:
             print("La contraseña debe comenzar con un numero")

    else:
        confirmacion = input("Ingrese la contraseña nuevamente:")

        if confirmacion == contraseña:
            print("Contraseña correcta")
            break 
            
        else:
            intentos += 1
            if intentos < max_intentos:
                print("Las contraseñas no coinciden")

print("Fin del programa")