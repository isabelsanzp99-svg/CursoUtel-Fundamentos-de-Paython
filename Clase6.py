
# Ciclos For y While

# Ciclo For en un rango.
# for i in range(6):
#    print("Caja "+str(i)+' Procesada.') 

# Ciclo For en una lista.
#for i in ['Diego','Ana','Juan']:
#    print(f"Nombre del alumno : {i}")

# Suma de los primeros 1000 numeros.
#Suma = 0
#for i in range(1,1001):
#    print(f"El número que se va a sumar es {i}")
#    Suma = Suma+i

#print(f"La suma de los primeros 1000 números es: {Suma}")


#Ciclo while ejemplo
bateria = 100
pasos = 0
#while bateria > 0:
#    print(f"El robot ha dado {pasos} pasos y le queda {bateria} de batería.")
#    pasos += 1
#    bateria -= 10



while bateria < 1000:
    print(f"El robot ha dado {pasos} pasos y le queda {bateria} de batería.")
    pasos += 1
    bateria -= 10 