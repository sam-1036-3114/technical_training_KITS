list1=list(map(str,input("enter the premium list members: ").split()))
list2=list(map(str,input("enter the normal list members: ").split()))
for i in list1:
    if i in list2:
        print(i)