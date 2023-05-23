# controller
from netmiko import ConnectHandler

cisco_ios = {
    "device_type": "cisco_ios_telnet",
    "host": "172.30.230.46",
    "port" : "5003"
}
cmd = ConnectHandler(**cisco_ios)
def enable():
    cmd.enable()
    
def show_ip_interface():
    result = cmd.send_command("show ip int br")
    print(result)
    
def ping():
    ip = input("Destination IP Address : ")
    result = cmd.send_command("ping %s" %ip)
    print(result)
