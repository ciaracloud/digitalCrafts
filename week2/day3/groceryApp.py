listOfGroceryStores = []

class ShoppingList:
    def __init__(self,title,address):
        self.title = title
        self.address = address
    def displayGroceryStore(self):
        groceryStore = [self.title, self.address]         
        for attribute in groceryStore:
            print(attribute,end=" ")

class GroceryItem:
    def __init__(self,title,price,quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

while True:
    groceryStoreName = input("What is the name of the grocery store you want to add? ")
    groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
    groceryStoreName = ShoppingList(groceryStoreName,groceryStoreAddress)
    listOfGroceryStores.append(groceryStoreName)
    print("Here is your list of grocery stores:")
    for eachGroceryStore in listOfGroceryStores:
        eachGroceryStore.displayGroceryStore()
    userContinue = input("\n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'. ")
    if userContinue == "N":
        break

# while True:
#     userGroceryItem = input("What item would you like to add to a shopping list? ")
#     userShoppingList = input(f"What list would you like to add {userGroceryItem} to? ")

# ShoppingList(groceryStoreName,groceryStoreAddress)