# print Patriacia to Anita 
# add marsha at the fourth position
# update the name Phiona to Phiona Aladina
# display the length of the students list
# print all the student names using a for loop
# calculate the total marks for the student marks variable

student_name = ['Sandra','Patricia','Phiona', "Anita"]
student_marks =[80, 56,78, 90]

# 1)
print(student_name[1::])

# 2)
student_name.insert(3, "Marsha")
print(student_name)

# 3)
student_name[2] = "Phiona Aladina"
print(student_name)

# 4)
print(len(student_name))

# 5)

for name in student_name:
    print(name)

# 6)
total_sum = sum(student_marks)
print(f"The sum of student marks {student_marks} is: {total_sum}")