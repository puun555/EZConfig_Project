# start

import tkinter as tk

def print_something(text):
    print(text)

app = tk.Tk()
button = tk.Button(text='click me!', command= lambda :print_something('print this'))
button.pack()
app.mainloop()