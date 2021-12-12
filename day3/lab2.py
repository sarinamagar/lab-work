'''WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
'''
sub1=int(input("enter your marks for english"))
sub2=int(input("enter your marks for maths"))
sub3=int(input("enter your marks for science"))
sub4=int(input("enter your marks for computer"))
total_marks= (sub1 + sub2 + sub3 + sub4)
percentage= ((total_marks/400)*100)
print("total marks =",total_marks)
print("percentage =",percentage)
if percentage>70 :
    print("grade = distinction")
elif percentage <=70 and percentage>60:
    print("grade =first")
elif percentage <=60 and percentage >40:
    print("grade = pass")
else:
    print("grade = fail")