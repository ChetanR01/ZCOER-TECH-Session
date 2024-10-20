
def generate_table(num,upto=10):
    
    for i in range(1,upto+1):
        print(f"{num} * {i} = {num*i}")


c=1
while c!=0 :
     
    print("***Multiplication Table***\n")
    num =int(input("Enter the number : "))
    generate_table(num)

    print("-"*10)

    c = int(input("Do you want to Continue?(0/1)"))


    
def table_1to10() :
    for i in range (1,11):
        for j in range(1,11):
            print(f"{i} * {j} = {j*i}")
        print("-"*13)  

table_1to10()            

def table2_1to10():

    for i in range(1,11):
        print(f"{1}*{i}={1*i}\t{2}*{i}={2*i}\t{3}*{i}={3*i}\t{4}*{i}={4*i}\t{5}*{i}={5*i}\t{6}*{i}={6*i}\t{7}*{i}={7*i}\t{8}*{i}={8*i}\t{9}*{i}={9*i}\t{10}*{i}={10*i}")

table2_1to10()