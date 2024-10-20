library={}
def add_book (title, author,year):
    if title in library:
        print(f"Book  {title} already exist in library...")
    else:
        print(f"New Book {title} adding to library")
        library[title]={"Author":author,"Year":year}

while True:
    print("1.Add new book\n2.Display books\n3.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        title=input("Enter book title: ")
        author=input("Enter author name: ")
        year=int(input("Enter book publish year"))
        add_book(title,author,year)
    elif choice==2:
        for title,detail in library.items():
            print(f"Title:{title}, Author:{detail["Author"]}, Year:{detail["Year"]}\n")
    elif choice==3:
        break
    else:
        print("Invalid  choice")