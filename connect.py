from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.9",
    "username": "admin",
    "password": "password",
}

net_connect = ConnectHandler(**router)

output = net_connect.send_command("show running-config")

with open("router_backup.txt", "w") as file:
    file.write(output)

print("Backup saved successfully!")

net_connect.disconnect()
