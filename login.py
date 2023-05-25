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
        self.destroy()

    def login(self):
        cmd = ConnectHandler(**cisco_ios)
        try:
            if cmd.is_alive:
                messagebox.showinfo(title="Cisco IOS Telnet", message="Connected Success!")
            else:
                messagebox.showerror(titile="Cisco IOS Telnet", message="Connected Failed!")
        except:
            p

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
