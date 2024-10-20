stud_info = {}

temp2 = int(input("Want to insert records ? \n1.YES\n2.NO\n"))
while(temp2==1):
        stud_name= input("Enter the Name Of Student")
        stud_age = int(input(f"Enter the Age of {stud_name}"))
        stud_Marks = int(input(f"Enter the Marks of {stud_name}"))
    
        stud_info.update({stud_name:{"Age":stud_age , "Marks":stud_Marks}})
        
        temp2 = int(input("Do you want to insert another record\n1.YES\n2.NO\n"))
     
print("The Record Inserted Successfully")

temp3 = int(input("Want to Display records ? \n1.YES\n2.NO\n"))
if(temp3==1):
    for i in stud_info:
        print(i,stud_info[i])
else:
    print("Thankyou")
    