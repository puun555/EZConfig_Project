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

        GLabel_649=tk.Label(root)
        GLabel_649["bg"] = "#f80000"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_649["font"] = ft
        GLabel_649["fg"] = "#333333"
        GLabel_649["justify"] = "right"
        GLabel_649["text"] = "IP"
        GLabel_649.place(x=100,y=30,width=70,height=25)

        GLineEdit_321=tk.Entry(root)
        GLineEdit_321["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_321["font"] = ft
        GLineEdit_321["fg"] = "#333333"
        GLineEdit_321["justify"] = "center"
        GLineEdit_321["text"] = "Entry"
        GLineEdit_321.place(x=200,y=30,width=88,height=25)

        GLabel_658=tk.Label(root)
        GLabel_658["bg"] = "#ff1919"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_658["font"] = ft
        GLabel_658["fg"] = "#333333"
        GLabel_658["justify"] = "right"
        GLabel_658["text"] = "Port"
        GLabel_658.place(x=100,y=80,width=70,height=25)

        GLabel_600=tk.Label(root)
        GLabel_600["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["justify"] = "right"
        GLabel_600["text"] = "Username"
        GLabel_600.place(x=100,y=130,width=70,height=25)

        GButton_342=tk.Button(root)
        GButton_342["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_342["font"] = ft
        GButton_342["fg"] = "#000000"
        GButton_342["justify"] = "center"
        GButton_342["text"] = "Button"
        GButton_342.place(x=160,y=240,width=70,height=25)
        GButton_342["command"] = self.GButton_342_command

        GLabel_988=tk.Label(root)
        GLabel_988["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_988["font"] = ft
        GLabel_988["fg"] = "#333333"
        GLabel_988["justify"] = "right"
        GLabel_988["text"] = "Password"
        GLabel_988.place(x=100,y=180,width=70,height=25)

        GLineEdit_453=tk.Entry(root)
        GLineEdit_453["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_453["font"] = ft
        GLineEdit_453["fg"] = "#333333"
        GLineEdit_453["justify"] = "center"
        GLineEdit_453["text"] = "Entry"
        GLineEdit_453.place(x=200,y=80,width=68,height=25)

        GLineEdit_304=tk.Entry(root)
        GLineEdit_304["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_304["font"] = ft
        GLineEdit_304["fg"] = "#333333"
        GLineEdit_304["justify"] = "center"
        GLineEdit_304["text"] = "Entry"
        GLineEdit_304.place(x=200,y=130,width=70,height=25)

        GLineEdit_584=tk.Entry(root)
        GLineEdit_584["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_584["font"] = ft
        GLineEdit_584["fg"] = "#333333"
        GLineEdit_584["justify"] = "center"
        GLineEdit_584["text"] = "Entry"
        GLineEdit_584.place(x=200,y=180,width=70,height=25)

    def GButton_342_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
