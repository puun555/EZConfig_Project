'''Puun Gui Ezconfig'''

import tkinter as tk
import netmiko as netmiko

def shw_run():
    running = "Puun Is OK"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, running)
    
def shw_ip_route():
    routee = "Route is yours"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, routee)
    
def shw_ip_int():
    intbr = "Ip interface Brief"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, intbr)
    
def shw_ip_ospf():
    ospf_nei = "Ospf neighbor"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, ospf_nei)
    
def shw_ip_eigrp():
    eigrp_nei = "Eigrp neighbor"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, eigrp_nei)

app = tk.Tk()
app.title('Ezconfig')
app.geometry("800x600")

'''Left Frame'''
left_frame = tk.Frame(app)
left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

'''Top Frame'''
top_frame = tk.Frame(app)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


'''Text Box To Display Config'''
text_frame = tk.Frame(top_frame)
text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
text_frame.config(background="White")

runningConf = tk.Text(text_frame)
runningConf.pack( expand=True, fill=tk.BOTH, padx=10, pady=5)


'''Show Frame to contain Show Config'''
show_frame = tk.Frame(left_frame)
show_frame.pack(side=tk.TOP, fill=tk.BOTH)
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

tk.Button(runconf_frame,text='Show Running Config!', bg = "yellow", 
          command=lambda:shw_run()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

tk.Button(intbr_frame,text='Show ip interface brief!', bg = "yellow", 
          command=lambda:shw_ip_int()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

tk.Button(shw_route,text='Show ip route!', bg = "yellow",
          command=lambda:shw_ip_route()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

tk.Button(shw_ospf,text='Show ospf neighbor!', bg = "yellow",
          command=shw_ip_ospf()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

tk.Button(shw_eigrp,text='Show eigrp neighbor', bg = "yellow",
          command=shw_ip_eigrp()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

'''Config Frame'''

config_frame = tk.Frame(left_frame)
config_frame.pack()
config_frame.config(background="red")

'''assign ip address'''
# Frame setup
add_ip_frame = tk.Frame(config_frame)
add_ip_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
add_ip_frame.columnconfigure(0, weight=1)

# IP address Header
tk.Label(add_ip_frame, text='Assign IP address').grid(column=0, row=0, columnspan=2)

# Interface frame
tk.Label(add_ip_frame, text='Interface : ').grid(column=0, row=1)
interface_form = tk.Entry(add_ip_frame, bd=2)
interface_form.grid(column=1, row=1)

# IP frame
tk.Label(add_ip_frame, text='IP : ').grid(column=0, row=3)
ip_form = tk.Entry(add_ip_frame, bd=2)
ip_form.grid(column=1, row=3)

# netmask frame
tk.Label(add_ip_frame, text='Subnet Mask : ').grid(column=0, row=4)
subnetmask = tk.Entry(add_ip_frame, bd=2)
subnetmask.grid(column=1, row=4)

# IP adding Button Frame
add_ip_button = tk.Frame(add_ip_frame)
add_ip_button.grid(column=0, row=5, columnspan=2)

tk.Button(add_ip_button, text="Add",
          ).pack(side=tk.LEFT)
tk.Button(add_ip_button, text="Shutdown"
          ).pack(side=tk.LEFT)
tk.Button(add_ip_button, text="No Shut"
          ).pack(side=tk.LEFT)


'''Routing Protocol'''
dynamic_route_frame = tk.Frame(config_frame)
dynamic_route_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)

'''Protocol Select'''
tk.Label(dynamic_route_frame, text="Dynamic Route Protocol Select").pack(side=tk.TOP)

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

var = tk.IntVar()

tk.Radiobutton(dynamic_route_frame, text="OSPF", variable=var, value=1,
                  command=sel).pack()

tk.Radiobutton(dynamic_route_frame, text="EIGRP", variable=var, value=2,
                  command=sel).pack()

tk.Radiobutton(dynamic_route_frame, text="RIPv2", variable=var, value=3,
                  command=sel).pack()

label = tk.Label(dynamic_route_frame)
label.pack()

tk.Button(dynamic_route_frame, text="Set Routing Protocol").pack()

'''Default Route'''
default_route_frame = tk.Frame(config_frame)
default_route_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
default_route_frame.columnconfigure(0,weight=1)

tk.Label(default_route_frame, text="Set Default Route").grid(row=0, column=0, columnspan=3)
tk.Label(default_route_frame, text="Next-Hop Interace : ").grid(row=1, column=0)
tk.Entry(default_route_frame, bd=2).grid(row=1, column=1)
tk.Button(default_route_frame, text="Set").grid(row=1, column=2)

'''Secure'''
secure_frame = tk.Frame(config_frame)
secure_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
secure_frame.columnconfigure(0, weight=1)

tk.Label(secure_frame, text="Security Set-up").grid(row=0, column=0, columnspan=3)

tk.Label(secure_frame, text="Set Enable Password : ").grid(row=1, column=0)
tk.Entry(secure_frame, bd=2).grid(row=1, column=1)
tk.Button(secure_frame, text="Set").grid(row=1, column=2)











app.mainloop()