num1=int(input("Enter the first integer value: "))
num2=int(input("Enter the second integer value: "))
num3=int(input("Enter the third integer value: "))
print("the largest number is: ", max(num1,num2,num3))

print("the lowest number is: ",min(num1,num2,num3))
a = sorted([num1,num2,num3])
print(a[1],"is the middle number")
