import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, messagebox as msg, Spinbox

win = tk.Tk()
win.title('Графический Интерфейс на Python')
tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='1')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='2')

tab_control.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text='Всесильный Python!')
mighty.grid(column=0, row=0, padx=8, pady=4)

mighty2 = ttk.LabelFrame(tab2, text='Хитрый Змей!!')
mighty2.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text='Введите своё имя')
a_label.grid(column=0, row=0, sticky='W')


def click_me():
    action.configure(text=f'Привет {name.get()}, №{number_chosen.get()}')


name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=80, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

action = ttk.Button(mighty, text='Нажмите Меня!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(mighty, text='Выберите номер:').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=6, textvariable=number, state='readonly')
number_chosen['values'] = tuple([2 ** x for x in range(7)])
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text='Недоступно', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text='Не выбрано', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text='Выбрано', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

colors = ('Blue', 'Gold', 'Red', 'Green')


def rad_call():
    rad_sel = radVar.get()
    mighty2.configure(text=colors[rad_sel - 1])


radVar = tk.IntVar()
radVar.set(99)

for _ in enumerate(colors):
    rad = tk.Radiobutton(mighty2, text=_[1], variable=radVar, value=_[0] + 1, command=rad_call)
    rad.grid(column=_[0], row=6, sticky=tk.W, columnspan=3)


def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '→')


spin = Spinbox(mighty, from_=0, to=10, width=5, bd=9, command=_spin)
spin.grid(column=0, row=2, sticky=tk.W)

scroll_w = 30
scroll_h = 3

scr = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)

buttons_frame = ttk.LabelFrame(mighty, text='Терпим и справляемся')
buttons_frame.grid(column=0, row=7, pady=10)

lbl_txt = ('Боль', 'Презрение', 'Ревность', 'Ярость', 'Гнев', 'Страсть', 'Ненасытность', 'Алчность')
for _ in enumerate(lbl_txt):
    ttk.Label(buttons_frame, text=_[1]).grid(column=_[0], row=0, sticky=tk.W + tk.E)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)


def _quit():
    win.quit()
    win.destroy()
    exit()


def _msg_box():
    msg.showinfo('О программе', 'Графический интерфейс на Tkinter\n Программа создана в 2022 году')


# Создание каскадного меню
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Новый')
file_menu.add_separator()
file_menu.add_command(label='Выход', command=_quit)
menu_bar.add_cascade(label='Файл', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)

help_menu.add_command(label='О программе', command=_msg_box)
menu_bar.add_cascade(label='Помощь', menu=help_menu)

win.iconbitmap('Python.ico')

name_entered.focus()
win.resizable(False, False)

win.mainloop()
