students={}
while True:
    print("****student info system****")
    print("1.add student")
    print("2.update student")
    print("3.display  all students")
    print("4.exit")
    choice=input("enter your choice(1-4): ")
    if choice=='1':
        name=input("enter name:")
        if name in students:
            print("name alreadt exists")
        else:
            age=int(input("enter age:"))
            marks=int(input("enter marks:"))
            students[name]={'age':age,'marks':marks}
            print("student added successfully!")
    elif choice=='2':
        name=input("enter name of student to update:")
        if name not in students:
            print("student does not existe")
        else:
            age=int(input("enter new age:"))
            marks=int(input("enter new marks:"))
            print("student details updated successfully")
    elif choice=='3':
        if not students:
            print("no students found")
        else:
            for name,details in students.items():
                age=details['age']
                marks=details['marks']
            if marks>=90:
                grade='A'
            elif marks>=80:
                grade='B'
            elif marks>=70:
                grade='c'
            elif marks>=60:
                grade='D'
            else:
                grade='F'
            print("students name:",{name})
            print("age:",{age})
            print("marks:",{marks})
            print("grade:",{grade})
    elif choice=='4':
        print("exiting program")
        break
    else:
        print("invalid choice")

