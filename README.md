#Calculadora de Índice de Masa Corporal (IMC) - Proyecto Modulo 1
## DESCRIPCIÓN DEL PROYECTO
Programa ejecutable en consola/terminal desarrollado en Python como proyecto. El código solicita al usuario datos personales (nombre, apellido paterno, apellido materno, edad y estatura) para calcular su índice de masa corporal (IMC) siguiendo la fórmula:
peso / estatura2   -> Peso sobre estatura al cuadrado
Además cuenta con cilos de validación para asegurar que ningún dato quede vació antes de realizar los cálculos y mostar el resumen final en pantalla.

DESARROLLO DEL PROGRAMA

Utilicé la función input() para solicitar cada dato en la terminal
Implementé ciclo While not variable después de cada entrada para validar que el usuario no deje ningún campo vacío. Si el usuario presion enter sin escribir nada, el programa muestra un mensaje de advertencia y vuelve a solicitar el dato.
Para poder aplicar operaciones matemáticas, convertí las entradas de texto del peso y estatura a valores decimales utilizando la funcion float()
Desplegué un bloque formateado con la lista de datos registrados y el valor del IMC utilizando f-strings y formato de redondeo :.2f para mostrar únicamente los decimales

REFLEXIONES

Comprendí las bases de la programación estructurada en Python, el uso correcto de algunas variables, la interacción del usuario desde la consola
Control del flujo del programa mediante ciclos e instrucciones condicionales.
La estructuración de validaciones con ciclos while para que el programa fuera interactivo y no permitiera continuar hasta que estuviera completo fue un gran reto.
Me siento satisfecha con el aprendizaje hasta hoy aun que sé que debo mejorar en la sintaxis, y entiendo que aún falta mucho conocimiento por aprender.

## Código fuente del programa 
```python
print(" --- CALCULADORA DE IMC ---")

print ()

#1.PEDIR DATOS PERSONALES (validar que no queden vacios)
nombre = input("Ingrese su nombre: ")
while not nombre:
    print("El nombre no puede estar vacío.")
    nombre = input("Ingrese su nombre: ")

apellido_paterno = input("Ingrese su apellido paterno: ")
while not apellido_paterno:
    print("El apellido paterno no puede estar vacío.")
    apellido_paterno = input("Ingrese su apellido paterno: ")

apellido_materno = input("Ingrese su apellido materno: ")
while not apellido_materno:
    print("El apellido materno no puede estar vacío.")
    apellido_materno = input("Ingrese su apellido materno: ")

edad = input("Ingrese su edad: ")
while not edad:
    print("La edad no puede estar vacía.")
    edad = input("Ingrese su edad: ")

peso = input("Ingrese su peso (kg): ")
while not peso:
    print("El peso no puede estar vacío.")
    peso = input("Ingrese su peso (kg): ")

estatura = input("Ingrese su estatura (m): ")
while not estatura:
    print("La estatura no puede estar vacía.")
    estatura = input("Ingrese su estatura (m): ")

#Convertimos el texto a numero decimal
estatura = float(estatura)
peso = float(peso)

#CALCULO DEL IMC
imc = peso / (estatura ** 2)

#MOSTRAR RESULTADOS EN PANTALLA
print()
print("===========================")
print("     DATOS REGISTRADOS     ")
print("===========================")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
```
