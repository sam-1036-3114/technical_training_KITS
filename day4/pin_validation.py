pin=int(input("Enter the pin: "))
acc_bal=0
if pin==1234:
    print("welcome to the bank")
    while(True):
        print("1.DEposit")
        print("2.withdrwal")
        print("3,Balance Inquiry")
        print("4.transaction History")
        print("5.exit")
        choice=int(input("Enter your choice to proceed action :"))
        if(choice==1):
            dep_amt=int(input("Enter your ammunt to add: "))
            acc_bal+=dep_amt
            print(f"Dear customer the acc no:xxxxxxx1543 is credited with{dep_amt} and at prsent avl balance is {acc_bal} ")
        elif choice==2:
            w_amt=int(input("enter the amount to with draw:"))
            if w_amt>acc_bal:
                print("insufficient acc balance")
            else:
                acc_bal-=w_amt
                print(f"the withdrawed amount is {w_amt}. avl balance = {acc_bal}")
        elif choice==3:
            print(f"the available balance in account{acc_bal}")
        else:
            exit()
else:
    print("Enter the valid pin")

    
