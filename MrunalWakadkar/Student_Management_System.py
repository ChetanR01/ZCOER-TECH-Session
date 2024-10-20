Details ={"sita":{"age":20 ,"marks":90} , "gita":{"age":19 ,"marks":75} , "mita":{"age":22 , "marks":88},"tina":{"age":16 ,"marks":65} ,"nita":{"age":19 ,"marks":85}
          }
def Addentry():
    name1=input("Enter name of the student : ")
    age=int(input("Enter age :"))
    marks=int(input("Enter marks :"))
    Details[name1]={age,marks}

def updateentry():
    name2=input("Enter name of the student which you want to update  : ")
    age=int(input("Enter updated age :"))
    marks=int(input("Enter updated marks :"))
    Details.update({name2:{age,marks}})        
def display():
    for i in Details.values():
        print(i)
        if i["marks"] >=90:
            print("A")
        elif i["marks"] >=80 and i["marks"]<=90:
            print("B")
        elif i["marks"] >=70 and i["marks"]<=80:
            print("C")
        elif i["marks"] >=60 and i["marks"]<=70:
            print("D")
        else:
            Details.update["Grade"]="F"
while True:
    print("1. To add entry :")
    print("2. Uodate the entry:")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        Addentry()
    elif ch==2:
        updateentry()
    elif ch==3:
        display()
    elif ch==4:
        exit()

    else:
        print("Invalid choice ")
    

    





