import tkinter as tk

# create the main window
root = tk.Tk()

# disable the window bar
root.overrideredirect(True)

# set transparency and make the window stay on top
root.attributes('-transparentcolor', 'white', '-topmost', True)

# set the background image
psg = tk.PhotoImage(file='victory2.png')
tk.Label(root, bg='white', image=psg).pack()

# move the window to center
root.eval('tk::PlaceWindow . Center')

# schedule the window to close after 4 seconds
root.after(6000, root.destroy)

# run the main loop
root.mainloop()
