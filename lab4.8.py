#Given an array 3,6,9,12,23 
# create another array containing the squared number of each number 
# from the array to second array

array = [3,6,9,12,23]
square=[]

for i in range(0,5) :

  square.append(array[i]*array[i])

  print(square[i])