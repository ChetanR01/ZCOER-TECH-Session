
shopping_cart = []

c=0
while c!=4:
    print("Menu:")
    print("choice 1 :Add items to the cart")
    print("""list of items available 
          item\t\tprice\n
          soap\t\t10\n
          handwash\t50\n
          cream\t\t50\n
          butter\t40\n
          milk\t\t45
          """)
    print("choice 2 :Remove item from cart")
    print("choice 3 :Display the cart")
    print("choice 4 :Exit")
    print("\n")


    c = int(input("Enter your choice :"))
    print("\n")

    if c == 1 :
        item_name =(input("Enter item name :"))
        Quantity = int(input("Enter Quantity : "))
        price = int(input("Enter price : "))

        T_item =tuple((item_name,Quantity,price))
        shopping_cart.append(T_item)

        print("Total Amount to pay: ")
        amt=0
        for i in shopping_cart:
           amtt= i[1]*i[2]
           amt += amtt

        print(amt)
        print("\n")


        
    elif c == 2:
        item_name = (input("Enter item to remove :"))
        for i in shopping_cart:
            if i[0]==item_name:
                shopping_cart.remove(i)
                print("Item Removed")

        print("Now Total Amount to pay: ")
        
        amt=0
        for item in shopping_cart:
            
               amtt = item[1]*item[2]
               amt+=amtt
        print(amt)
        print("\n")
        

    elif c == 3 :
        for i in shopping_cart:
            print(i)

        amt=0
        for item in shopping_cart:
            
               amtt = item[1]*item[2]
               amt+=amtt

        if amt>=200:
            print("you get 10% Discount")
            print("Total amount to pay :",amt-(0.1*amt))

        elif amt in range (50,200):
            print("you get 5% Discount")
            print("Total amount to pay :",amt-(0.05*amt))

        else:
            print("No Discount")
            print("Total amount to pay :",amt)
        
        print("\n")

    
    else :
        if c!=4:
            print("Enter valid choice\n")

            

    


