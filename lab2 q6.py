#student id : 1201200449
#student name : Lai Jian Hong
#lab2 question 6

import math 

math.pi=22/7
radius = float(input("Enter the radius:" ))
sur_area = 4 * math.pi * pow(radius,2)
volume = (4/3) * math.pi * pow(radius,3)
print("The volume is: {:.2f} ".format(volume))
print("The surface area is: {:.2f} ".format(sur_area))
