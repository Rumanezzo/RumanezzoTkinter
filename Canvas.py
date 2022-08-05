from tkinter import Tk, StringVar, Entry, Canvas


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Текстовые элементы Canvas")
        self.geometry("1280x100")

        self.var = StringVar()
        self.entry = Entry(self, textvariable=self.var, width=100, font='FreeMono 15')
        self.canvas = Canvas(self, bg="gold", width=1200, height=100)

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


if __name__ == "__main__":
    app = App()
    app.mainloop()
