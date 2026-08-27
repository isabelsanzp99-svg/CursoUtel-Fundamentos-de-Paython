"""
Clase de Formulario 
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Formulario de Registro")
root.geometry("400x300")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

tk.Label(root, text="Carrera:").pack()
entry_carrera = tk.Entry(root)
entry_carrera.pack()



nombre = entry_nombre.get()
edad = entry_edad.get()
carrera = entry_carrera.get()

errores = []

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()

    if not nombre or not edad or not carrera:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    print("Datos Guardados")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Carrera: {carrera}")

tk.Button(root, text="Enviar", command=guardar_datos).pack()
root.mainloop() 

