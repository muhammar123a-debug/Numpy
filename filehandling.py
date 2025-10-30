import numpy as np


# Read File 
# file = open("info.txt", "r")
# data = file.read()
# print(data)
# file.close()

# Write File
file = open("info.txt", "w")
file.write("This is my persnal detail")
file.close()

file = open("info.txt", "r")
data = file.read()
print(data)
file.close()

