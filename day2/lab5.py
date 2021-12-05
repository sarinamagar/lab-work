#desks 
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