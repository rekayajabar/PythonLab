print('**** Welcome to the LAB grade calculator!****')
name = input('Who are we calculating grades for? ==>')
print(name)
print()
lab_grade = float(input('Enter the labs grade? ==>'))
if lab_grade >100:
    print('The lab value should be 100 or less. It should be changed to 100')
    lab_grade = 100
elif lab_grade <0:
    print('The lab value should be greater thean 0. It should be changed to 0')
    lab_grade = 0
print(lab_grade)
print()
exam_grade = float(input('Enter the EXAMS grade? ==>'))
if exam_grade >100:
    print('The lab value should be 100 or less. It should be changed to 100')
    exam_grade = 100
elif exam_grade <0:
    print('The lab value should be greater thean 0. It should be changed to 0')
    exam_grade = 0
print(exam_grade)
print()
attendance = float(input('Enter the Attendance grade? ==>'))
if attendance >100:
    print('The lab value should be 100 or less. It should be changed to 100')
    attendance = 100
elif attendance <0:
    print('The lab value should be greater thean 0. It should be changed to 0')
    attendance = 0
print(attendance)
print()
#after receiving an input, we will then multipy all grades by weight
lab_grade = (lab_grade * 0.7)
exam_grade = (exam_grade * 0.2)
attendance = (attendance * 0.1)
#after finding the weight, we will add and find the final grade
final_grade = (lab_grade + exam_grade + attendance)
print('The weighted grade for' , name , 'is' , final_grade)
if final_grade <=100 and final_grade >=90:
    print(name , 'has a letter grade of A')
elif final_grade <90 and final_grade >=80:
    print(name , 'has a letter grade of B')
elif final_grade <80 and final_grade >=70:
    print(name , 'has a letter grade of C')
elif final_grade <70 and final_grade >=60:
    print(name , 'has a letter grade of D')
elif final_grade <60 and final_grade >=0:
    print(name , 'has a letter grade of F')

print('****Thanks for using the Lab grade calculator ****')


