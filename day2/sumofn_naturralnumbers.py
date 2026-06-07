n=int(input("enter the n value:"))
Sum=0
for i in range(1,n+1):
    Sum+=i
#print(f"the sum is : {Sum}")
print(sum(range(1,n+1)))