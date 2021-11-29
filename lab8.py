#sum of odd number
n=int(input("emter the number upto which you want to add : "))
i=1
sum=0
while i<=n:
    if i%2==1:
     sum=sum+i
    i=i+2
print("sum of odd number:",sum)
