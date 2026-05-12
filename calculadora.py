#Importando nuestra librerio
import tkinter as tk
#Ventana 
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry ("400x800")
#Pantallla 
pantalla = tk.Entry(ventana,font=("Arial",20),borderwidth=5 ,relief="raised",justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#Para poder agregar numeros
def click (boton):
    pantalla.insert(tk.END,boton)

def limpiar():
    pantalla.delete(tk.END)

def calcular ():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0,tk.END)
        pantalla.insert(0,resultado)
    except:
        pantalla.delete(0,tk.END)
        pantalla.insert (0,"Error")
botones = [
    '7','8','9','/',
    '6','5','4','*',
    '3','2','1','-',
    '0','.','=','+'
]
fila = 1
columna = 0

for boton in botones :
    if boton == "=":
        tk.Button(ventana, text=boton, width=5, height=2, command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, width=5, height=2, command=lambda b=boton: click(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
tk.Button(ventana, text="C", width=22, height=2, command=limpiar).grid(row=5, column=0, columnspan=4)

ventana.mainloop()

