#flow control statements
#1.conditional statements
#2.loops or iterative statements
#3.transfer statements
#1. conditional statements or decision-making:if,if-else,if-elif-else
#2.loops or iterative statements:for loop,while loop,
#3.transfer statements:break,continue,pass
#if-else statement:
#if condition:
    #block of code to be executed if the condition is true
#else:
    #block of code to be executed if the condition is false
# NOW write the python program whenther the age is valid to vote or not
age=int(input("Enter your age: "))
if(age>=18):
    print("you are eligible to vote")
else:
    print("You are not eligible to vote")

res="not eligible to vote" if age<18 else "eligible to vote"
print(f"you are {res}")
#write a python program to read an interger value from the user and check whter it is positive or negative or zero
num=int(input("Enter the value:"))
if num>0:
    print("the number is positive")
elif(num==0):
    print("the number is zero")
else:
    print("the number is negative")
    #write a python program to read two interger values as input and find the largest number
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("the largest number is: ",num1 if num1>num2 else num2)
print("the number is :",num1 if num1>num2 else num2,"both are equal" if num1==num2 else "")
#write the pythonn program to read the input from the user and check the whether the month number is valid or not
month=int(input("Enter the month number: "))
print("valid month number"if month in range(1,13) else "invalid month")
#w rite a python program to read the month number and print the days in  the month
