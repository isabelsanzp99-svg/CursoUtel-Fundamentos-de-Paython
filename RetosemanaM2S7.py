lista = []

alumnos = 0

while True:
    opcion = input("Agregar alumno (1) o terminar (2): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calificaciones = []

        while len(calificaciones) < 3:
            num_calif = len(calificaciones) + 1

            if len(calificaciones) >=1:
                preg = input(f"¿Desea ingresar la calificación {num_calif} para {nombre}? (s/n): ").lower()
                if preg != "s":
                    break

            try:
                calif = float(input(f"Ingrese la calificación {num_calif} de {nombre}:"))
                calificaciones.append(calif)
            except ValueError:
                print("Por favor, ingrese un número válido.")

        lista.append([nombre, calificaciones])
        alumnos +=1

    elif opcion == "2":
        print(f"\nEl programa ha terminado con {alumnos} alumnos.")
        break
    else:
        print("Se ha ingresado una opción invalida.")

print("\n---Resultados---")
for alumno in lista:
    nombre_alumno = alumno[0]
    cals = alumno[1]
    promedio = sum(cals) / len(cals)
    print(f"Alumno: {nombre_alumno} | Promedio: {promedio:.2f}")


                
       