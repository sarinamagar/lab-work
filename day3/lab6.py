#Given an integer number, print its last digit. 

inp = int(input("num"))
in_str = str(inp)
for x in in_str:
    sum = sum + int(x)

print(sum)