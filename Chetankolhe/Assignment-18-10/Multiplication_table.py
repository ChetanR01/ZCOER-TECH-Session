while True:
    temp2 = int(input("Select Choice :- \n1.Display Table of perticular Number\n2.Display All Table From 1 to 10 \n3.Exit\n"))
    if(temp2 == 1):
        num = int(input("Enter The Number"))
        print(f"\nTable Of {num}\n")
        for i in range(1,11):
            print(f"{num} * {i} = {num*i}")
            
            
    elif(temp2 == 2):
        print("\nThe Multiplication Table From 1 to 10 are:- ")
        # i loop for the main numbers
        for i in range(1,11):
            print(f"\nTable Of {i}\n")
            # j loop for inner numbers 
            for j in range(1,11):
                 print(f"{i} * {j} = {i*j}")
            print("\n")
            
            
    elif(temp2 == 3):
        print("Thankyou For Visit \n"
              "Visit Again !!!")
        break
            
        