from tkinter import END, Tk, Entry, X, Label


def exit_win(event):
    if event:
        print('*')
    root.destroy()


def in_label(event):
    if event:
        print('*')
    t = ent.get()
    label.configure(text=t)


def select_all_(event):
    root.after(10, select_all, event.widget)


def select_all(widget):
    widget.selection_range(0, END)
    widget.icursor(END)  # курсор в конец


root = Tk()
root.geometry()
root.title('Вводи-ка что-нибудь и нажми Enter!!!')
ent = Entry(width=60, font='FreeMono 16')
ent.focus_set()
ent.pack(fill=X)
label = Label(height=3, fg='orange', bg='darkgreen', font='Neucha 48 bold')
label.pack(fill=X)

ent.bind('<Return>', in_label)
ent.bind('<Control-a>', select_all_)
root.bind('<Control-q>', exit_win)

root.mainloop()
