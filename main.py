# start

import tkinter as tk

import controller

def psth(text):
    print(text)

app = tk.Tk()
test = tk.Button(text="Test", command="aa")
button = tk.Button(text='Ping!', command= lambda :controller.ping())
button2 = tk.Button(text='Show IP Interface!', command= lambda :controller.show_ip_interface())
button3 = tk.Button(text='Add Route!', command= lambda :controller.addRoute())
button4 = tk.Button(text='Show run!', command= lambda :controller.showRunningConfig())
button5 = tk.Button(text='write!', command= lambda :controller.writeToStartupConfig())
button6 = tk.Button(text='config()!', command= lambda :controller.configTerminal())
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
test.pack()
app.mainloop()
