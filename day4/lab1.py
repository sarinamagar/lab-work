#check whether the giver year is a leap year or not
year= int(input("enter the year"))
if (year%4==0 and year %100!=0 or year%400==0):
    print("it ia a leap year")
else:
    print("it is not a leap year")
