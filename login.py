import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Cisco IOS Telnet")
        #setting window size
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
        lb_ip["fg"] = "#333333"
        lb_ip["justify"] = "center"
        lb_ip["text"] = "IP"
        lb_ip.place(x=100,y=30,width=70,height=25)

        GLineEdit_321=tk.Entry(root)
        GLineEdit_321["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=11)
        GLineEdit_321["font"] = tkFont.Font(family='Times',size=11)
        GLineEdit_321["fg"] = "#333333"
        GLineEdit_321["justify"] = "left"
        # GLineEdit_321["text"] = "zxczxc"
        GLineEdit_321.place(x=200,y=30,width=90,height=25)

        lb_port=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_port["font"] = ft
        lb_port["fg"] = "#333333"
        lb_port["justify"] = "left"
        lb_port["text"] = "Port"
        lb_port.place(x=100,y=80,width=70,height=25)

        lb_username=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_username["font"] = ft
        lb_username["fg"] = "#333333"
        lb_username["justify"] = "right"
        lb_username["text"] = "Username"
        lb_username.place(x=100,y=130,width=70,height=25)

        btn_cancel=tk.Button(root)
        btn_cancel["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        btn_cancel["font"] = ft
        btn_cancel["fg"] = "#000000"
        btn_cancel["justify"] = "center"
        btn_cancel["text"] = "Cancel"
        btn_cancel.place(x=200,y=230,width=70,height=25)
        btn_cancel["command"] = self.GButton_342_command

        lb_password=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        lb_password["font"] = ft
        lb_password["fg"] = "#333333"
        lb_password["justify"] = "right"
        lb_password["text"] = "Password"
        lb_password.place(x=100,y=180,width=70,height=25)

        txt_2=tk.Entry(root)
        txt_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        txt_2["font"] = ft
        txt_2["fg"] = "#333333"
        txt_2["justify"] = "left"
        txt_2["text"] = ""
        txt_2.place(x=200,y=80,width=90,height=25)

        GLineEdit_304=tk.Entry(root)
        GLineEdit_304["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        GLineEdit_304["font"] = ft
        GLineEdit_304["fg"] = "#333333"
        GLineEdit_304["justify"] = "left"
        GLineEdit_304["text"] = ""
        GLineEdit_304.place(x=200,y=130,width=90,height=25)

        GLineEdit_584=tk.Entry(root)
        GLineEdit_584["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        GLineEdit_584["font"] = ft
        GLineEdit_584["fg"] = "#333333"
        GLineEdit_584["justify"] = "left"
        GLineEdit_584["text"] = ""
        GLineEdit_584.place(x=200,y=180,width=90,height=25)

        btn_connect=tk.Button(root)
        btn_connect["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        btn_connect["font"] = ft
        btn_connect["fg"] = "#000000"
        btn_connect["justify"] = "center"
        btn_connect["text"] = "Connect"
        btn_connect.place(x=100,y=230,width=70,height=25)
        btn_connect["command"] = self.GButton_482_command


    def GButton_342_command(self):
        print("command")


    def GButton_482_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
