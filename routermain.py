'''Puun Gui Ezconfig'''

import tkinter as tk
import netmiko as netmiko

def shw_run():
    running = "Puun Is OK"

app = tk.Tk()
app.title('Ezconfig')
app.geometry("800x600")

'''Show Frame to contain Show Config'''
show_frame = tk.Frame(app)
show_frame.grid(row=0, column=0, rowspan=2, sticky='NSEW')
show_frame.config(background='Light Blue' )

runconf_frame = tk.Frame(show_frame)
runconf_frame.pack(side=tk.TOP,  expand=True, fill=tk.X, padx=10, pady=5)

intbr_frame = tk.Frame(show_frame)
intbr_frame.pack(side=tk.TOP,  expand=True, fill=tk.X, padx=10, pady=5)

shw_route = tk.Frame(show_frame)
shw_route.pack(side=tk.TOP,  expand=True, fill=tk.X, padx=10, pady=5)

shw_ospf = tk.Frame(show_frame)
shw_ospf.pack(side=tk.TOP,  expand=True, fill=tk.X, padx=10, pady=5)

shw_eigrp = tk.Frame(show_frame)
shw_eigrp.pack(side=tk.TOP,  expand=True, fill=tk.X, padx=10, pady=5)

tk.Label(runconf_frame, text='Show Running Config!', bg = "blue").pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
tk.Button(runconf_frame,text='A', bg = "yellow", 
          command=shw_run()).pack(side=tk.TOP, expand = True, fill=tk.BOTH)
tk.Label(intbr_frame, text='Show ip interface brief!',  bg = "blue" ).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
tk.Button(intbr_frame,text='B', bg = "yellow").pack(side=tk.TOP, expand = True, fill=tk.BOTH)
tk.Label(shw_route, text='Show ip route!',  bg = "blue").pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
tk.Button(shw_route,text='C', bg = "yellow").pack(side=tk.TOP, expand = True, fill=tk.BOTH)
tk.Label(shw_ospf, text='Show ospf neighbor!',  bg = "blue").pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
tk.Button(shw_ospf,text='D', bg = "yellow").pack(side=tk.TOP, expand = True, fill=tk.BOTH)
tk.Label(shw_eigrp, text='Show eigrp neighbor!',  bg = "blue").pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
tk.Button(shw_eigrp,text='D', bg = "yellow").pack(side=tk.TOP, expand = True, fill=tk.BOTH)


'''Text Box To Display Config'''
text_frame = tk.Frame(app)
text_frame.grid(row=0, column=1, rowspan=3, sticky='NSEW')
text_frame.config(background="White")

runningConf = tk.Text(text_frame).pack( expand=True, fill=tk.BOTH, padx=10, pady=5)



def shw_run():
    running = "Puun Is OK"
    
app.mainloop()