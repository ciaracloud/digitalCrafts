#"Normal way of creating a class:
class Groceries:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
    def getPrice(self):
        self.price *= self.quantity
        print(self.price)
    def printGroceryList(self):
        print(f"You have purchased {self.quantity} {self.item} for ${self.price}")
johnList = Groceries('cereal', 1, 3.00)
print(vars(johnList))#how it looks 'normally'
#--------------------------------------------
#the class constructor below is one that accepts unlimited parameters:
class Groceries2:
    def __init__(self, *args):
        for idx, item in enumerate(args):
            setattr(self, "attr{}".format(idx), item)
janList = Groceries2('peach 1 1.00', 'apple 1 2.00') #this puts the entire string in one attribute, however, this may cause problems with applying a function
joeList = Groceries2('melon', 1, 1.00, 'strawberry', 2, 2.00) #this puts each individual piece of information in its own attribute....maybe we could manipulate it
print(vars(janList))
print(vars(joeList))