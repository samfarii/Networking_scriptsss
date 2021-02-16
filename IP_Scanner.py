#! usr/bin/env python3

import re
import os


def main():
    subnet_supplied = input("please provide the subnet you would ike to check e.g x.x.x.x/24:  \n ")
    if "/24" in subnet_supplied:
        return subnet_24_confirmation(subnet_supplied)
    elif "/25" in subnet_supplied:
        return subnet_25_confirmation(subnet_supplied)

def subnet_24_confirmation(subnet_to_check):
    confirmation = input(f"please indicate y/n if this is the subnet {subnet_to_check} you want to scan and press enter: \n")
    try:
        assert "/24" in subnet_to_check
        if "y" in confirmation:
            return subnet_24(subnet_to_check)
        else:
           return main()
    except AssertionError:
        print("The subnet you provided is not a /24, please supply a valid /24 subnet to check")
        main()

def subnet_25_confirmation(subnet_to_check):
    confirmation = input(f"please indicate y/n if this is the subnet {subnet_to_check} you want to scan and press enter: \n")
    try:
        assert "/25" in subnet_to_check
        if "y" in confirmation:
            return subnet_25(subnet_to_check)
        else:
           return main()
    except AssertionError:
        print("The subnet you provided is not a /25, please supply a valid /25 subnet to check")
        main()

def subnet_24(subnet):
    ''' The /24 subnet will be pinged
    and output written to a file appended with the subnet id '''

    net_portion = re.search("(\d+\.\d+\.\d+)\.\d+", subnet).group(1)
    print(f"Starting the ping routine for {net_portion}.0/24 range...\n")
    ip_no_subnet = subnet.strip("/24")
    with open(f"ping_output_{net_portion}.0_24.txt", "w") as f:
        for i in range(1,255):
            ping_output = os.popen(f"ping -c 1 {net_portion}.{i}")
            if "ttl" in ping_output.read():
                f.write(f"{net_portion}.{i} is UP \n")
            else:
                f.write(f"{net_portion}.{i} is unreachable \n")

        print(f"Scan for {net_portion}.0/24 range has been completed \n")

if __name__ == "__main__":
    main()
