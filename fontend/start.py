# start

import tkinter as tk

import sys
sys.path.append("backend")
import controller

def print_something(text):
    print(text)

app = tk.Tk()
button = tk.Button(text='Ping!', command= lambda :controller.ping())
button2 = tk.Button(text='Show IP Interface!', command= lambda :controller.show_ip_interface())
button.pack()
button2.pack()
app.mainloop()
