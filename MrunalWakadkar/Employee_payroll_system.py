employee={"Mrunal":{"Hwork":4 ,"Hwage":50}, "OM":{"Hwork":2,"Hwage":30} , "guddi":{"Hwork":5 ,"Hwage":70}}
def calculate_payroll():
    for i , j in employee.items():
        total_pay=j["Hwork"] * j["Hwage"]
        print(f"Total pay  for {i} :{total_pay}")

def Addentry():
    name1=input("Enter name of the employee : ")
    hw=int(input("Enter work hours :"))
    hwage=int(input("Enter work wage  :"))
    employee[name1]={hw,hwage}

def updateentry():
    name2=input("Enter name of the employee which you want to update  : ")
    hw=int(input("Enter updated   work hour  :"))
    hwage=int(input("Enter updated work wage  :"))
    employee.update({name2:{hw,hwage}})      


while True:
    print("1. To add entry :")
    print("2. Update the entry:")
    print("3. Calculate pay roll")
    print("4. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        Addentry()
    elif ch==2:
        updateentry()
    elif ch==3:
        calculate_payroll()
    elif ch==4:
        exit()

    else:
        print("Invalid choice ")
    
calculate_payroll()