"""
Exploracion de variables string y sus metodos
"""

#Definicion de variables string

nombre = "Mariano"

print(nombre)
print(nombre[0]) #Imprime la primera letra de la variable nombre
print(nombre[-1]) #Imprime la ultima letra de la variable nombre
print(nombre[0:3]) #Imprime las primeras tres letras de la variable nombre

#Indexacion de caracteres en strings
nombre="Mariano"
print(nombre[0]) #Muestra la rpimera letra
print(nombre[-1]) #Muestra la ultima letra
print(nombre[1:4]) #Muestra las letras desde la posicion 1 hasta la 3

#Inmutabilidad de las variables string
print("caracter a cambiar", nombre[-1])
nombre = nombre[:-1] + "a"

#Slicing de strings
print(nombre[1:4]) #Muestra las letras desde la posicion 1 hasta la 3

#Operaciones con strings

#Upper cambia todas las letras a mayusculas
print(nombre.upper()) #Muestra el string en mayusculas 

#Lower cambia todas las letras a minusculas
print(nombre.lower()) #Muestra el string en minusculas

#Title cambia la primera letra de cada palabra a mayuscula
print("y cuando desperté, el dinosaurio seguia ahi".title()) #Muestra el string con la primera letra de cada palabra en mayus

#Strip, lstrio y rstrip eliminan espacios en blanco al inicio y al final del string
nombre = "Isabel "
print(nombre.rstrip() == "Isabel")

#Replace reemplaza un caracter por otro

enunciado = "El carro viejo de mi tio es muy feo"

print(enunciado.replace("feo", "bonito").replace("viejo", "nuevo")) #Muesstra el string con los cambios realizados

#Funciones de comprobacion de strings

variable = "10"
print(variable.isnumeric())
print(int(variable)+100)
print(variable.isalpha()) #isalpha() devuelve True si todos los caracteres de la cadena son letras y hay al menos un caracter, de lo contrario devuelve False
print(variable.isalnum()) #isalnum() devuelve True si todos los caracteres de la cadena son alfanuméricos y hay al menos un caracter, de lo contrario devuelve False
print(variable.startswith("1")) #startswith() devuelve True si la cadena comienza con el prefijo especificado, de lo contrario devuelve False
print(variable.endswith("p")) #endswith() devuelve True si la cadena termina con el sufijo especificado, de lo contrario devuelve False
frase = "El perro de San Roque no tiene rabo"
print(frase.split(" "))

#print(variable+100)
