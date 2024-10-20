emp_info = {}
def salary_calc(no_hours,wage):
    total_salary = no_hours*wage
    return total_salary
while(True):
        temp2 = int(input("Select Choice:- \n1.Insert Records\n2.Update Records\n3.Display Records\n4.Display_Record_of_perticular_emp\n5.exit"))
        if(temp2 ==1):
            emp_name= input("Enter the Name Of emp:- ")
            emp_Hours_worked= int(input(f"Enter the Number of Hours worked of {emp_name}:- "))
            emp_wage_per_hour = int(input(f"Enter the wage per hours of {emp_name}:- "))
            emp_salary = salary_calc(emp_Hours_worked,emp_wage_per_hour)
            bonus_salary = 0
            bonus_hrs = 0
            if(emp_Hours_worked>40):
                bonus_hrs = emp_Hours_worked - 40
                bonus_salary =   salary_calc(bonus_hrs , emp_wage_per_hour)
            else: 
                bonus_hrs = 0
            
            emp_info.update({emp_name:{"Hours":emp_Hours_worked ,"Wage":emp_wage_per_hour,"Bonus_hrs":bonus_hrs,"Bonus_salary":bonus_salary,"Total_salary_with_bonus":emp_salary}})
        
        elif(temp2 ==2):
            #Update Records 
            
            emp_name= input("Enter The Name Of Emp To Update Records:- ")
            emp_Hours_worked= int(input(f"Enter the Number of Hours worked of {emp_name}:- "))
            emp_wage_per_hour = int(input(f"Enter the wage per hours of {emp_name}:- "))
            emp_salary = salary_calc(emp_Hours_worked,emp_wage_per_hour)
            bonus_salary = 0
            bonus_hrs = 0
            if(emp_Hours_worked>40):
                bonus_hrs = emp_Hours_worked - 40
                bonus_salary =  salary_calc(bonus_hrs , emp_wage_per_hour)
                
            else:
                bonus_hrs = 0
            emp_info.update({emp_name:{"Hours":emp_Hours_worked ,"Wage":emp_wage_per_hour,"Bonus_hrs":bonus_hrs,"Bonus_salary":bonus_salary,"Total_salary_with_bonus":emp_salary}})
           
               
        elif(temp2 == 3):
            #display all the emp rocords
            
            for i in emp_info:
                print(i,emp_info[i])
        
        elif(temp2 == 4):
            #display a single emp records
            
            name = input("Enter The Name Of Emp To Display Records:- ")
            print(name,emp_info[name])
            
        elif(temp2 == 5):
            print("Thankyou For Visit \n"
              "Visit Again !!!")
            break
            
        else:
            print("Invalid Choice")
           