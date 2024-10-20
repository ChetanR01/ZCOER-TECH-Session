def calculate_pay(hours, wage):
 
  if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * wage * 1.5
    regular_pay = 40 * wage
    total_pay = regular_pay + overtime_pay
  else:
    total_pay = hours * wage
  return total_pay

def add_employee(employees):
  name = input("Enter employee name: ")
  hours_worked = float(input("Enter hours worked: "))
  hourly_wage = float(input("Enter hourly wage: "))
  employees[name] = {"hours": hours_worked, "wage": hourly_wage}

def update_employee(employees):
  name = input("Enter employee name to update: ")
  if name in employees:
    hours_worked = float(input("Enter new hours worked: "))
    hourly_wage = float(input("Enter new hourly wage: "))
    employees[name]["hours"] = hours_worked
    employees[name]["wage"] = hourly_wage
  else:
    print("Employee not found.")

employees = {}
while True:
    print("\nEmployee Payroll System")
    print("1. Add employee")
    print("2. Update employee")
    print("3. Calculate payroll")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      add_employee(employees)
    elif choice == 2:
      update_employee(employees)
    elif choice == 3:
      total_payroll = 0
      for name, employee in employees.items():
        hours = employee["hours"]
        wage = employee["wage"]
        pay = calculate_pay(hours, wage)
        total_payroll += pay
        print(f"{name}: ${pay}")
      print(f"Total payroll: ${total_payroll}")
    elif choice == 4:
      break
    else:
      print("Invalid choice. Please try again.")
    
    