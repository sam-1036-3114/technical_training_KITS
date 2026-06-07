print("Welcome to pizza hotel")
cost=0
while(True):
    print("do u want to order the pizza:c")
    print("enter 1 to order:")
    print("enter 2 to exit")
    choice1=int(input("enter the your choice"))
    if(choice1==1):
        print("how many pizza do you want to order: ")
        p_num=int(input())
        for i in range(1,p_num+1):
            print("choose the size of the of order: ")
            print("choose the pizza size: ")
            print("1.the small pizza: 10$ ")
            print("2.the medium pizza: 15$ ")
            print("3.the large pizza:20$")
            choice2=int(input("enter the your choice: "))
            if choice2==1:
                cost+=10
            elif choice2==2:
                cost+=15
            else:
                cost+=20
            print(f"the cost without toppings:{cost}")
        print("how many topping do you want to add:")
        t_num=int(input())
        for i in range(1,t_num+1):
                choice3=int(input("select 1. to choose the toppings and 2. not to order topings "))
                if choice3==1:
                    print("the topping available are: ")
                    print("1.chees:2$")
                    print("2.peperment:3$")
                    print("3:oliver:4$")
                    print("4:jalapenos:5$")
                    choice4=int(input("Enter the input:"))
                    if choice4==1:
                        cost+=2
                    elif choice4==2:
                        cost+=3
                    elif choice4==3:
                        cost+=4
                    elif choice4==4:
                        cost+=5
                    print(f"the total cost:{cost}")
                else:
                    print(f"the total cost:{cost}")
    else:
        exit()
        
            
            
    