
emp_data = {
            "Rudrali":{"hours":50,"hourly_wage":350},
            "Anushka":{"hours":56,"hourly_wage":350},
            "Tanishka":{"hours":47,"hourly_wage":350},
            "Raksha":{"hours":30,"hourly_wage":350}
            }
            

def calculate_pay(hours,wage):
    total_pay = hours*wage
    return total_pay

c=0
while c!=5:
    print("Menu:")
    print("choice 1 :Update existing employee data")
    print("choice 2 :Add new employee dta")
    print("choice 3 :Display employee data and pay roll")
    print("choice 4 :check overtime")
    print("choice 5 :Exit")
    print("\n")


    c = int(input("Enter your choice : "))
    print("\n")

    if c == 1 :
        key = (input("Enter the name of Employee to upadate data :"))
        key = key.capitalize()
        hrs = int(input("Enter work hours : "))
        

        

        emp_data[key]["hours"]=hrs
        
        print("\n")
       
    elif c == 2:
        key = (input("Enter the name of employee :"))
        key = key.capitalize()
        hrs = int(input("Enter work hours : "))
        wage = int(input("Enter hourly wage : "))

        emp_data.update({key:{"hours":hrs,"wage":wage}})
        print("\n")

        

    elif c == 3 :
        for i,j in emp_data.items():
            print(i,j)
            amt =calculate_pay(j["hours"],j["hourly_wage"])
            print(f"{i}'s pay roll = {amt}")

        print("\n")

    elif c == 4 :

        for i,j in emp_data.items():
            if j["hours"]>40 :
                print(f"{i} get bonus of 1500 rupees\nTotal Pay = {calculate_pay(j["hours"],j["hourly_wage"])+1500}")

            else :
                print(f"{i} get no bonus\nTotal Pay = {calculate_pay(j["hours"],j["hourly_wage"])}")



    else :
        if c!=5:
            print("Enter valid choice\n")

            

    


