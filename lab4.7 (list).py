#display the student names in reverse order
# student_name[0]="Law qian er", student_name[1]="Wong Bing Jie" , student_name[2] ="Khoo Chong Qin"

student_name = ["Law Qian Er\n\n", "Wong Bing Jie", "Khoo Chong Qin"]
student_name.reverse()
for name in student_name:
    print(name)


#method 2

student_name = ["Law Qian Er", "Wong Bing Jie", "Khoo Chong Qin"]
student_name.append("Suhaimi")

for student_index in range(3,-1,-1):  #2,1,0
    print(student_name[student_index])


#student_name.reverse...reverse list
#student_name.append...to add a new value
#student_name.remove...to remove the value



