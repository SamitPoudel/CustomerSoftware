from customer import Customer
import csv

def add_customer(c1):
    print("Adding Customer")
    c1=Customer(id=0, name=" ", phone=0, balance=0, citizenship=0)
    c1.name=input(f"enter customer name:")
    c1.id=input(f"enter customer id:")
    c1.phone=input(f"enter customer phone:")
    c1.balance=input(f"enter customer balance:")
    c1.citizenship=input(f"enter customer citizenship:")
    f=open("customers.csv","a") 
    f.write(f"{c1.name}, {c1.id}, {c1.phone}, {c1.balance}, {c1.citizenship}\n")
    print("data added succesfully")

def view_allcustomers():
    print("view all customer")
    f=open("customers.csv", "r")
    print(f.read())

def veiw_customerwithid():
    print("searching customer with id")
    id = "4"
    all_customers=[]
    with open("customers.csv", "r") as file:
        csv_reader=csv.reader(file)
        for i in csv_reader:
            #print(f"{i} Hello")
            c1=Customer(name=i[0], id=i[1], phone=i[2], balance=i[3], citizenship=i[4])
            all_customers.append(c1)

    ##print(all_customers)
    record_found=False
    customer=Customer(id=0, name="", phone=0, balance=0, citizenship=0)

    for c1 in all_customers:
        print(c1.id == id)
        if c1.id==id:
            record_found=True
            customer=c1
            break
        else:
            record_found=False

    if record_found==True:
        print("record is found")
        customer.display_customer()
    else:
        print("costumer id not found")
        

def delete_customers():
    print("deleting data")


