#A school decided to replace the desks in three classrooms. Each desk sits two students.
#Given the number of students in each class, print the smallest possible number of desks
#that can be purchased.
#The program should read three integers: the number of students in each of the three
#classes, a, b and c respectively.
#Suppose In the first test there are three groups. The first group has 20 students and thus needs 10
#desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
 
a=int(input("no. of students in class a : "))
classA= a//2
b=int(input("no of students in class b : "))
classB= b//2
c=int(input("no of students in class c : "))
classC= c//2
print(f"no of chairs needed in class A= {classA}")
print(f"no of chairs needed in class B={classB}")
print(f"no of chairs needed in class C={classC}")
remaining_chairsA=a%2
remaining_chairsB=b%2
remaining_chairsC=c%2
print(f"remaining chairs in class A: {remaining_chairsA}")
print(f"remaining chairs in class B: {remaining_chairsB}")
print(f"remaining chairs in class C: {remaining_chairsC}")