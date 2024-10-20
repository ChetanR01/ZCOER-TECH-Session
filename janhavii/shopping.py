cart=[]
while True:
    print("****shopping cart menu****")
    print("1.add item")
    print("2.remove item")
    print("3.view item")
    print("4.calculate")
    print("5.exit")
    choice=input("enter your choice (1-5):")
    if choice=='1':
        item_name=input("enter item name:")
        quant=int(input("enter item quantity:"))
        price=float(input("enter item price:"))
        cart.append((item_name,quant,price))
        print("item added successfull!")
    elif choice=='2':
        if not cart:
            print("cart is already empty")
        else:
            item_name=input("enter name of item to be removed")
            #found=False
            for item in cart:
                if item[0]==item_name:
                    cart.remove(item)
                    #found=True
                    print("item removed")
                    break
            if item not in cart:
                print("item is not in cart")
    elif choice == '3':
        if not cart:
            print("Your cart is empty.")
        else:
            print("---Current Cart Items---")
            for item in cart:
                print("Item:",item[0],"Quantity:",item[1],"Price:",item[2])
    

    elif choice=='4':
        if not cart:
            print("cart s empty")
        else:
            total_price=0
            print("---Checkout---1")
            for items in cart:
                item_total=item[1]*item[2]
                total_price+=item_total
                print("Item:",item[0],"Quantity:",item[1]," Subtotal:" ,item_total)
            if total_price>100:
                discount=0.10
                print("10% discount!")
            elif 50<=total_price<=100:
                discount=0.05
                print("5% discount!")
            else:
                discount=0.00
                print("no discount")
            discount_amount=total_price*discount
            final_price=total_price-discount_amount
            print("\nTotal price before discount:" ,total_price)
            print("Discount:",discount_amount)
            print("Final price after discount:",final_price)
    elif choice=='5':
        print("program exiting")
        break
    else:
        print("invalid choice")
        