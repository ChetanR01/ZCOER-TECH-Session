#library management system
mybook1={
    "TOC": {
        "title":"TOC",
        "Author":"PAJ",
        "Year":2021,
        "Availability":"A"
    },
    "DBMS": {
        "title":"DBMS",
        "Author":"RAP",
        "Year":2020,
        "Availability":"A"

    }
}

def bupdate():
    bname=str(input("enter book name to update:"))
    for i in mybook1: #iterating the dictionary
        if bname in mybook1: 
            print("1.Title\n2.Author\n3.Year\n4.Availability")
            ch=int(input("what do you want to update:"))
            if ch==1:
                ttl=str(input("enter updated title:"))
                mybook1[bname]["title"]=ttl
                print("Book title updated succesfully to:",mybook1[bname]["title"])
            elif ch==2:
                athr=str(input("enter updated author:"))
                mybook1[bname]["Author"]=athr
                print("book author updated succesfully to:",mybook1[bname]["Author"])
            elif ch==3:
                yr=int(input("enter updated year:"))
                mybook1[bname]["Year"]=yr
                print("book author updated succesfully to:",mybook1[bname]["Year"])
            else:
                if[bname]["Availabilty"]=="A":
                    [bname]["Availabilty"]="NA"
                else:
                    [bname]["Availabilty"]="A"
        else:
            print("book does not exist")
        break


def bookadd():
    b=str(input("enter title of book:"))
    c=str(input("enter author name:"))
    d=str(input("enter publish year:"))
    e=str(input("enter availability:"))
    mybook1["title"]=b
    mybook1["Author"]=c
    mybook1["Year"]=d
    mybook1["Availability"]=e
    print("book added succesfully")

def bookdisplay():
    for x,y in mybook1.items():
        print(x)
        print(y)
    
while(1):
    print("1.Update book info\n2.Add books\n3.Display books\n4.exit")
    n=int(input("enter your choice :"))
    if n==1:
        bupdate()
    elif n==2:
        bookadd()
    elif n==3:
        bookdisplay()
    else:
        break
    