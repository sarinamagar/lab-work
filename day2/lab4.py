#apples
n= int(input("no. of students ="))
k= int(input("no of apples ="))
apples = k//n
remaining_apples= k%n
print(f"each student got {apples} apples",)
print(f"{remaining_apples} apples are remaining")