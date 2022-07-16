from tkinter import *


def change():
    txt = 'Привет - ' + ed.get() + '!'
    t1.config(text='Ты внял(а) моим мольбам!')
    t2.config(text=txt, font=('FreeMono', 20, 'bold'))
    b1.destroy()
    ed.destroy()
    b2 = Button(w1, text='Теперь можешь уходить!', command=bye, font=('FreeMono', 16, 'bold'))
    b2.config(width=25, height=1, bg='olive', fg='white')
    b2.pack()


def bye():
    w1.destroy()


w1 = Tk()
x_max = w1.winfo_screenwidth()
y_max = w1.winfo_screenheight()
w, h = x_max // 2, y_max // 6
x, y = (x_max - w) // 2, (y_max - h) // 2

w1.geometry(f'{w}x{h}+{x}+{y}')
w1.iconbitmap('bomb.ico')

w1.config(bg='DarkGrey')
w1.title('Диалог ввода имени и выход по нажатию кнопки!')

t1 = Label(w1, text='Вопрошаю об имени твоём!!!', fg='yellow', bg='DarkGray')
t1.config(font=('FreeMono', 16, 'bold'))
t1.pack()

t2 = Label(w1, text='Вводи свое имя в зеленое поле!', fg='DarkBlue', bg='DarkGray')
t2.config(font=('FreeMono', 20, 'bold'))
t2.pack()

ed = Entry(w1, width=40, bg='green', fg='gold', font=('FreeMono', 16))
ed.focus_force()
ed.pack()

b1 = Button(w1, text='Подтверждение ввода!', command=change, font=('FreeMono', 14, 'bold'))
b1.config(width=25, height=1, bg='olive', fg='white')
b1.pack()


w1.mainloop()
