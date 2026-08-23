"""
Clase 2 del curso de utel Python Fundamentos.
"""
#Variable:

Texto: Strings
#Numeros enteros: Integers (e.g. 1, 2, 3)
#Numeros decimales: Floats (e.g. 1.5, 2.7, 3.14)
#Booleanos: Booleans (e.g. True, False)
#lista: List (e.g. [1, 2, 3], ["a", "b", "c"])
#Tuplas: Tuples (e.g. (1, 2, 3), ("a", "b", "c"))
#Diccionarios: Dictionaries (e.g. {"key": "value"}, {"name": "John", "age": 30})

#Muchos mas tipos de datos y estructuras de datos en Python.


#Variables tipo int y string
print("Bienvenido al sistema")
nombre= input("Ingrese su nombre:")
edad= int(input("Ingrese su edad:"))

paridad = edad % 2 

edad_float = float(edad)
print("Usuario registrado con exito") 
print("Nombre:", nombre)
print("Edad:", edad)
print("Paridad:", paridad)
print("Edad como float:", edad_float)
print("Variable booleana: ", edad > 18)
mis_datos = {"nombre": nombre, "edad": edad, "paridad": paridad, "edad_float": edad_float, edad > 18: edad > 18}
mis_datos_tupla = (nombre, edad, paridad, edad_float, edad > 18)
mis_datos_diccionario = {"nombre": nombre, "edad": edad, "paridad": paridad, "edad_float": edad_float, "mayor_de_edad": edad > 18}


#Identificar el error

#Codigo con errores (para entregar a los alumnos)
Precio_base = 1000
descuento = "200"

print("El final es: " + str(Precio_base - int(descuento)))
