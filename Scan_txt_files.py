#! usr/bin/env python3

import os

textfiles = []
files = os.listdir("/home/farii/Desktop")
for i in files:
    if ".txt" in i:
        textfiles.append(i)
print(textfiles)
for j in textfiles:
    with open(j, "r") as f:
        if "is unreachable" in f.read():
            print(f"It's in this file {j} \n")
