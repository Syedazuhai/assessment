student_marks = int(input("Enter the student's mark"))

if 70 <= student_marks <= 100:
    grade = "A"
elif 60 <= student_marks <= 69:
        grade = "B"
elif 50 <= student_marks <= 59:
    grade = "C"
elif 40 <= student_marks <= 49:
    grade = "D"
elif 30 <= student_marks <= 39:
    grade = "E"
elif 20 <= student_marks <= 29:
    grade = "F"
else:
    grade = ("Invalid student_marks")

print("The grade is:" , grade)
