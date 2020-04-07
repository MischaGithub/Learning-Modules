#This program illustrates the importance of modules

side_of_square = int(input("Please enter the size of one side: \n"))

import modules

Area = modules.area_of_square(side_of_square)

print("Area of a square is", Area, "cm2")

import platform

x = platform.machine()
print(x)

y = platform.architecture()
print(y)