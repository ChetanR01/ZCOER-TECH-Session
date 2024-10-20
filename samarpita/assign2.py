'''Problem 2: Shopping Cart

Write a program to simulate a shopping cart system. The program should:
Use a list to store the items added to the cart. Each item is represented by a tuple containing the item name, quantity, and price.
Allow the user to add items to the cart, remove items, and display the current contents of the cart.
After adding items, calculate and display the total price of the cart.
Apply a discount using if-elif conditions:
10% off if the total price is above $100.
5% off if the total price is between $50 and $100.
No discount if the total price is below $50.'''

prod = [] #initially cart empty

#add items
cost = 0
m=int(input("enter no of items : "))

for i in range (m):
    n = input("enter item name: ")
    q = int(input("enter item quantity: "))
    c = int(input("enter item cost: "))
    p =(n , q, c)
    prod.append(p)
    
    cost +=c
    
print() 
print(prod)
print() 

print("total cost of cart ", cost)


print() #for newline to differentiate functionality
#------------------------------------------------------------------------------


#delete item
item = input("enter item name to be deleted : ")
for i in prod : #i is tuple
    for j in i : #j is item in tuples
        if j == item :
           prod.remove(i)
           price = i[2]
           cost-=price
           print("now cart price is ", cost)

print(prod)
 
print() #for newline to differentiate functionality
#------------------------------------------------------------------------------

#discount
if cost >100:
    dis = cost*0.1
    cost-=dis
    print("cost after discount",cost)
elif 50<= cost <=100:
    dis = cost*0.5
    cost-=dis
    print("cost after discount",cost)
elif cost<50:
    print("no discount")