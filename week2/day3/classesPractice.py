addresses = []

class User:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
    def add_address(self,address):
        addresses = []
        addresses.append(address)

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    def display_addresses(self):
        print(addresses)


ciara = user("Ciara", "Cloud")
ciara.add_address("123 happy st.")
print(f"adding this address: {ciara.add_address} to the addresses list.")