#library management system
mybook1={
    "title":"TOC",
    "Author":"PAJ",
    "Year":2021,
    "Availability":"A"
}
"""
mybook2={
    "title":"DBMS",
    "Author":"RAP",
    "Year":2020,
    "Availability":"A"
    """

def bupdate():
    if mybook1["Availability"]=="A":
        mybook1.update({"Availability":"NA"})
        print("updated")
        print(mybook1["Availability"])
    else:
        mybook1.update({"Availability":"A"})
        print("updated")
        print(mybook1["Availability"])

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
while(1):
    print("1.Update book info\n2.Add books\n3.Exit")
    n=int(input("enter your choice :"))
    if n==1:
        bupdate()
    elif n==2:
        bookadd()
    else:
        break