for i in range(1,5):
    if(i==2):
        break
    if(i==3):
        continue
    print("helo")
    for i in range(1,11):
        if i%2==0:
            print(f"5 X {i} = {5*i}")