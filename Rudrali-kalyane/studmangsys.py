
student_data = {"Rudrali":{"age":18,"marks":90},
                "Anushka":{"age":19,"marks":90},
                "Tanishka":{"age":17,"marks":80},
                "Raksha":{"age":16,"marks":70}}
c=0
while c!=5:
    print("Menu:")
    print("choice 1 :Update existing student data")
    print("choice 2 :Add new student data")
    print("choice 3 :Display student data")
    print("choice 4 :Show students grade")
    print("choice 5 :Exit")
    print("\n")

    c = int(input("Enter your choice : "))
    print("\n")

    if c == 1 :
        key = (input("Enter the name of student to upadate data :"))
        key = key.capitalize()
        age = int(input("Enter new age : "))
        marks = int(input("Enter new marks : "))

        

        student_data[key]["age"]=age
        student_data[key]["marks"]=marks
        print("\n")
        # print(student_data)

    elif c == 2:
        key = (input("Enter the name of student :"))
        key = key.capitalize()
        age = int(input("Enter age : "))
        marks = int(input("Enter  marks : "))

        student_data.update({key:{"age":age,"marks":marks}})
        print("\n")

        # print(student_data)

    elif c == 3 :
        for i,j in student_data.items():
            print(i,j)

        print("\n")

    elif c == 4 :

        for name in student_data.keys():
            if (student_data[name]["marks"] >=90):
                print(f"Name :{name} , Grade :A")

            elif (student_data[name]["marks"]<90 and 70>=student_data[name]["marks"]):
                print(f"Name :{name} , Grade :B")

            elif (student_data[name]["marks"]<70 and 50>=student_data[name]["marks"]):
                print(f"Name :{name} , Grade :C")
            
            elif (student_data[name]["marks"]<50 and 40>=student_data[name]["marks"]):
                print(f"Name :{name} , Grade :D")

            else:
                print(f"Name :{name} , Grade :F")

            print("\n")

    else :
        if c!=5:
            print("Enter valid choice\n")

            

    


