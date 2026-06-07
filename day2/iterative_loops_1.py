for i in range(1,11):
    print("hello world!")
#to print natural numbers from n to 1
n=int(input("enter the value of n: "))
for i in range(n,0,-1):
    print(i,end=" ")
    
    
#write a python program to print the first n odd numbers
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    print(f"even number: {i}" if i%2==0 else f"odd number: {i}")