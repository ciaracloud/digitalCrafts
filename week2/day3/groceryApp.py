listOfGroceryStores = []

class ShoppingList:
    def __init__(self,title,address):
        self.title = title
        self.address = address
    def displayGroceryStore(self):
        groceryStore = [self.title, self.address]         
        for attribute in groceryStore:
            print(attribute,end=" ")

#attempt #1
# class ShoppingList:
#     def __init__(self,title,address):
#         self.title = title
#         self.address = address
#     def displayListOfGroceryStores(self):
#         groceryStores = [self.title, self.address]
#         for eachGroceryStore in listOfGroceryStores:           
#             for attribute in groceryStores:
#                 print(attribute,end=" ")

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
        groceryStoreName.displayGroceryStore()
    userContinue = input("\n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'. ")
    if userContinue == "N":
        break

#test #5
# while True:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     groceryStoreTitle = input(f"What would you like to store {groceryStoreName} as? ")
#     groceryStoreTitle = ShoppingList(groceryStoreName,groceryStoreAddress)
#     # listOfGroceryStores.append(groceryStore)
#     listOfGroceryStores.append(groceryStoreTitle)
#     print("Here is your list of grocery stores:")
#     for eachGroceryStore in listOfGroceryStores:
#         groceryStoreTitle.displayGroceryStore()
#     userContinue = input("\n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

#test #4
# while True:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     groceryStoreTitle = input(f"What would you like to store {groceryStoreName} as? ")
#     groceryStoreTitle = ShoppingList(groceryStoreName,groceryStoreAddress)
#     # listOfGroceryStores.append(groceryStore)
#     listOfGroceryStores.append(groceryStoreTitle)
#     print("Here is your list of grocery stores:")
#     groceryStoreTitle.displayListOfGroceryStores()
#     userContinue = input("\n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

#test 3
# groceryStoreName = input("What is the name of the grocery store you want to add? ")
# groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
# groceryStoreTitle = input(f"What would you like to write {groceryStoreName} down as on the list? ")
# groceryStoreTitle = ShoppingList(groceryStoreName,groceryStoreAddress)
# listOfGroceryStores.append(groceryStoreTitle)

# for eachGroceryStore in listOfGroceryStores:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     groceryStoreTitle = input(f"What would you like to write {groceryStoreName} down as on the list? ")
#     groceryStoreTitle = ShoppingList(groceryStoreName,groceryStoreAddress)
#     # listOfGroceryStores.append(groceryStore)
#     listOfGroceryStores.append(groceryStoreTitle)
#     print("Here is your list of grocery stores:")
#     groceryStoreTitle.displayListOfGroceryStores()
#     userContinue = input("Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

#test 3
# while True:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     groceryStoreTitle = input(f"What would you like to write {groceryStoreName} down as on the list? ")
#     groceryStoreTitle = ShoppingList(groceryStoreName,groceryStoreAddress)
#     # listOfGroceryStores.append(groceryStore)
#     listOfGroceryStores.append(groceryStoreTitle)
#     print("Here is your list of grocery stores:")
#     groceryStoreTitle.displayListOfGroceryStores()
#     userContinue = input("Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

#test 2
# while True:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     groceryStore = {"title": groceryStoreName, "address": groceryStoreAddress}
#     groceryStore["title"] = groceryStoreName
#     groceryStore["address"] = groceryStoreAddress
#     listOfGroceryStores.append(groceryStoreName)
#     listOfGroceryStores.append(ShoppingList(groceryStoreName,groceryStoreAddress))
#     userContinue = input(f"Here is your list of grocery stores so far: {listOfGroceryStores} \n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

#test 1
# while True:
#     groceryStoreName = input("What is the name of the grocery store you want to add? ")
#     groceryStoreAddress = input(f"What is the address of {groceryStoreName}? ")
#     listOfGroceryStores.append(ShoppingList(groceryStoreName,groceryStoreAddress))
#     userContinue = input(f"Here is your list of grocery stores so far: {listOfGroceryStores} \n Would you like to add another grocery store to your list? If yes, press enter. If no, press 'N'.")
#     if userContinue == "N":
#         break

# while True:
#     userGroceryItem = input("What item would you like to add to a shopping list? ")
#     userShoppingList = input(f"What list would you like to add {userGroceryItem} to? ")

# ShoppingList(groceryStoreName,groceryStoreAddress)