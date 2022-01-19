addresses = []

class user:
    def __init__(self, first_name, last_name):
        self.firstName = firstName
        self.lastName = lastName
    def add_address(self,address):
        addresses = []
        addresses.append(address)

class address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    def display_addresses(self):
        print(addresses)


ciara = user("Ciara", "Cloud")
ciara.add_address("123 happy st.")
print(ciara.add_address)