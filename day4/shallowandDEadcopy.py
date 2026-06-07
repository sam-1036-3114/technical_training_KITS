import copy
a=[1,1,13,3,3]
b=[1,4,32,2]
print(a)
print(b)
a=copy.copy(b)
print(a)
b=copy.deepcopy(a)
print(a)
b.append(10)
print(a)
a.append(20)
print(a)
print(b)