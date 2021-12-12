#write a python program to sum three given integers. However, if two or more values are equal sum will be zero.
a= int(input("enter the 1st number"))
b= int(input("enter the 3nd number"))
c= int(input("enter the 4th number"))
total=a+b+c
if a==b==c or a==b or a==c:
    print("the sum is 0")
else:
    print("the sum of three number = ",total)