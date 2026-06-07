num=int(input("enter the number: "))
print("reversed multiplication table")

for i in range(num,0,-1):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
        
print("normal multiplication table")
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
 