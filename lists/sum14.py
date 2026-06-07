list1=list(map(bool,input(" enter the expenses").split()))
if all(list1)==True:
    print("all server are up: True | all servers are down: false ")
else:
    print("all server are up: false | all servers are down: True ")