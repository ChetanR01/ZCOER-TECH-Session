'''Problem 1: Student Management System
Create a program to manage student information for a class. Implement the following features:
Store student details like name, age, and marks in a dictionary where the key is the student's name and the value is another dictionary with age and marks.
Allow the user to add new students, update details of existing students, and display all student details.
Use if-else conditions to evaluate the student's grade based on their marks and display it (e.g., A, B, C, D, or F).
The program should continue to accept inputs until the user chooses to exit.'''

student = {
    "Raya" : { "age" : 20 , "marks" : 15} ,
    "Riya" : { "age" : 20 , "marks" : 20} ,
    "Rashi" : { "age" : 20 , "marks" : 30} ,
}

#to insert record
records= int(input("enter no of records you want to insert : "))
for i in range(1, records+1):
    stud_name = input("enter name : ")
    stud_age = int(input("enter age : "))
    stud_marks = int(input("enter marks : "))
    student[stud_name] = {"age" : stud_age , "marks" : stud_marks}
    print("record inserted")
print(student.items())

print() #for newline to differentiate functionality
#------------------------------------------------------------------------------


#to update age or marks
stud_update = input("enter the name of student who's record you want to update : ")
update_what = input("update age or marks : ")

if update_what == "age":
    new_age= int(input("enter age : "))
    student[stud_update].update( {"age" : new_age}) #stud_update contains name of stud
    print("age updated")
else :
    new_marks = int(input("enter marks : "))
    student[stud_update ].update(  {"marks" : new_marks})
    print("marks updated")
print("record after updations " , student.items())

print() #for newline to differentiate functionality
#------------------------------------------------------------------------------    


#update grade in dict for each student
for x, y in student.items() :
    m= y.get("marks")
    if m in range(25,31):
        student[x].update( {"grade" : 'A'}) 
    elif m in range (20,26):
         student[x].update( {"grade" : 'B'}) 
    elif m in range (15,21):
         student[x].update({"grade" : 'C'}) 
print("printing records with grades " , student.items())