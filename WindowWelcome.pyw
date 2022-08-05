from tkinter import Label, Button, Tk, Entry


class MyWindow(Tk):
    def __init__(self):
        super().__init__()

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        self.w, self.h = sw // 2, sh // 6
        x, y = (sw - self.w) // 2, (sh - self.h) // 2

        self.geometry(f'{self.w}x{self.h}+{x}+{y}')

        self.config(bg='DarkGrey')
        self.iconbitmap('icon.ico')
        self.title('Диалог ввода имени и выход по нажатию кнопки!')

        self.text1 = Label(self, text='Вопрошаю об имени твоём!!!', fg='yellow', bg='DarkGray')
        self.text1.config(font=('FreeMono', 16, 'bold'))
        self.text1.pack()

        self.text2 = Label(self, text='Вводи свое имя в зеленое поле!', fg='DarkBlue', bg='DarkGray')
        self.text2.config(font=('FreeMono', 20, 'bold'))
        self.text2.pack()

        self.ed = Entry(self, width=40, bg='green', fg='gold', font=('FreeMono', 18))
        self.ed.focus_force()
        self.ed.pack()

        self.button1 = Button(self, text='Подтверждение ввода!', command=self.change, font=('FreeMono', 14, 'bold'))
        self.button1.config(width=25, height=1, bg='olive', fg='white')
        self.button1.pack()

    def change(self):
        txt = 'Привет - ' + self.ed.get() + '!'
        self.text1.config(text='Ты внял(а) моим мольбам!')
        self.text2.config(text=txt, font=('FreeMono', 20, 'bold'))
        self.button1.destroy()
        self.ed.destroy()
        button2 = Button(self, text='Теперь можешь уходить!', command=self.destroy, font=('FreeMono', 16, 'bold'))
        button2.config(width=25, height=1, bg='olive', fg='white')
        button2.pack()


def main():
    root = MyWindow()
    root.mainloop()


if __name__ == '__main__':
    main()
