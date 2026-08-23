print("Hello Word, bienvenido al curso de Fundamentos de Python")
print("Este es mi primer script de python")
altura = int(input("¿De qué altura quieres la pirámide? "))

if altura > 0:
    for fila in range(1, altura + 1):
        espacios = " " * (altura - fila)
        asteriscos = "* " * fila
        print(espacios + asteriscos)
else:
    print("La altura debe ser un número entero positivo.")