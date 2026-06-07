rating=list(map(int,input("enter the ratings:").split()))

if len(rating)==0:
    print("empty list")
else:
    avg=sum(rating)/len(rating)
    res=round(avg,2)
    print(res)