import tkinter as tk

def click_boton(valor):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + str(valor))

def limpiar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

screen = tk.Tk()
screen.title("Calculadora")
screen.geometry("350x500")
screen.iconbitmap(r"C:\Users\jdaniel\Documents\1-Python\12-Tkinter\calculadora.ico")

# Screen
pantalla = tk.Entry(screen, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right", bg="#90ee90", fg="#222222")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        tk.Button(screen, text=texto, width=5, height=2, font=("Arial", 16), command=calcular).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(screen, text=texto, width=5, height=2, font=("Arial", 16), command=lambda t=texto: click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)

# Botón de limpiar
tk.Button(screen, text="C", width=5, height=2, font=("Arial", 16), command=limpiar).grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

screen.mainloop()