'''Problem 3: Multiplication Table Generator
Write a program that generates multiplication tables. The program should:
Ask the user for a number and display its multiplication table up to 10 using a for loop.
Use nested loops to generate tables for numbers from 1 to 10.
Implement a function generate_table(number, upto) that prints the multiplication table for a given number.
Allow the user to generate multiple tables until they choose to exit.'''
def main():
    while True:
        user_input = input("Enter a number to generate its multiplication table (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("bye!")
            break
        
        # Check if the input is a valid number
        if user_input.isdigit():
            number = int(user_input)

            # Print multiplication table for the user's number
            print(f"\nMultiplication Table for {number}:")
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")

            # Nested loop to print multiplication tables from 1 to 10
            print("\nMultiplication Tables from 1 to 10:")
            for j in range(1, 11):  # Outer loop for the base number
                print(f"\nMultiplication Table for {j}:")
                for i in range(1, 11):  # Inner loop for the multiplier
                    print(f"{j} x {i} = {j * i}")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
