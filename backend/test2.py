
from netmiko import ConnectHandler

cisco_ios = {
    "device_type": "cisco_ios_telnet",
    "host": "172.30.230.46",
    "port" : "5003"
}
cmd = ConnectHandler(**cisco_ios)
cmd.enable()
cmd.send_command("show ip int br")



