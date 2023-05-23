from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        
# def send_config_set(device, commands):
#     result = {}
#     try:
#         with ConnectHandler(**device) as ssh:
#             ssh.enable()
#             for command in commands:
#                 output = ssh.send_config_set(command)
#                 result[command] = output
#         return result
#     except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
#         print(error)
        


if __name__ == "__main__":
    device = {
        "device_type": "cisco_ios_telnet",
        "host": "172.30.230.46",
        # "username": "cisco",
        # "password": "cisco",
        # "secret": "cisco",
        "port": "5003"
    }
    
    
    # result = send_show_command(device, ["sh run"])
    send_config_set(device, ["int f0/0\r\nno shutdown"])
    # pprint(result, width=120)
