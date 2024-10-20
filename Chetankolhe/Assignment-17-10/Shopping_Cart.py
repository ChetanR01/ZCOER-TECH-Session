cart =[]
print(cart)
temp3 =0 
while True:
    temp2 = int(input("Select Choice :- \n1.Add_to_cart\n2.Delete_From_cart\n3.Display_cart\n4.exit\n"))
    if(temp2==1):    
        item_tuple=()
        temp_list = list(item_tuple)
        
        #cart item id
        temp_list.append(temp3)
       
        #cart item name
        item_name=input("Enter the item name:- ")
        temp_list.append(item_name) 
        
        #cart item quantity
        item_quantity = int(input("Enter the Item quantity:- "))
        temp_list.append(item_quantity)
        
        #cart item price
        item_price = int(input("Enter the price of item:- ")) 
        temp_list.append(item_price) 
        
        #converting list to tuple
        new_tuple = tuple(temp_list)
        #adding the tuple to the main cart list
        cart.append(new_tuple)
        temp3=temp3+1
          
    elif(temp2==2):
        #taking user input of cart item id to delete only the required element
        itm_index = int(input("Enter the Cart_item_id:- "))
        #poping the whole tuple from the cart list
        cart.pop(itm_index)
        
    elif(temp2==3):
        #just Displaying the cart items here
        print(cart)
        
    elif(temp2==4):
        print("Thankyou For Adding Items In Our Cart \n"
              "Visit Again !!!")
        break
    
    else:
        print("Enter The Valid Number :(")
        