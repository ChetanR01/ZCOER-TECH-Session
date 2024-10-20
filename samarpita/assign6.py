'''Problem 3: Multiplication Table Generator

Write a program that generates multiplication tables. The program should:
Ask the user for a number and display its multiplication table up to 10 using a for loop.
Use nested loops to generate tables for numbers from 1 to 10.
Implement a function generate_table(number, upto) that prints the multiplication table for a given number.
Allow the user to generate multiple tables until they choose to exit.'''

def generate_table() :
    num = int (input("enter number : "))
    upto = int(input("multiply upto number ? "))
    for i in range(1,upto+1) :
        print(f"{num} *",i ,"=", num * i)
    
flag = 1    
while flag :
    generate_table()
    
    cont = input("do you wanna continue : ")
    if cont == 'y' or cont == 'Y' :
        flag = 1
    else :
        flag = 0    
        
        