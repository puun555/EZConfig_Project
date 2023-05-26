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
        if txt_ip.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out IP Address correctly!")
        if txt_port.get() == "":
            cisco_ios["port"] = "23"
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
            messagebox.showerror(title="Cisco IOS Telnet", message="Connected Failed!")

    def openMainWindow(self):
        app = tk.Tk()
        mf = MainFrame(app,cmd)
        app.mainloop()

class MainFrame:
    def __init__(self,app,cmd):
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

        global runningConf
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
                command=lambda:self.shw_run()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

        tk.Button(intbr_frame,text='Show ip interface brief!', bg = "yellow", 
                command=lambda:self.shw_ip_int()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

        tk.Button(shw_route,text='Show ip route!', bg = "yellow",
                command=lambda:self.shw_ip_route()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

        tk.Button(shw_ospf,text='Show ospf neighbor!', bg = "yellow",
                command=lambda:self.shw_ip_ospf()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)
        tk.Button(shw_eigrp,text='Show eigrp neighbor', bg = "yellow",
                command=lambda:self.shw_ip_eigrp()).pack(side=tk.LEFT, expand = True, fill=tk.BOTH)

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
        global interface_form
        interface_form = tk.Entry(add_ip_frame, bd=2)
        interface_form.grid(column=1, row=1)

        # IP frame
        tk.Label(add_ip_frame, text='IP : ').grid(column=0, row=3)
        global ip_form
        ip_form = tk.Entry(add_ip_frame, bd=2)
        ip_form.grid(column=1, row=3)

        # netmask frame
        tk.Label(add_ip_frame, text='Subnet Mask : ').grid(column=0, row=4)
        global subnetmask
        subnetmask = tk.Entry(add_ip_frame, bd=2)
        subnetmask.grid(column=1, row=4)

        # IP adding Button Frame
        add_ip_button = tk.Frame(add_ip_frame)
        add_ip_button.grid(column=0, row=5, columnspan=2)

        tk.Button(add_ip_button, text="Add", command=lambda:self.add_ip_to_interface()
                ).pack(side=tk.LEFT)
        tk.Button(add_ip_button, text="Shutdown", command=lambda:self.int_shutdown()
                ).pack(side=tk.LEFT)
        tk.Button(add_ip_button, text="No Shut",command=lambda:self.int_no_shutdown()
                ).pack(side=tk.LEFT)


        '''Routing Protocol'''
        dynamic_route_frame = tk.Frame(config_frame)
        dynamic_route_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
        dynamic_route_frame.columnconfigure(0,weight=1)

        '''Protocol Select'''
        tk.Label(dynamic_route_frame, text="Dynamic Route Protocol Select").pack(side=tk.TOP)

        global var
        var = tk.IntVar()

        tk.Radiobutton(dynamic_route_frame, text="OSPF", variable=var, value=1,
                        command=lambda:self.sel1()).pack()

        tk.Radiobutton(dynamic_route_frame, text="EIGRP", variable=var, value=2,
                        command=lambda:self.sel2()).pack()

        tk.Radiobutton(dynamic_route_frame, text="RIPv2", variable=var, value=3,
                        command=lambda:self.sel3()).pack()
        global label
        label = tk.Label(dynamic_route_frame)
        label.pack()

        '''Static Route'''
        static_route_frame = tk.Frame(config_frame)
        static_route_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
        static_route_frame.columnconfigure(0,weight=1)


        tk.Label(static_route_frame, text="Set Static Route").grid(row=0, column=0, columnspan=2)
        tk.Label(static_route_frame, text="Destination Network : ").grid(row=1, column=0)
        global destination
        destination = tk.Entry(static_route_frame, bd=2)
        destination.grid(row=1, column=1)
        tk.Label(static_route_frame, text="Destination Netmask : ").grid(row=2, column=0)
        global subnetmask_static
        subnetmask_static = tk.Entry(static_route_frame, bd=2)
        subnetmask_static.grid(row=2, column=1)
        tk.Label(static_route_frame, text="Next-Hop Interface : ").grid(row=3, column=0)
        global nexthop
        nexthop = tk.Entry(static_route_frame, bd=2)
        nexthop.grid(row=3, column=1)
        tk.Button(static_route_frame, text="Set", command=lambda:self.static_route()).grid(row=4, column=0, columnspan=2)
        
        
        '''Service'''
        service_frame = tk.Frame(config_frame)
        service_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
        service_frame.columnconfigure(0, weight=1)
        
        tk.Label(service_frame, text="Set Your Services").grid(row=0, column=0, columnspan=3)
        
        tk.Label(service_frame, text="NTP Server Address : ").grid(row=1, column=0)
        global ntps
        ntps = tk.Entry(service_frame, bd=2)
        ntps.grid(row=1, column=1)
        tk.Button(service_frame, text="Set",command=lambda:self.set_ntp()).grid(row=1, column=2)
        
        tk.Label(service_frame, text="Syslogs Server Address : ").grid(row=2, column=0)
        global syslogs
        syslogs = tk.Entry(service_frame, bd=2)
        syslogs.grid(row=2, column=1)
        tk.Button(service_frame, text="Set",command=lambda:self.set_syslog()).grid(row=2, column=2)
        
        # tk.Label(service_frame, text="TFTP Server Address : ").grid(row=3, column=0)
        # global tftps
        # tftps = tk.Entry(service_frame, bd=2)
        # tftps.grid(row=3, column=1)
        # tk.Button(service_frame, text="Send",command=lambda:self.set_tftp()).grid(row=3, column=2)
        
        
        '''DHCP'''
        dhcp_frame = tk.Frame(config_frame)
        dhcp_frame.pack(side=tk.TOP, expand=True, fill=tk.X, padx=10, pady=5)
        dhcp_frame.columnconfigure(0, weight=1)

        tk.Label(dhcp_frame, text="Setup DHCP Server").grid(row=0, column=0, columnspan=3)

        tk.Label(dhcp_frame, text="DHCP Pools Name : ").grid(row=1, column=0)
        global pool_name
        pool_name = tk.Entry(dhcp_frame, bd=2)
        pool_name.grid(row=1, column=1)

        tk.Label(dhcp_frame, text="Network Area : ").grid(row=2, column=0)
        global net_area 
        net_area = tk.Entry(dhcp_frame, bd=2)
        net_area.grid(row=2, column=1)
        tk.Label(dhcp_frame, text="Subnet Mask").grid(row=3, column=0)
        global snm
        snm = tk.Entry(dhcp_frame, bd=2)
        snm.grid(row=3, column=1)

        tk.Label(dhcp_frame, text="Default Router : ").grid(row=4, column=0)
        global default
        default = tk.Entry(dhcp_frame, bd=2)
        default.grid(row=4, column=1)

        tk.Label(dhcp_frame, text="(Optional)DNS Server : ").grid(row=5, column=0)
        global dns
        dns = tk.Entry(dhcp_frame, bd=2)
        dns.grid(row=5, column=1)

        tk.Label(dhcp_frame, text="(Optional)Domain-name : ").grid(row=6, column=0)
        global dm_name
        dm_name = tk.Entry(dhcp_frame, bd=2)
        dm_name.grid(row=6, column=1)

        tk.Button(dhcp_frame, text="Set",command=lambda:self.set_dhcp()).grid(row=7, column=0, columnspan=3)
        
    def sel1(self):
        selection = "You have selected OSPF"
        label.config(text = selection)
        route_app = tk.Tk()
        route_app.title("OSPF")
            
        network_area_frame = tk.Frame(route_app)
        network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
            
        tk.Label(network_area_frame, text="OSPF Nextwork Area").grid(row=0, column=0, columnspan=3)
            
        tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
        tk.Label(network_area_frame, text="Wild Card").grid(row=1, column=2)
            
        tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
        global onw1,osn1
        onw1 = tk.Entry(network_area_frame, bd=2)
        onw1.grid(row=2, column=1)
        osn1 = tk.Entry(network_area_frame, bd=2)
        osn1.grid(row=2, column=2)
            
        tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
        global onw2,osn2
        onw2 = tk.Entry(network_area_frame, bd=2)
        onw2.grid(row=3, column=1)
        osn2 = tk.Entry(network_area_frame, bd=2)
        osn2.grid(row=3, column=2)
        
        tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
        global onw3,osn3
        onw3 = tk.Entry(network_area_frame, bd=2)
        onw3.grid(row=4, column=1)
        osn3 = tk.Entry(network_area_frame, bd=2)
        osn3.grid(row=4, column=2)
            
        tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
        global onw4,osn4
        onw4 = tk.Entry(network_area_frame, bd=2)
        onw4.grid(row=5, column=1)
        osn4 = tk.Entry(network_area_frame, bd=2)
        osn4.grid(row=5, column=2)
        
        tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
        global onw5,osn5
        onw5 = tk.Entry(network_area_frame, bd=2)
        onw5.grid(row=6, column=1)
        osn5 = tk.Entry(network_area_frame, bd=2)
        osn5.grid(row=6, column=2)
            
        tk.Label(network_area_frame, text="Router Priority : ").grid(row=7, column=0)
        global ospfpri
        ospfpri = tk.Entry(network_area_frame, bd=2)
        ospfpri.grid(row=7, column=1)
            
        tk.Button(network_area_frame, text="Set",command=lambda:self.set_ospf()).grid(row=8, column=0, columnspan=3)
    
    def sel2(self):
        selection = "You have selected EIGRP"
        label.config(text = selection)
        route_app = tk.Tk()
        route_app.title("EIGRP")
            
        network_area_frame = tk.Frame(route_app)
        network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
            
        tk.Label(network_area_frame, text="EIGRP Nextwork Area").grid(row=0, column=0, columnspan=3)
            
        tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
        tk.Label(network_area_frame, text="Wild Card").grid(row=1, column=2)
            
        tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
        global enw1,esn1
        enw1 = tk.Entry(network_area_frame, bd=2)
        enw1.grid(row=2, column=1)
        esn1 = tk.Entry(network_area_frame, bd=2)
        esn1.grid(row=2, column=2)
            
        tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
        global enw2,esn2
        enw2 = tk.Entry(network_area_frame, bd=2)
        enw2.grid(row=3, column=1)
        esn2 = tk.Entry(network_area_frame, bd=2)
        esn2.grid(row=3, column=2)
            
        tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
        global enw3,esn3
        enw3 = tk.Entry(network_area_frame, bd=2)
        enw3.grid(row=4, column=1)
        esn3 = tk.Entry(network_area_frame, bd=2)
        esn3.grid(row=4, column=2)
            
        tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
        global enw4,esn4
        enw4 = tk.Entry(network_area_frame, bd=2)
        enw4.grid(row=5, column=1)
        esn4 = tk.Entry(network_area_frame, bd=2)
        esn4.grid(row=5, column=2)
            
        tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
        global enw5,esn5
        enw5 = tk.Entry(network_area_frame, bd=2)
        enw5.grid(row=6, column=1)
        esn5 = tk.Entry(network_area_frame, bd=2)
        esn5.grid(row=6, column=2)

        tk.Label(network_area_frame, text="Router Priority : ").grid(row=7, column=0)
        global eigrppri
        eigrppri = tk.Entry(network_area_frame, bd=2)
        eigrppri.grid(row=7, column=1)
            
        tk.Button(network_area_frame, text="Set",command=lambda:self.set_eigrp()).grid(row=7, column=0, columnspan=3)

    def sel3(self):
        selection = "You have selected RIPv2"
        label.config(text = selection)
        route_app = tk.Tk()
        route_app.title("RIPv2")
            
        network_area_frame = tk.Frame(route_app)
        network_area_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=5)
            
        tk.Label(network_area_frame, text="RIPv2 Nextwork Area").grid(row=0, column=0, columnspan=2)
            
        tk.Label(network_area_frame, text="Network Area").grid(row=1, column=1)
            
        tk.Label(network_area_frame, text="1 : ").grid(row=2, column=0)
        global rnw1
        rnw1 = tk.Entry(network_area_frame, bd=2)
        rnw1.grid(row=2, column=1)
            
        tk.Label(network_area_frame, text="2 : ").grid(row=3, column=0)
        global rnw2
        rnw2 = tk.Entry(network_area_frame, bd=2)
        rnw2.grid(row=3, column=1)
            
        tk.Label(network_area_frame, text="3 : ").grid(row=4, column=0)
        global rnw3
        rnw3 = tk.Entry(network_area_frame, bd=2)
        rnw3.grid(row=4, column=1)
            
        tk.Label(network_area_frame, text="4 : ").grid(row=5, column=0)
        global rnw4
        rnw4 = tk.Entry(network_area_frame, bd=2)
        rnw4.grid(row=5, column=1)
            
        tk.Label(network_area_frame, text="5 : ").grid(row=6, column=0)
        global rnw5
        rnw5 = tk.Entry(network_area_frame, bd=2)
        rnw5.grid(row=6, column=1)
        
        tk.Button(network_area_frame, text="Set",command=lambda:self.set_rip()).grid(row=7, column=0, columnspan=2)

    def shw_run(self):
        running = cmd.send_command("show run")
        runningConf.delete("1.0", "end")
        runningConf.insert(tk.END, running)
        
    def shw_ip_route(self):
        routee = cmd.send_command("show ip route")
        runningConf.delete("1.0", "end")
        runningConf.insert(tk.END, routee)
        
    def shw_ip_int(self):
        intbr = cmd.send_command("show ip int br")
        runningConf.delete("1.0", "end")
        runningConf.insert(tk.END, intbr)
        
    def shw_ip_ospf(self):
        ospf_nei = cmd.send_command("show ip ospf neighbor")
        runningConf.delete("1.0", "end")
        runningConf.insert(tk.END, ospf_nei)
        
    def shw_ip_eigrp(self):
        eigrp_nei = cmd.send_command("show ip eigrp neighbor")
        runningConf.delete("1.0", "end")
        runningConf.insert(tk.END, eigrp_nei)

    def add_ip_to_interface(self):
        int = interface_form.get()
        ip = ip_form.get()
        subnet = subnetmask.get()
        result = cmd.send_config_set(["int {0}".format(int), "ip address {0} {1}".format(ip,subnet)])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if interface_form.get() == "" or ip_form.get() == "" or subnetmask.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
    
    def int_shutdown(self):
        int = interface_form.get()
        result = cmd.send_config_set(["int {0}".format(int),"shutdown"])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if interface_form.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
    def int_no_shutdown(self):
        int = interface_form.get()
        result = cmd.send_config_set(["int {0}".format(int),"no shutdown"])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if interface_form.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
    
    def set_ntp(self):
        ip = ntps.get()
        result = cmd.send_config_set(["ntp server {0}".format(ip)])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if ntps.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
    def set_syslog(self):
        ip = syslogs.get()
        result = cmd.send_config_set(["logging {0}".format(ip),"logging trap debugging","service timestamps log datetime msec"])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if syslogs.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
    
    def static_route(self):
        dest = destination.get()
        subnet = subnetmask_static.get()
        next = nexthop.get()
        result = cmd.send_config_set(["ip route {0} {1} {2}".format(dest,subnet,next)])
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)
        if destination.get() == "" or subnetmask_static.get() == "" or nexthop.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
        
    def set_dhcp(self):
        pool = pool_name.get()
        net = net_area.get()
        sn = snm.get()
        df = default.get()
        dn = dns.get()
        dm = dm_name.get()
        dhcp_pool = ["ip dhcp pool {0}".format(pool),"network {0} {1}".format(net,sn),"default-router {0}".format(df)]
        if dns.get() != "":
            dhcp_pool.append("dns-server {0}".format(dn))
        if dm_name.get() != "":
            dhcp_pool.append("domain-name {0}".format(dm))
        if pool_name.get() == "" or net_area.get() == "" or snm.get() == "" or default.get() == "":
            messagebox.showerror(title="Cisco IOS Telnet", message="Please fill out the information correctly!")
        result = cmd.send_config_set(dhcp_pool)
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)

    def set_ospf(self):
        ospf_nwlist = [onw1.get(),onw2.get(),onw3.get(),onw4.get(),onw5.get()]
        ospf_snlist = [osn1.get(),osn2.get(),osn3.get(),osn4.get(),osn5.get()]
        ospf_nw = ["router ospf 1"]
        for i in range(5):
            if ospf_nwlist[i] != "" and ospf_snlist[i] != "":
                ospf_nw.append("network {0} {1} area 0".format(ospf_nwlist[i],ospf_snlist[i]))
        if ospfpri.get() != "":
            ospf_nw.append("router-id {0}".format(ospfpri.get()))
        result = cmd.send_config_set(ospf_nw)
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)

    def set_eigrp(self):
        eigrp_nwlist = [enw1.get(),enw2.get(),enw3.get(),enw4.get(),enw5.get()]
        eigrp_snlist = [esn1.get(),esn2.get(),esn3.get(),esn4.get(),esn5.get()]
        eigrp_nw = ["router eigrp 1","no auto-summary"]
        for i in range(5):
            if eigrp_nwlist[i] != "" and eigrp_snlist[i] != "":
                eigrp_nw.append("network {0} {1}".format(eigrp_nwlist[i],eigrp_snlist[i]))
        if eigrppri.get() != "":
            eigrp_nw.append("eigrp router-id {0}".format(eigrppri.get()))
        result = cmd.send_config_set(eigrp_nw)
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)

    def set_rip(self):
        rip_nwlist = [rnw1.get(),rnw2.get(),rnw3.get(),rnw4.get(),rnw5.get()]
        rip_nw = ["router rip","version 2", "no auto-summary"]
        for i in range(5):
            if rip_nwlist[i] != "":
                rip_nw.append("network {0}".format(rip_nwlist[i]))
        print(rip_nw)
        result = cmd.send_config_set(rip_nw)
        runningConf.delete("1.0","end")
        runningConf.insert(tk.END, result)


#-----------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    


