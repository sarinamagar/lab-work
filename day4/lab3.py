print("enter your age")
age =int(input())
print("enter your gender m or f")
gender= input()
if (gender =="F"or gender =="f") and 20<=age <=60:
    print("urban areas only")
elif (gender=="M" or gender =="m") and 20<=age <=60:
    print("urban areas only")
else:
    print("error")