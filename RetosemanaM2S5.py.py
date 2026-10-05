#If - else

print("El año actual es 2026")

anio_actual = int(input("Introduce el año actual:"))
anio_otro = int(input("Introduce otro año para calcular:"))
diferencia = abs(anio_actual - anio_otro)


if anio_otro < anio_actual:
    if diferencia == 1:
        print(f"Desde el año {anio_otro} ha pasado 1 año")

    else: 
        print(f"Han pasado {diferencia} años desde el año que has introducido")
        
elif anio_otro > anio_actual:
    if diferencia == 1:
        print(f"Para llegar a {anio_otro} hace falta 1 año")
    else: 
        print(f"Faltan {diferencia} años para llegar al año que has introducido")
else:
    print("Has introducido el mismo año que el actual")
