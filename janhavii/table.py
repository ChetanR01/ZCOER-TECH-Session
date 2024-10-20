def generate_table(number, upto):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")
    print()
def generate_table_1to10():
    for number in range(1, 11):
        generate_table(number, 10)
def main():
    while True:
        print("1. table for a number")
        print("2. tables for numbers 1 to 10")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                number = int(input("Enter a number to print its table: "))
                generate_table(number, 10)
            except ValueError:
                print("Invalid input!")       
        elif choice == '2':
            generate_table_1to10()              
        else:
            print("Invalid choice!")
main()