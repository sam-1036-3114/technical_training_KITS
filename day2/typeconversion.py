
num1=1234
siz=str(num1)
numsize=len(siz)
print(siz)
revnum=0
print(numsize)
while(numsize!=0):
    lastnum=num1%10
    siz=num1/10
    revnum=lastnum*10+revnum
    numsize-=1
print(revnum)
print
