
balance = {"Rudrali":100000,"Raksha":100000,"Tanisha":10000}
c=0
while c!=4:

    print("Menu")
    print("choice 1 :Check Balance")
    print("choice 2 :Deposit Money")
    print("choice 3 :Withdraw Money")
    print("choice 4 :Exit")
    print("\n")


    
    c = int(input("Enter your choice : "))
    
    
    if c == 1 :
        try :

            user = input("Enter username : ")
            if user not in (balance.keys()):
                raise Exception("Sorry, no such username")

            user = user.capitalize()
            print("Total Balance :",balance[user])
        except :
            print("Enter valid username")

    elif c == 2:

        user = input("Enter username : ")
        user = user.capitalize()
       
        D_amt = int(input("Enter amount to deposit :"))
        balance[user] +=D_amt

    elif c == 3 :

        user = input("Enter username : ")
        user = user.capitalize()
        
        W_amt = int(input("Enter amount to withdraw : "))

        if balance[user]>=W_amt:
            print("withdraw amount : ",W_amt)
            print("Balance in account : ",balance[user])

            balance[user]-=W_amt

        else :
            print("Insuffient amount...\nMoney can't be Debited")


    else :
        if c!=4:
            print("Enter valid choice\n")

