import tkinter as tk
import random


def generar_puntos(num_puntos, canvas_width, canvas_height):
    puntos = [(random.randint(0, canvas_width), random.randint(0, canvas_height)) for _ in range(num_puntos)]
    return puntos


def punto_dentro_del_circulo(x, y, centro_x, centro_y, radio):
    distancia = ((x - centro_x) ** 2 + (y - centro_y) ** 2) ** 0.5
    return distancia <= radio


def dibujar_cuadrado_circulo_puntos():
    num_puntos = int(entry_num_puntos.get())

    canvas.delete("all")

    centro_x, centro_y = canvas_width // 2, canvas_height // 2
    radio = min(canvas_width, canvas_height) // 2

    canvas.create_rectangle(0, 0, canvas_width, canvas_height, outline="black")


    canvas.create_oval(centro_x - radio, centro_y - radio, centro_x + radio, centro_y + radio, outline="black")

    puntos_dentro = 0
    for punto in generar_puntos(num_puntos, canvas_width, canvas_height):
        x, y = punto
        if punto_dentro_del_circulo(x, y, centro_x, centro_y, radio):
            puntos_dentro += 1
            canvas.create_oval(x, y, x+1, y+1, fill="blue")
        else:
            canvas.create_oval(x, y, x+1, y+1, fill="red")


    pi_aproximado = (puntos_dentro / num_puntos) * 4


    resultados_label.config(text=f"Puntos dentro del círculo: {puntos_dentro}/{num_puntos}")
    aproximacion_label.config(text=f"Aproximación de π: {pi_aproximado:.5f}")


root = tk.Tk()
root.title("Método Montecarlo")


label_num_puntos = tk.Label(root, text="Número de Puntos:")
label_num_puntos.pack()

entry_num_puntos = tk.Entry(root)
entry_num_puntos.pack()


btn_mostrar_puntos = tk.Button(root, text="Mostrar Puntos", command=dibujar_cuadrado_circulo_puntos)
btn_mostrar_puntos.pack()


canvas_width, canvas_height = 400, 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()


resultados_label = tk.Label(root, text="")
resultados_label.pack()

aproximacion_label = tk.Label(root, text="")
aproximacion_label.pack()

root.mainloop()
