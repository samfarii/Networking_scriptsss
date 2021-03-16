import os
import re
import csv
import io
import textfsm

# template for text fsm to extract the switch ports, SW, version per device
template = io.StringIO("""\
Value Switch (\d+)
Value Ports (\d+)
Value Model (\S+)
Value Version (\S+)
Value Image (\S+)

Start
  ^\*\s+${Switch}\s+${Ports}\s+${Model}\s+${Version}\s+${Image} -> Record
  """)

files = os.listdir(r"C:\Users\Fariyikes\RCC_Backup_18022021")

for j in files:
    #extract device ip addresses from the text file name
    if "output.txt" in j:
        device_ip = re.findall("(\d+\.\d+\.\d+\.\d+)", j)
        device_ip = device_ip[0]
        print(f"Starting the parse for sw version on device = {device_ip}")
    #open file and parse using TextFSM


        with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\{j}", "r") as f:
            fsm = textfsm.TextFSM(template)
            result = fsm.ParseText(f.read())

            print(f"Now printing the sw version details for:  ", device_ip)

            with open(fr"C:\Users\Fariyikes\RCC_Backup_18022021\RCC_device_sw_version.csv", "a", newline='') as g:
                writer = csv.writer(g)
                y = list(result)
                #Convert the output into a list of ports, SW, version and append the router ID to the list, then print to csv so it's easier to filter in csv
                #y.append(device_ip)
                for i in y:
                    i.append(device_ip)
                    print(i)
                    writer.writerow(i)

        print(f"The sw version has been extracted for device = {device_ip}\n")
