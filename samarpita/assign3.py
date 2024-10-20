'''Problem 3: ATM Simulator

Create an ATM simulator that allows users to perform basic banking operations. The program should:
Store the user's balance in a variable.
Provide options to check the balance, deposit money, and withdraw money.
For withdrawals, use if-else statements to ensure the withdrawal amount doesn't exceed the balance.
Use a while loop to allow the user to perform multiple operations until they choose to exit'''

users = {
    "u1" : {"id" : 1 , "balance" : 5000 },
     "u2" : {"id" : 2 , "balance" : 3000 },
     "u3" : {"id" : 3 , "balance" : 6000 }
}

flag =1


print("operations : 1. Show balance \n2. Deposit \n3. Wthdrawl")


while flag :
   
    op = int(input("enter operation no. : "))
    ID_ = int(input("enter id : "))
    
    if op == 1 :
        #show bal
        for x,y in users.items():
            b_id = y.get("id")
            if ID_ == b_id :
                print(y.get("balance"))
    
    elif op == 2 : 
        #for deposit             
        for x,y in users.items():
            d_id = y.get("id")
            if ID_ == d_id :
                bal2 = y.get("balance")
                dep = int(input("enter amt to be deposited : "))
                new_bal2 = bal2 + dep 
                users[x].update({"balance" : new_bal2})
                print("id and updated balance are : ",users[x].values())
    
    elif  op == 3 :
        #for withdrawl
        for x,y in users.items() :
            ident = y.get("id")
            if ID_ == ident :
                bal = y.get("balance")
                w_amt = int(input("enter withdrawl amt : "))
                if w_amt <=bal :
                    new_bal = bal-w_amt
                    users[x].update( {"balance" : new_bal })
                    print("id and updated balance are : ",users[x].values())
                else :
                    print("balance insufficient")          
        

    cont = input("do you wanna continue : ")
    if cont == 'y' or cont == 'Y' :
        flag = 1
    else :
        flag = 0    
    
     