import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Подключаем привязки клавиш Matplotlib по умолчанию.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from sys import exit

root = tk.Tk()
tk.Tk.iconbitmap(root, default="icon.ico")
root.wm_title("Встраиваем Matplotlib в Tkinter")

large_font = ("FreeMono", 33, 'bold')
small_font = ("FreeMono", 16)
fin_font = ("Special Elite", 18, 'bold')

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
ax = fig.add_subplot()
line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
ax.set_xlabel("t -  время в сек")
ax.set_ylabel("f(t) - гармонические колебания")

canvas = FigureCanvasTkAgg(fig, master=root)  # Создаем объект для рисования
canvas.draw()

# не пакуем toolbar здесь!!!.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"Вы нажали {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tk.Button(master=root, text="Выход", command=exit, font=small_font)


def update_frequency(new_val):
    # запрашиваем частоту
    f = float(new_val)

    # обновляем данные
    y = 2 * np.sin(2 * np.pi * f * t)
    line.set_data(t, y)

    # требуется для обновления canvas и присоединения toolbar!
    canvas.draw()


slider_update = tk.Scale(root, from_=1, to=6, orient=tk.HORIZONTAL, resolution=0.01,
                         command=update_frequency, label="Частота (Гц)", font=small_font)

# Порядок упаковки - важен!.

button_quit.pack(side=tk.BOTTOM)
slider_update.pack(side=tk.BOTTOM, fill='x')
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.mainloop()
