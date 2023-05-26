import tkinter as tk
import tkinter.font as tkFont
from netmiko import *
from tkinter import messagebox

class App:
    
    def __init__(self, root):
        #setting title
        root.title("Cisco IOS Telnet")
        #setting window size
        root["bg"] = "#fff"
        width=400
        height=300 
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)



        lb_ip=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_ip["font"] = ft
        lb_ip["fg"] = "#000"
        lb_ip["bg"] = "#fff"
        lb_ip["justify"] = "center"
        lb_ip["text"] = "IP"
        lb_ip.place(x=100,y=30,width=70,height=25)

        global txt_ip
        txt_ip=tk.Entry(root)
        txt_ip["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=11)
        txt_ip["font"] = tkFont.Font(family='Times',size=11)
        txt_ip["fg"] = "#000"
        txt_ip["bg"] = "#fff"
        txt_ip["justify"] = "left"
        # txt_ip["text"] = "zxczxc"
        txt_ip.place(x=200,y=30,width=90,height=25)

        lb_port=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_port["font"] = ft
        lb_port["fg"] = "#000"
        lb_port["bg"] = "#fff"
        lb_port["justify"] = "left"
        lb_port["text"] = "Port"
        lb_port.place(x=100,y=80,width=70,height=25)

        lb_username=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_username["font"] = ft
        lb_username["fg"] = "#000"
        lb_username["bg"] = "#fff"
        lb_username["justify"] = "right"
        lb_username["text"] = "Username"
        lb_username.place(x=100,y=130,width=70,height=25)

        btn_cancel=tk.Button(root)
        btn_cancel["bg"] = "#fff"
        ft = tkFont.Font(family='Times',size=11)
        btn_cancel["font"] = ft
        btn_cancel["fg"] = "#000"
        btn_cancel["justify"] = "center"
        btn_cancel["text"] = "Cancel"
        btn_cancel.place(x=200,y=230,width=70,height=25)
        btn_cancel["command"] = self.cancelCommand

        lb_password=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_password["font"] = ft
        lb_password["fg"] = "#000"
        lb_password["bg"] = "#fff"
        lb_password["justify"] = "right"
        lb_password["text"] = "Password"
        lb_password.place(x=100,y=180,width=70,height=25)

        global txt_port
        txt_port=tk.Entry(root)
        txt_port["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        txt_port["font"] = ft
        txt_port["fg"] = "#000"
        txt_port["bg"] = "#fff"
        txt_port["justify"] = "left"
        txt_port["text"] = ""
        txt_port.place(x=200,y=80,width=90,height=25)

        global txt_username
        txt_username=tk.Entry(root)
        txt_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        txt_username["font"] = ft
        txt_username["fg"] = "#000"
        txt_username["bg"] = "#fff"
        txt_username["justify"] = "left"
        txt_username["text"] = ""
        txt_username.place(x=200,y=130,width=90,height=25)

        global txt_password
        txt_password=tk.Entry(root)
        txt_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        txt_password["font"] = ft
        txt_password["fg"] = "#000"
        txt_password["bg"] = "#fff"
        txt_password["justify"] = "left"
        txt_password["text"] = ""
        txt_password.place(x=200,y=180,width=90,height=25)

        btn_connect=tk.Button(root)
        btn_connect["bg"] = "#fff"
        ft = tkFont.Font(family='Times',size=11)
        btn_connect["font"] = ft
        btn_connect["fg"] = "#000"
        btn_connect["justify"] = "center"
        btn_connect["text"] = "Connect"
        btn_connect.place(x=100,y=230,width=70,height=25)
        btn_connect["command"] = self.connectCommand

    
    def connectCommand(self):
        global cisco_ios 
        cisco_ios = {
        "device_type": "cisco_ios_telnet",
        "host": "",
        "port" : "",
        "username" : "",
        "password" : ""
        }
        cisco_ios["host"] = txt_ip.get()
        cisco_ios["port"] = txt_port.get()
        cisco_ios["username"] = txt_username.get()
        cisco_ios["password"] = txt_password.get()
        app.login()

    def cancelCommand(self):
        root.destroy()

    def login(self):
        global cmd
        cmd = ConnectHandler(**cisco_ios)
        try:
            with ConnectHandler(**cisco_ios) as cmd:
                messagebox.showinfo(title="Cisco IOS Telnet", message="Connected Success!")
                self.openMainWindow()
                self.cancelCommand()
        except:
            messagebox.showerror(titile="Cisco IOS Telnet", message="Connected Failed!")

    def openMainWindow(self):
        app = tk.Tk()
        mf = MainFrame(app)
        mf.mainloop()

class MainFrame:
    def __init__(self,app):

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
                command=lambda:shw_ip_ospf()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

        tk.Button(shw_eigrp,text='Show eigrp neighbor', bg = "yellow",
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

        tk.Button(add_ip_button, text="Add", command=lambda:add_ip_to_interface()
                ).pack(side=tk.LEFT)
        tk.Button(add_ip_button, text="Shutdown", command=lambda:int_shutdown()
                ).pack(side=tk.LEFT)
        tk.Button(add_ip_button, text="No Shut",command=lambda:int_no_shutdown()
                ).pack(side=tk.LEFT)


        '''Routing Protocol'''
        dynamic_route_frame = tk.Frame(config_frame)
        dynamic_route_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)

        '''Protocol Select'''
        tk.Label(dynamic_route_frame, text="Dynamic Route Protocol Select").pack(side=tk.TOP)

        var = tk.IntVar()

        tk.Radiobutton(dynamic_route_frame, text="OSPF", variable=var, value=1,
                          command=lambda:sel()).pack()
        
        tk.Radiobutton(dynamic_route_frame, text="EIGRP", variable=var, value=2,
                          command=lambda:sel()).pack()
        
        tk.Radiobutton(dynamic_route_frame, text="RIPv2", variable=var, value=3,
                          command=lambda:sel()).pack()
        
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
        tk.Label(dhcp_frame, text="Subnet Mask").grid(row=1, column=2)
        
        tk.Label(dhcp_frame, text="Network Area : ").grid(row=2, column=0)
        tk.Entry(dhcp_frame, bd=2).grid(row=2, column=1)
        tk.Entry(dhcp_frame, bd=2).grid(row=2, column=2)
        
        tk.Label(dhcp_frame, text="(Optional) DNS Server Address : ").grid(row=3, column=0)
        tk.Entry(dhcp_frame, bd=2).grid(row=3, column=1)
        
        tk.Label(dhcp_frame, text="(Optional) Domain-name : ").grid(row=4, column=0)
        tk.Entry(dhcp_frame, bd=2).grid(row=4, column=1)
        
        tk.Button(dhcp_frame, text="Set").grid(row=5, column=2)
        
        def sel():
            selection = "You selected the option " + str(var.get())
            label.config(text = selection)

        def shw_run():
            running = cmd.send_command("show run")
            runningConf.delete("1.0", "end")
            runningConf.insert(tk.END, running)
            
        def shw_ip_route():
            routee = cmd.send_command("show ip route")
            runningConf.delete("1.0", "end")
            runningConf.insert(tk.END, routee)
            
        def shw_ip_int():
            intbr = cmd.send_command("show ip int br")
            runningConf.delete("1.0", "end")
            runningConf.insert(tk.END, intbr)
            
        def shw_ip_ospf():
            ospf_nei = cmd.send_command("show ip ospf neighbor")
            runningConf.delete("1.0", "end")
            runningConf.insert(tk.END, ospf_nei)
            
        def shw_ip_eigrp():
            eigrp_nei = cmd.send_command("show ip eigrp neighbor")
            runningConf.delete("1.0", "end")
            runningConf.insert(tk.END, eigrp_nei)

        def add_ip_to_interface():
            int = interface_form.get()
            ip = ip_form.get()
            subnet = subnetmask.get()
            result = cmd.send_config_set(["int {0}".format(int), "ip address {0} {1}".format(ip,subnet)])
            runningConf.delete("1.0","end")
            runningConf.insert(tk.END, result)
        
        def int_shutdown():
            int = interface_form.get()
            result = cmd.send_config_set(["int {0}".format(int),"shutdown"])
            runningConf.delete("1.0","end")
            runningConf.insert(tk.END, result)

        def int_no_shutdown():
            int = interface_form.get()
            result = cmd.send_config_set(["int {0}".format(int),"no shutdown"])
            runningConf.delete("1.0","end")
            runningConf.insert(tk.END, result)
        
        
        
        
        
        
        
    







#-----------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    


