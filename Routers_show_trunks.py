import os
import re
import csv
from netmiko import ConnectHandler


with open(r"C:\Users\Fariyikes\RCC_Backup_18022021\router.txt", "r") as file:

    for device_row in file:

        try:
            router_ip = device_row.strip()
            ssh_username = "admin-fariyikes"
            #ssh_password = getpass.getpass('SSH Password: ')
            ssh_password = "xxxxxxx"
            ssh_session = ConnectHandler(device_type='cisco_ios', ip=router_ip,
            username=ssh_username, password=ssh_password, global_delay_factor=2)
            with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\New\router_{router_ip}_output.txt", "a") as y:
                o = ssh_session.send_command("term len 0")
                y.write(o)
                print("term len 0")
                t = ssh_session.send_command("show int trunk")
                print("show int trunk")
                y.write(t)
                print(f"The output for {router_ip} has been saved")

        except:
            with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\New\Unreachable_trunk_devices.txt", "a") as g:
                g.write(f"{router_ip} authentication failed \n")
                print(f"Authentication for {router_ip} failed")
