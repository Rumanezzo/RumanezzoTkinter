from tkinter import Tk, Label, Canvas, Frame, Scrollbar
from tkinter import font

root = Tk()
x_max = root.winfo_screenwidth()
y_max = root.winfo_screenheight()

w, h = x_max // 4, y_max - 60
x, y = (x_max - w) // 2, (y_max - h) // 2

root.geometry(f'{w}x{h}+-10+-25')

fonts = list(font.families())
fonts.sort()
sizeof_font = 18
exclude = (30, 56, 101, 102, 103, 104, 105, 106, 108, 109, 110, 114, 147, 150, 154, 155, 159,
           169, 173, 177, 178, 182, 223, 261, 262, 263, 267, 268, 269, 270, 284, 285, 286,
           307, 308, 309, 310)

def populate(frame):
    for item in enumerate(fonts):
        if item[0] in exclude:
            continue
        Label(frame, text=str(item[0]) + ' → ' + item[1], font=(item[1], sizeof_font)).pack(anchor='w')


def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


canvas0 = Canvas(root, borderwidth=0, background="#fdfddf", width=w, height=h,)
frame0 = Frame(canvas0, background="#ffffff")

vsb = Scrollbar(root, orient="vertical", command=canvas0.yview)
canvas0.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas0.pack(side="left", fill="both", expand=True)
canvas0.create_window((4, 4), window=frame0, anchor="nw")

frame0.bind("<Configure>", lambda event, canvas=canvas0: on_frame_configure(canvas))

populate(frame0)

root.mainloop()
