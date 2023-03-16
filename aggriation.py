class Customer:
    def __init__(self,name, gender, address):
        self.name = name
        self.gender = gender
        self.address  = address

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.new_name = new_name
        self.address.change_address(new_city,new_pin,new_state)



class Address:
    def __init__(self,city,pincode,state):
        self.city  = city
        self.pincode = pincode
        self.state= state

    def change_address(self,new_city,new_pincode,new_state):
        self.new_city = new_city
        self.new_pincode = new_pincode
        self.new_state = new_state



add = Address('noida',2323,'up')
cust = Customer('ashish','male',add)
print(cust.address.city)

cust.edit_profile('ashish','delhi',2313,'delhi')

print(cust.address.pincode)
