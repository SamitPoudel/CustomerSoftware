from customer import Customer
import controller as c1

option_text=""""
What do you want to do?
1. Add customer
2.View all customer
3.View Customers by id
4.Update Customers
5.Delete Customers
"""
option = int(input(option_text))

if option==1:
    c1.add_customer(c1)
elif option==2:
    c1.view_allcustomers()
elif option==3:
    print("view all customer by id")
elif option==4:
    print("update customer")
elif option==5:
    print("delete customer")
else:
    print("invalid option")



