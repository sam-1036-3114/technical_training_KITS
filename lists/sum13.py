# list1=list(map(int,input().split()))
# for i,j in enumerate(list1,start=1):
#     print(i,j)
list1=list(map(int,input(" enter the expenses").split()))
for i,j in enumerate(list1,start=1):
    print(f"the day{i}:{j}  ")
    if len(list1)==i:
        print(f"the total:| {sum(list1)}")

