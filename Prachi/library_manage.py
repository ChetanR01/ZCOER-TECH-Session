book={
    
"id1": { "Title": "Harry Potter","Author": "JK Gosling", "Year":2003, "Status":"Borrowed"},
"id2": { "Title": "Wings of Fire","Author": "APJ Abdul Kalam", "Year":2000, "Status":"Borrowed"}

}

while True:
    n=int(input(" 1.Add new book\n 2.Update book availability \n 3.Display all available books \n 4.Search a book \n 5.Exit"))

    if n==5:
        break

    elif n==1:
        id=input("Enter id of book: ")
        title=input("Enter title of book: ")
        author=input("Enter author of book: ")
        year=input("Enter year of book: ")
        status=input("Enter status of book: ")
        book[id]={ "Title" :title,"Author" : author,"Year":year,"Status":status}
        print("Student details added successfully !")

    elif n==2:
        id=input("Enter id of book: ")
        if id in book:
            for x,y in book.items():
                if x==id:
                    status=input("Enter new status of book: ")
                    book[id]={ "Status" :status}
                    print("Book details updated successfully !")
    
    elif n==3:
        if book:
            for x,y in book.items():
                print(f"Id:{x}")
                print(f"Title:{y['Title']}")
                print(f"Author :{y['Author']}")
                print(f"Year:{y['Year']}")
                print(f"Status:{y['Status']}")

    elif n==4:
        id=input("Enter id of book")
        if id in book:
            for x,y in book.items():
                if x==id:
                    print(f"Id:{x}")
                    print(f"Title:{y['Title']}")
                    print(f"Author :{y['Author']}")
                    print(f"Year:{y['Year']}")
                    print(f"Status:{y['Status']}")