list1=list(map(str,input("enter the email: ").split()))
print(list1)
list2=[]
for i in list1:
    if i.strip()!='':
        list2.append(i)
print(list2)