# student id :1201200449
#student name : lai Jian hong


def rectangle(width,length):
   area=width*length
   return area

   
def triangle(width,length):
    area=width*length/2
    return area

width=float(input("Enter width :"))
length=float(input("Enter length :"))

area_r=rectangle(width,length)
area_t=triangle(width,length)

print("Rectangle area :{:.2f} ".format(area_r))
print("Triangle area :{:.2f} ".format(area_t))