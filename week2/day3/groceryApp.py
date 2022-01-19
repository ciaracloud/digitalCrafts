# listOfGroceryStores = []

while True:
    groceryStoreName = input("What is the name of the grocery store you want to add? ")
    groceryStoreAddress = input("What is the address of the grocery store you want to add? ")
    userContinue = input("Would you like to continue? If no, press N.")
    if userContinue == "N":
        break



# while True:
#     userGroceryItem = input("What item would you like to add to a shopping list? ")
#     userShoppingList = input(f"What list would you like to add {userGroceryItem} to? ")


# class ShoppingList:
#     def __init__(self,title,address):
#         self.title = title
#         self.address = address

# class GroceryItem:
#     def __init__(self,title,price,quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity


# walmart = ShoppingList(groceryStoreName,groceryStoreAddress)