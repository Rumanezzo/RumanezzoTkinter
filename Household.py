import tkinter as tk
from tkinter import ttk
import sqlite3

btn = '<Button-1>'
srh = 'Поиск'


class Main(tk.Frame):
    def __init__(self, root_):
        super().__init__(root_)

        self.refresh_img = None
        self.delete_img = None
        self.search_img = None
        self.tree = None
        self.update_img = None
        self.add_img = None

        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text=srh, bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='№')
        self.tree.heading('description', text='Название Транзакции')
        self.tree.heading('costs', text='Доход или Расход?')
        self.tree.heading('total', text='Сколько?')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def update_record(self, description, costs, total):
        self.db.c.execute('''UPDATE finance SET description=?, costs=?, total=? WHERE ID=?''',
                          (description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM finance WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%',)
        self.db.c.execute('''SELECT * FROM finance WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    @staticmethod
    def open_dialog():
        Child()

    @staticmethod
    def open_update_dialog():
        Update()

    @staticmethod
    def open_search_dialog():
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)

        self.btn_ok = None
        self.combobox = None
        self.entry_money = None
        self.entry_description = None

        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить доходы или расходы')
        self.geometry('400x220+400+300')
        self.iconbitmap("config.ico")
        self.resizable(False, False)

        label_description = tk.Label(self, text='Транзакция:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Тип Транзакции:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=['Доход', 'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind(btn, lambda event: self.view.records(self.entry_description.get(),
                                                              self.combobox.get(),
                                                              self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать транзакцию')
        btn_edit = ttk.Button(self, text='Подтвердить')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM finance WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.entry_description.insert(0, row[1])
        if row[2] != 'Доход':
            self.combobox.current(1)
        self.entry_money.insert(0, row[3])


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.entry_search = None
        self.init_search()
        self.view = app

    def action_button(self, event):
        if event == 0:
            print('Кажется ничего не происходит...')
        self.view.search_records(self.entry_search.get())
        self.destroy()

    def init_search(self):
        self.title(srh)
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text=srh)
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text=srh)
        btn_search.place(x=105, y=50)
        btn_search.bind(btn, self.action_button)


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
        self.conn.commit()

    def insert_data(self, description, costs, total):
        self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
                       (description, costs, total))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DataBase()
    app = Main(root)
    app.pack()
    root.title("Учитываем приходы и расходы в семье")
    root.iconbitmap("config.ico")
    root.geometry("665x450+300+200")
    root.resizable(False, False)
    root.mainloop()
