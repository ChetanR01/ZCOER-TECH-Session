def f_grade(marks):
    if marks >= 80 and marks <= 100:
        return 'A'
    elif marks >= 60 and marks < 80:
        return 'B'
    elif marks >= 40 and marks < 60:
        return 'C'
    else:
        return 'F'

students = {}

while True:
    print("1. Add or Update student info\n2. Display student information\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = int(input("Enter marks out of 100: "))
        grade = f_grade(marks)
        
        if name in students:
            print(f"\nUpdating data for {name}\n")
        else:
            print(f"\nAdding new student {name}\n")
        
        # Add or update the student data in the dictionary
        students[name] = {"age": age, "Marks": marks, "Grade": grade}
    
    elif choice == 2:
        if students:
            for name, details in students.items():
                print(f"Name: {name}, Age: {details['age']}, Marks: {details['Marks']}, Grade: {details['Grade']}\n")
        else:
            print("No student data available.\n")
    
    elif choice == 3:
        break
    
    else:
        print("Invalid option")

