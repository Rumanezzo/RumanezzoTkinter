from tkinter import Tk, StringVar, Entry, Canvas, SUNKEN


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Текстовые элементы Canvas")
        self.iconbitmap('icon.ico')

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.w, self.h = 1280, 100
        x, y = (sw - self.w) // 2, (sh - self.h) // 3

        self.geometry(f'{self.w}x{self.h}+{x}+{y}')
        self.resizable(False, False)

        self.var = StringVar()
        self.entry = Entry(self, textvariable=self.var, width=106, font='FreeMono 15', relief=SUNKEN, bg="LightGrey")
        self.canvas = Canvas(self, bg="DarkGrey", width=1280, height=100)

        self.entry.pack(pady=3)
        self.canvas.pack()
        self.update()

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        options = {"font": "Neucha 26", "fill": "blue",
                   "activefill": "red"}
        self.text_id = self.canvas.create_text((w / 2, h / 2), **options)
        self.var.trace("w", self.write_text)

    def write_text(self, *args):
        self.canvas.itemconfig(self.text_id, text=self.var.get())
        return len(args)


if __name__ == "__main__":
    app = App()
    app.mainloop()
