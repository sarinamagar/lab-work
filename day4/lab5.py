#a student is not allowed to sit for the exams if his attendance is less than 75%
classes= int("enter the number of classes held")
atendance= int("enter the nuber of classes attended")
percentage =(atendance/classes)*100
if percentage>=75:
    print("the student is allowed to sit for the exam")
else:
    print("the student is not allowed to sit for the exam")
    