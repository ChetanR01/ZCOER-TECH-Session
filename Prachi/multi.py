
def calc_multi(n):
    for i in range(1,11):
        print(f"{n} * {i} =",i*n)

while True:
    num=int(input("Enter the number of which you want multiplication table: "))
    calc_multi(num)
    k=input("Do you want to continue?(y/n)")
    if k=="N" or k=="n":
        break