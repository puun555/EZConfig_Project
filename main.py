# start

import tkinter as tk

# import sys
# sys.path.append("backend")
import controller

def print_something(text):
    print(text)

app = tk.Tk()
app.title("Cisco IOS Telnet")
w = 400
h = 300 
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

lb1 = tk.Label(text="ip", fg="black",)
txt1 = tk.Entry()
lb2 = tk.Label(text="port", fg="black")
txt2 = tk.Entry()
lb3 = tk.Label(text="usernane", fg="black")
txt3 = tk.Entry()
lb4 = tk.Label(text="password", fg="black")
txt4 = tk.Entry()
# textbox = tk.Text(app)
btn = tk.Button(text="Click Me", command=lambda: controller.connect())
# textbox.pack()
lb1.grid(row=0, column=0)
txt1.pack()
lb2.pack()
txt2.pack()
lb3.pack()
txt3.pack()
lb4.pack()
txt4.pack()
btn.pack()

app.mainloop()
