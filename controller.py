# controller
<<<<<<< Updated upstream
from netmiko import *
=======
from netmiko import *;
>>>>>>> Stashed changes

cisco_ios = {
    "device_type": "cisco_ios_telnet",
    "host": "10.144.10.10",
    "port" : "5002"
}

cmd = ConnectHandler(**cisco_ios)

global status
status = "privileged"


def enable():
    cmd.enable()
    
def show_ip_interface():
    result = cmd.send_command("show ip int br")
    print(result)
    
def ping():
    ip = input("Destination IP Address : ")
    result = cmd.send_command("ping %s" %ip)
    print(result)

def end():
    cmd.send_command("end")
    
def logout():
    end()
    cmd.send_command("logout")

    
def configTerminal():
    cmd.send_command("config terminal")
    
def addRoute():
    changeStatus("config")
    network_dest_ip = input("Network Destination Address : ")
    network_dest_subnet_mask = input("Network Destination Subnet Mask : ")
    nexthop_address = input("Nexthop Address : ")
    result = cmd.send_config_set("ip route %s %s %s" %(network_dest_ip,network_dest_subnet_mask,nexthop_address))
    print(result)
    
def showRunningConfig():
    changeStatus(status,"privileged")
    result = cmd.send_command("show run")
    print(result)
    
def writeToStartupConfig():
    changeStatus(status,"privileged")
    result = cmd.send_command("write")
    print(result)

def changeStatus(status, want):
    if status == "config":
        if want == "privileged":
            end()
            status = "privileged"
        elif want == "user":
            end()
            logout()
            status = "user"
    elif status == "user":
        if want == "privileged":
            enable()
            status = "privileged"
        elif want == "config":
            enable()
            configTerminal()
            status = "config"
    elif status == "privileged":
        if want == "config":
            configTerminal()
            status = "config"

# showRunningConfig()