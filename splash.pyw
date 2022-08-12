import tkinter as tk

root = tk.Tk()

# убираем меню окна
root.overrideredirect(True)

# устанавливаем прозрачность окна и его расположение поверх других окон
root.attributes('-transparentcolor', 'white', '-topmost', True)

# Устанавливаем заставку (background)
psg = tk.PhotoImage(file='splash.png')
tk.Label(root, bg='white', image=psg).pack()

# Перемещаем окно в центр экрана
root.eval('tk::PlaceWindow . Center')

# Задаем уничтожение окна через 6 сек
root.after(6000, root.destroy)

root.mainloop()
