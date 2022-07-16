# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, BOTH


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="grey")
        self.parent = parent
        
        self.pack(fill=BOTH, expand=1)
        self.center_window()

    def center_window(self):

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        w, h = 2 * sw // 3, 2 * sh // 3
        x, y = (sw - w) // 2, (sh - h) // 2

        self.parent.geometry(f'{w}x{h}+{x}+{y}')
        self.parent.title(f'Окно размером: {w}x{h} по координатам: x={x}, y={y} выведено в центре экрана при '
                          f'разрешении: {sw}x{sh}')


def main():
    root = Tk()
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
