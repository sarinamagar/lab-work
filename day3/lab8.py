#Given a n-digit number. Find the sum of its digits.
sum = 0
inp = int(input("num"))
in_str = str(inp)
for x in in_str:
    sum = sum + int(x)

print(sum)