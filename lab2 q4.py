#student id : 1201200449
#student name : Lai Jian Hong
#lab2 question 4

banana=1.5
grapes=5.60


qty_banana=int(input("Enter the quantity(comb)of banana bought :"))
qty_grapes=int(input("Enter the quantity(kg)of grapes bought:"))

total_banana=banana*qty_banana
total_grapes=grapes*qty_grapes
price=total_banana+total_grapes

print("Item \t\t        Qty \t\t   Price   3\t Total")
print("Banana(comb)" "\t\t" ,qty_banana, "\t\tRM",banana ,"\t\tRM",total_banana)
print("Grapes(kg)"  "\t\t" ,qty_grapes  ,"\t\tRM",grapes ,"\t\tRM",total_grapes)
print("Total :RM{:.2f}".format(price))

