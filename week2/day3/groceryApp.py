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
    def addItemToList(self,groceryItemName):
        self.groceryItems.append(groceryItemName)
    def displayCompleteGroceryList(self): 
        for  store in self.groceryItems:
            print(self.title)
            print(f"{store.title} : price: {store.price} quantity: {store.quantity}")


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

while True:
    groceryItemName = input("What is the name of the item you need to put on your grocery list? ")
    groceryItemPrice = input(f"How much is this {groceryItemName}? ")
    groceryItemQuantity = input(f"How many of {groceryItemName} would you like to purchase? ")
    userGroceryStoreChoice = input(f"Which grocery store would you like to add {groceryItemName} to? ")
    groceryItemName = GroceryItem(groceryItemName,groceryItemPrice,groceryItemQuantity)
    storeThatMatches = [store for store in listOfGroceryStores if store.title == userGroceryStoreChoice]
    print(storeThatMatches)
    for eachGroceryStore in listOfGroceryStores:

        if eachGroceryStore.title == userGroceryStoreChoice:
            print("true")
           
            eachGroceryStore.addItemToList(groceryItemName)
            # eachGroceryStore.displayCompleteGroceryList()
    print(f"Here is your grocery list for {userGroceryStoreChoice}:")
    storeThatMatches[0].displayCompleteGroceryList()
    userContinue = input("\n Would you like to add another grocery item? If yes, press enter. If no, press 'N'. ")
    if userContinue == "N":
        break

# while True:
#     userGroceryItem = input("What item would you like to add to a shopping list? ")
#     userShoppingList = input(f"What list would you like to add {userGroceryItem} to? ")
