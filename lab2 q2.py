#student id : 1201200449
#student name : Lai Jian Hong
#lab2 question 2

FT=0.3048  #constant value, mean the value doesn't change , name is Capital letters

feet = float(input("Please enter the value of feet:"))

meter=FT*feet

print("The meter is",meter,"and feet is",feet)

print("For{:.2f} feet is equivalent to {:.2f} meters".format(feet,meter))