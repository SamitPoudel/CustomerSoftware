class Customer:
    def __init__(self, name, id, phone, balance,citizenship):
        self.name=name
        self.id=id
        self.phone=phone
        self.balance=balance
        self.citizenship=citizenship

    def display_customer(self):
        print(f"customer name is {self.name}")
        print(f"customer id  is {self.id}")
        print(f"customer phone is {self.phone}")
        print(f"customer balance is {self.balance}")
        print(f"customer citizenship is {self.citizenship}")

##c1=Customer(id="1", name="Samit", phone="12823122", balance="10000", citizenship="12121211")
##print(c1.name)