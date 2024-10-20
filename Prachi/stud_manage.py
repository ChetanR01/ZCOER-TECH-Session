

students = {
  "Prachi" : {
    "age" : 20,
    "marks" : 80
  },
  "Shruti" : {
    "age" : 20,
    "marks" : 70
  },
  "Gauri" : {
    "age" : 20,
    "marks" : 90
  }
}
def grades(marks):
    if marks>=90:
        return "A"  
    elif marks>=80:
        return "B"  
    elif marks>=70:
        return "C"  
    elif marks>=60:
        return "D"  
    else:
        return "F"    
    
while True:

    i=int(input("Enter : 1.Add new students\n\t2.Update details of existing students \n\t3.Display all student details\n\t4.Exit"))

    if i==3:
        if students:
            for x,y in students.items():
                print(f"Name:{x}")
                print(f"Age:{y['age']}")
                print(f"Marks:{y['marks']}")
                grade=grades(y['marks'])
                print(f"Grade:{grade}")

    elif i==1:
        name=input("Enter name of student: ")
        age=int(input("Enter age of student: "))
        marks=float(input("Enter marks of student: "))
        students[name]={ "age" : age,"marks" : marks}
        print("Student details added successfully !")
        
    elif i==2:
        name=input("Enter name of student: ")
        if name in students:
            age=int(input("Enter new age of student: "))
            marks=float(input("Enter new marks of student: "))
            students[name]={ "age" : age,"marks" : marks}
            print("Student details updated successfully !")

    elif i==4:
        break
