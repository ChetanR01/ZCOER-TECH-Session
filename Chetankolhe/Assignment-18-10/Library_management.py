Book_info = {}
def available(b_name):
    if(Book_info[b_name]["Status"]=="Available"):
        return True
    else:
        return False
    
    
   
while(True):
        temp2 = int(input("\nSelect Choice:- \n1.Insert Book\n2.Check_availability\n3.Borrow_book\n4.Return_book\n5.Display_All_Books\n6.exit"))
        if(temp2 ==1):
            book_name = input("\nEnter the Name Of emp:- ")
            book_authar= input(f"\nEnter the Author of book {book_name}:- ")
            book_year = int(input(f"\nEnter the year of publish of {book_name}:- "))
            book_status = "Available"
            
            Book_info.update({book_name:{"Author":book_authar ,"Year":book_year,"Status":book_status}})
        
        elif(temp2 == 2):
            name = input("Enter the name of book:- ")
            if name in Book_info:
                if(Book_info[name]["Status"]=="Available"):
                    print("Yes Book is Available\n")
                else:
                    print("No Book is Not Available\n")
            else:
                print("Book Not In Stock\n")
                
        elif(temp2==3):
            name1 = input("Enter the name of book to be borrow :- ")
            if(available(name1) == True):
                print("Book Aloted Succesfully")
                Book_info[name1]["Status"] = "Not Available"
            else:
                print("Sorry Book Not Available \nTry again After Some Time !!!")
                
                
        elif(temp2 == 4):
            name1 = input("Enter the name of book to be Return :- ")
            if(available(name1) != True):
                print("Book return Sucessfully")
                Book_info[name1]["Status"] = "Available"
            else:
                print("Book Not Borrowed\n"
                      "First Borrow the And Then return it !!!")
                
        elif(temp2==5):
            
             for i in Book_info:
                print(i,Book_info[i])
                
            
                
                
        elif(temp2 == 6):
            print("Thankyou For Visit \n"
            "Visit Again !!!")
            break
        else:
            print("Invalid Choice")
            
