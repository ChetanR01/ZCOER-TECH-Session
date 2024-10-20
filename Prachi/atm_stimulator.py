balance=10000

while True:

    print("Enter\t1.Check Balance\n\t2.Deposit money\n\t3.Withdraw money\n\t4.Exit")
    i=int(input())
    if i==1:
        print(balance)
        print("Balance is checked successfully !")

    elif i==2:
        dep_money=int(input("Enter amount of money to be deposited : "))
        balance+=dep_money
        print("Money is deposited successfully !")

    elif i==3:
        wit_money=int(input("Enter amount of money to be withdrawn : "))
        balance-=wit_money
        print("Money is deposited successfully !")

    elif i==4:
        break
    
