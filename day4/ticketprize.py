size=int(input("Enter th size of the list: "))
age=[]
for i in range(1,size+1):
    ele=int(input("enter the age of the people: "))
    age.append(ele)
print("the age of people u have entered: ",age)
for i in age:
    if i<12:
        print(f"the ticket price for the people of age below {i}: $10.")
    elif i>=12 and i<=60:
        print(f"the ticket price for the people of age {i}: $15$.")
    else:
        print(f"the ticket price for the people of age  {i}: $12.")