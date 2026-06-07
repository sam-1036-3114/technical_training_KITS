list1=list(map(int,input("enter the prices: ").split()))
list2=[price for price in list1 if price>1000]
print(list2)