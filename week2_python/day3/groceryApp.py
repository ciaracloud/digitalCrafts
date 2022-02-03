listOfGroceryStores = []

class ShoppingList:
    def __init__(self,title,address,groceryItems=[]):
        self.title = title
        self.address = address
        self.groceryItems = groceryItems
    def displayGroceryStore(self):
        groceryStore = [self.title, self.address]         
        for attribute in groceryStore:
            print(attribute,end=" ")
        print()
    def addItemToList(self,groceryItemName):
        self.groceryItems.append(groceryItemName)
    def displayCompleteGroceryList(self): 
        for groceryItem in self.groceryItems:
            print(self.title)
            groceryItemTotal = groceryItem.quantity * groceryItem.price
            print(f"{groceryItem.title} x {groceryItem.quantity} at ${groceryItem.price} each, which is ${groceryItemTotal}")

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
    print("Here is your current list of grocery stores: ")
    for eachGroceryStore in listOfGroceryStores:
        eachGroceryStore.displayGroceryStore()
    userContinue = input("Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'. ")
    if userContinue == "N":
        break

while True:
    groceryItemName = input("What is the name of the item you need to put on your grocery list? ")
    groceryItemPrice = int(input(f"How much is this {groceryItemName}? "))
    groceryItemQuantity = int(input(f"How many of {groceryItemName} would you like to purchase? "))
    userGroceryStoreChoice = input(f"Which grocery store would you like to add {groceryItemName} to? ")
    groceryItemName = GroceryItem(groceryItemName,groceryItemPrice,groceryItemQuantity)
    storeThatMatches = [store for store in listOfGroceryStores if store.title == userGroceryStoreChoice]
    print(storeThatMatches)
    for eachGroceryStore in listOfGroceryStores:
        if eachGroceryStore.title == userGroceryStoreChoice:
            eachGroceryStore.addItemToList(groceryItemName)
            # eachGroceryStore.displayCompleteGroceryList()
    print(f"Here is your grocery list for {userGroceryStoreChoice}:")
    storeThatMatches[0].displayCompleteGroceryList()
    userContinue = input("Would you like to add another grocery item? If yes, press enter. If no, press 'N'. ")
    if userContinue == "N":
        break

