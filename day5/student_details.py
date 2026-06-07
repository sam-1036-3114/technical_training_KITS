dic={101:"sam",102:'mam',103:'wow',104:'potato'}
print(dic)
dic[106]='man'
print(dic)
del dic[103]
print("prsent " if 101 in dic else "absent")
print(dic)
del dic[101]
print(dic)
print(dic.values())
print(dic.keys())
dic.clear()
print(dic)
a=dic.copy()
print(a)
print(dic)
colors={}
values=('red','blue')
keys=(101,102)
print(colors.fromkeys(values,keys))
colors1={}
values1={'red','blue'}
keys1={101,102}
print(colors1.fromkeys(values1,keys1))