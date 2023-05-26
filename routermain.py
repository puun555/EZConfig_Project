'''Puun Gui Ezconfig'''

import tkinter as tk
import netmiko as netmiko

def shw_run():
    running = "Puun Is OK"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, running)
    
def shw_ip_int():
    intbr = "Ip interface Brief"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, intbr)

def shw_ip_route():
    routee = "Route is yours"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, routee)
    
def shw_ip_ospf():
    ospf_text = "yoyoyoyoyoyyo"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, ospf_text)
    
def shw_ip_eigrp():
    eigrp_text = "sdsdsdsdsdsdsdsdsdsdsd"
    runningConf.delete("1.0", "end")
    runningConf.insert(tk.END, eigrp_text)



app = tk.Tk()
app.title('Ezconfig')
app.geometry("800x1000")

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
          command=lambda:shw_ip_ospf()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

tk.Button(shw_eigrp,text='Show eigrp neighbor!', bg = "yellow",
          command=lambda:shw_ip_eigrp()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

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
dynamic_route_frame.columnconfigure(0,weight=1)

'''Protocol Select'''
tk.Label(dynamic_route_frame, text="Dynamic Route Protocol Select").pack(side=tk.TOP)

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
   if var.get() == 1 :
       route_app = tk.Tk()
       route_app.title("OSPF")
       
       network_area_frame = tk.Frame(route_app)
       network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
       
       tk.Label(network_area_frame, text="OSPF Nextwork Area").grid(row=0, column=0, columnspan=3)
       
       tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
       tk.Label(network_area_frame, text="Wild Card").grid(row=1, column=2)
       
       tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=2, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=2, column=2)
       
       tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=3, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=3, column=2)
       
       tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=4, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=4, column=2)
       
       tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=5, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=5, column=2)
       
       tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=6, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=6, column=2)
       
       tk.Label(network_area_frame, text="Router Piority : ").grid(row=7, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=7, column=1)
       
       tk.Button(network_area_frame, text="Set").grid(row=8, column=0, columnspan=3)
   elif var.get() == 2 :
       route_app = tk.Tk()
       route_app.title("EIGRP")
       
       network_area_frame = tk.Frame(route_app)
       network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
       
       tk.Label(network_area_frame, text="EIGRP Nextwork Area").grid(row=0, column=0, columnspan=3)
       
       tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
       tk.Label(network_area_frame, text="Wild Card").grid(row=1, column=2)
       
       tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=2, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=2, column=2)
       
       tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=3, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=3, column=2)
       
       tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=4, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=4, column=2)
       
       tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=5, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=5, column=2)
       
       tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=6, column=1)
       tk.Entry(network_area_frame, bd=2).grid(row=6, column=2)
       
       tk.Button(network_area_frame, text="Set").grid(row=7, column=0, columnspan=3)
       
   elif var.get() == 3 :
       route_app = tk.Tk()
       route_app.title("RIPv2")
       
       network_area_frame = tk.Frame(route_app)
       network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
       
       tk.Label(network_area_frame, text="RIPv2 Nextwork Area").grid(row=0, column=0, columnspan=2)
       
       tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
       
       tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=2, column=1)
       
       tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=3, column=1)
       
       tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=4, column=1)
       
       tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=5, column=1)
       
       tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
       tk.Entry(network_area_frame, bd=2).grid(row=6, column=1)
       
       tk.Button(network_area_frame, text="Set").grid(row=7, column=0, columnspan=2)
       

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

'''Service'''
service_frame = tk.Frame(config_frame)
service_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
service_frame.columnconfigure(0, weight=1)

tk.Label(service_frame, text="Set Your Services").grid(row=0, column=0, columnspan=3)

tk.Label(service_frame, text="NTP Server Address : ").grid(row=1, column=0)
tk.Entry(service_frame, bd=2).grid(row=1, column=1)
tk.Button(service_frame, text="Set").grid(row=1, column=2)

tk.Label(service_frame, text="Syslogs Server Address : ").grid(row=2, column=0)
tk.Entry(service_frame, bd=2).grid(row=2, column=1)
tk.Button(service_frame, text="Set").grid(row=2, column=2)

tk.Label(service_frame, text="TFTP Server Address : ").grid(row=3, column=0)
tk.Entry(service_frame, bd=2).grid(row=3, column=1)
tk.Button(service_frame, text="Set").grid(row=3, column=2)


'''DHCP'''
dhcp_frame = tk.Frame(config_frame)
dhcp_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
dhcp_frame.columnconfigure(0, weight=1)

tk.Label(dhcp_frame, text="Setup DHCP Server").grid(row=0, column=0, columnspan=3)

tk.Label(dhcp_frame, text="DHCP Pools Name : ").grid(row=1, column=0)
tk.Entry(dhcp_frame, bd=2).grid(row=1, column=1)

tk.Label(dhcp_frame, text="Network Area : ").grid(row=2, column=0)
tk.Entry(dhcp_frame, bd=2).grid(row=2, column=1)
tk.Label(dhcp_frame, text="Subnet Mask").grid(row=3, column=0)
tk.Entry(dhcp_frame, bd=2).grid(row=3, column=1)

tk.Label(dhcp_frame, text="(Optional)DNS Server : ").grid(row=4, column=0)
tk.Entry(dhcp_frame, bd=2).grid(row=4, column=1)

tk.Label(dhcp_frame, text="(Optional)Domain-name : ").grid(row=5, column=0)
tk.Entry(dhcp_frame, bd=2).grid(row=5, column=1)

tk.Button(dhcp_frame, text="Set").grid(row=6, column=0, columnspan=3)











app.mainloop()