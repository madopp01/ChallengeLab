from netmiko import ConnectHandler
import time


print("HENTER STATUS PÅ ALLE INTERFACES VIA SSH:")
ssh = ConnectHandler(
    device_type="cisco_ios",
    host="172.20.100.79",
    port="22",
    username="cisco",
    password="cisco123!"
    )
send_show_ip_brief=ssh.send_command("show ip interface brief")
print()
print(send_show_ip_brief)
print()
print("OPSÆTTER LOOPBACK 7 INTERFACE VIA SSH:")
interface_create =  [
    "int loopback 7",
    "ip address 14.15.16.17 255.255.255.0",
    "description oprettet med netmiko",
    "no shutdown"
]
send_interface_commands = ssh.send_config_set(interface_create)
print()
time.sleep(4)
print("SUCCESS")
time.sleep(4)
print()
print("HENTER LOOPBACK 7 INTERFACE VIA SSH:")
send_show_loopback_interface=ssh.send_command("show run interface Loopback 7")
print()
time.sleep(4)
print(send_show_loopback_interface)