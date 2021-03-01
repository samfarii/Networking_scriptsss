import os
import re
import csv
import io
import textfsm

# template for text fsm to extract the vlan ids per device
template = io.StringIO("""\
Value Port (\S+(/\d+)?)
Value Vlans (\d+([-,]\d+)+)

Start
  ^Port\s+Vlans allowed on trunk$$ -> Begin

Begin
  ^${Port}\s+${Vlans}$$ -> Record
  ^Port\s+Vlans allowed and active in management domain$$ -> End
""")

files = os.listdir(r"C:\Users\Fariyikes\RCC_Backup_18022021\New")

for j in files:
    #extract device ip addresses from the text file name
    if "output.txt" in j:
        device_ip = re.findall("(\d+\.\d+\.\d+\.\d+)", j)
        device_ip = device_ip[0]
        print(f"Starting the parse for trunks on device = {device_ip}")
    #open file and parse using TextFSM


        with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\New\{j}", "r") as f:
            fsm = textfsm.TextFSM(template)
            result = fsm.ParseText(f.read())

            print(f"Now printing the trunks for:  ", device_ip)

            with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\RCC_device_trunks2.csv", "a", newline='') as g:
                writer = csv.writer(g)
                y = list(result)
                #Convert the list of trunk interfaces and VLANS into a list, append the router ID to the list and then print to csv so it's easier to filter in csv
                #y.append(device_ip)
                for i in y:
                    i.append(device_ip)
                    print(i)
                    writer.writerow(i)

        print(f"The trunks have been extracted for device = {device_ip}\n")
