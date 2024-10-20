def print_table():
    for j in range(1,11):
        for i in range(1,11):
            print(j*i)
        print("----------")

def generate_table(num1):
    for m in range(1,11):
        print(num1,"*" ,m ,"=" , num1*m) 
    



while True:
    print("1. Print table 1-10")
    print("2. Generate table ")
    print("3. Exit")
    ch =int(input("Enter your choice:"))
    if ch==1:
        print_table()
    
    elif ch==2:
        num = int(input("Enter a number :"))
        generate_table(num)
    elif ch==3:
        exit()
    else:
        print("Invalid")
    
