class User:
    def __init__(self, first_name, last_name, address, address2):
        self.firstName = first_name
        self.lastName = last_name
        self.address = address
        self.address2 = address2

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    def display_address(self):
        address = [self.street, self.city, self.state, self.zip_code]
        for element in address:
            print(element,end=" ")
        print()
    
ciarasAddress2 = Address("456 Sad St.", "St.Louis", "MO", "12345")
ciarasAddress = Address("123 Happy St.", "Tampa", "FL", "12345")
ciara = User("Ciara", "Cloud", ciarasAddress, ciarasAddress2)
ciarasAddress.display_address()
ciarasAddress2.display_address()