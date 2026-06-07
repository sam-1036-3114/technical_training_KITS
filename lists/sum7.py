list1=list(map(int,input("enter the input : ").split()))
list3=[]
for i in list1:
    
    print("the count is :",list1.count(i))
    if list1.count(i)>1 and i not in list3:
        list3.append(i)
list2=list(set(list1))
print(list2)
print(list3 if len(list3)>0 else "no duplicates")