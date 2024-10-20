def mulgenerator (num,upto=10):
    for i in range(1,upto+1):
        print(f"{num} x {i} = {num*i}")
    print()


while True:
    print("1.Generate a table\n2.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        num=int(input("Enter a number you want to generate a table"))
        mulgenerator(num)
    elif choice==2:
        break
    else:
        print("Invalid choice")
