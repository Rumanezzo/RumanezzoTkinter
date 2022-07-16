from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sys import exit

import tkinter as tk

large_font = ("FreeMono", 33, 'bold')
small_font = ("FreeMono", 18)
fin_font = ("Special Elite", 18, 'bold')


class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.iconbitmap(default="icon.ico")

        self.wm_title("Внедряем Matplotlib в Tkinter!")

        container = tk.LabelFrame(self, bg='yellow',
                                  text='Все происходит внутри этой рамки и, как видишь, она - желтая!')
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frm in (StartPage, PageOne, PageTwo, PageThree):
            frame = frm(container, self)
            self.frames[frm] = frame
            frame.grid(row=0, column=0, sticky='NEWS')

        self.show_frame(StartPage)
        self.wm_geometry("+0+0")  # Не меняя размера окна, размещаем его в т. (0, 0)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Начальная страница", font=large_font)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Не нажимайте на эту кнопку!", font=small_font,
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="И на эту тоже не нажимайте!", font=small_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=5)

        button4 = tk.Button(self, text='Выходим, не задерживаемся!', font=fin_font,
                            command=exit)
        button4.pack(pady=5, side='bottom')

        button3 = tk.Button(self, text="Обязательно посмотрите график!", font=fin_font,
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(pady=5, side='bottom')


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Какое Разочарование...", font=large_font)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Возвращаемся на Начальную!", font=fin_font,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="На Вторую Страницу?! Серьёзно?", font=small_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="И снова разочарование...", font=large_font)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Возвращаемся на Начальную!",
                            command=lambda: controller.show_frame(StartPage), font=fin_font, )
        button1.pack()

        button2 = tk.Button(self, text="На Первую!",
                            command=lambda: controller.show_frame(PageOne), font=small_font, )
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Страница с Графиком!", font=large_font)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Возвращаемся на Начальную!", font=fin_font,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)


app = MainFrame()
app.mainloop()
