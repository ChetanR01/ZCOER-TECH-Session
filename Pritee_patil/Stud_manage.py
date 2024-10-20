'''
Problem Statement:
Create a program to manage student information for a class. Implement the following features:
Store student details like name, age, and marks in a dictionary where the key is the student’s name and the value is another dictionary with age and marks.
Allow the user to add new students, update details of existing students, and display all student details.
Use if-else conditions to evaluate the student's grade based on their marks and display it (e.g., A, B, C, D, or F).
The program should continue to accept inputs until the user chooses to exit.
'''
ClassTEC = {
    "student1": {"name": "Pritee", "age": 21, "marks": 70},
    "student2": {"name": "Mayuri", "age": 20, "marks": 69}
}

while True:
    # Display menu options
    print("\nMenu")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        student_id = f"student{len(ClassTEC) + 1}" #mostly we use f-string for taking input
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        marks = int(input("Enter student's marks: "))

        # Add new student to dictionary
        ClassTEC[student_id] = {"name": name, "age": age, "marks": marks}
        print(f"{name} has been added as {student_id}.")
      
    elif choice == '2':  # Update Student
        student_id = input("Enter the student ID to update (e.g., student1): ")
        if student_id in ClassTEC:

            name = input("Enter the new name (or press Enter to keep it unchanged): ")
            age_input = input("Enter the new age (or press Enter to keep it unchanged): ")
            marks_input = input("Enter the new marks (or press Enter to keep it unchanged): ")
            
            if name:
                ClassTEC[student_id]["name"] = name
            if age_input:
                ClassTEC[student_id]["age"] = int(age_input)
            if marks_input:
                ClassTEC[student_id]["marks"] = int(marks_input)
                
            print(f"{student_id} has been updated.")
        else:
            print("Student ID not found.")
    
    elif choice == '3':  # Display Students
        print("\nClassTEC Students:")
        for student_id, details in ClassTEC.items():
            print(f"{student_id}: Name: {details['name']}, Age: {details['age']}, Marks: {details['marks']}")
    
    elif choice == '4':  # Exit
        print("Exiting the program.")
        break  # Exit the loop and end the program
    
    else:
        print("Invalid choice. Please try again.")

# Optional: Print the final state of ClassTEC
print("Final ClassTEC:", ClassTEC)
