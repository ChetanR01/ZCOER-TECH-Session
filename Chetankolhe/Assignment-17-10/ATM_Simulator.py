acc_balance = 0
while True:
    temp = int(input("Select Choice :- \n1.Withdraw\n2.Deposite\n3.Check_Balance\n4.exit\n"))
    if(temp ==1):
        amount = int(input("Enter the Amount To Be Withdraw:- "))
        if(amount<acc_balance):
            acc_balance=acc_balance-amount
            print("Your A/c No xxxxx890 debited by INR",amount, ".A/c Balance is INR",acc_balance)
        else:
            print("Insufficient Balance \n"
                  "Verify The Account Balance")
            
    elif(temp ==2):
        amount2 = int(input("Enter the Amount To Be Deposited:- "))
        acc_balance=acc_balance+amount2
        print("Your A/c No xxxxx890 credited by INR",amount2, ".A/c Balance is INR",acc_balance)
        
    elif(temp==3):
        print("Your A/c No xxxxx890 A/c Balance is INR",acc_balance)
    
    elif(temp==4):
        print("Thankyou For Visit\n"
              "Visit Again !!!")
        break
        
    else:
        print("Invalid Choice")