import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


a = 0
b = 2
n = 10


def f(x):
    return x**2 + math.sin(x)


def lagrange_polynomial(x, x_nodes, y_nodes):
    result = 0

    for i in range(len(x_nodes)):
        term = y_nodes[i]
        for j in range(len(x_nodes)):
            if j != i:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term

    return result


def calculate():
    for row in table.get_children():
        table.delete(row)

    h = (b - a) / n

    x_nodes = []
    y_nodes = []

    for i in range(n + 1):
        x_i = a + h * i
        y_i = f(x_i)
        x_nodes.append(x_i)
        y_nodes.append(y_i)

        table.insert(
            "",
            "end",
            values=(i, round(x_i, 4), round(y_i, 4))
        )

    x_plot = np.linspace(a, b, 400)

    y_real = []
    y_lagrange = []

    for x in x_plot:
        y_real.append(f(x))
        y_lagrange.append(lagrange_polynomial(x, x_nodes, y_nodes))

    plt.figure()
    plt.plot(x_plot, y_real, label="f(x)")
    plt.plot(x_plot, y_lagrange, label="Поліном Лагранжа")
    plt.scatter(x_nodes, y_nodes)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


root = tk.Tk()
root.title("Поліном Лагранжа")
root.geometry("750x500")

tk.Label(
    root,
    text="Інтерполяція функції поліномом Лагранжа"
).pack(pady=5)

tk.Label(
    root,
    text="f(x) = x² + sin(x)"
).pack(pady=5)

tk.Button(
    root,
    text="Обчислити",
    command=calculate
).pack(pady=10)

columns = ("i", "x", "f(x)")
table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center")

table.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()
