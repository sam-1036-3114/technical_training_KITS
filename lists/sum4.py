#absentees counter
list1=list(map(str,input("Enter the attendence: ").split()))
count=0
for i in list1:
    if i=='Absent' or i=='absent' or i=='ABSENT':
        count+=1
print(count)