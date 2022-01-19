# Introduction to classes
#  Factory that produces at scale
#  A base that you can build on top of 

soybean = {
    "furColor": "black/tan",
    "cutenessLevel": 10,
    "tailLength": "9 in",
    "furLength": "4 in",
    "name": "Soybean",
    "breed": "German Shepherd",
    "image": "https://bit.ly/3FKhMPH"
}

mooncake = {
    "furColor": "white/tan",
    "cutenessLevel": 10,
    "tailLength": "6 in",
    "furLength": "3 in",
    "name": "Mooncake",
    "breed": "Corgi",
    "image": "https://bit.ly/3IjVgyN"
}
#  We run into the problem that we have to create more objects if we have more data
#  Is there a better way to create a base to start at??
puppy = {
    "breed": "",
    "name": "",
    "size":""
}

def eatFood(food):
    print(f"I am eating {food}")

eatFood("hotdog")
#  Classes fit that description and help you create a base/skeleton for a complex dictionary
#  Defining a class
listForStuff = ["howdy"]
listForStuff.append("howdyhowdyhowdy")

class Puppy:
    #  This is the fundamental qualities of your class
    def __init__(self,name,size,breed,happiness=50):
        self.name = name
        self.size = size
        self.breed = breed
        self.happiness = happiness
    # define a function inside of a class, it is called a method
    def giveTreat(self):
        self.happiness = self.happiness * 2
    def bark(self):
        print("woof woof")


luna = Puppy("luna","med","labrador")
mooncake = Puppy("mooncake", "small", "Corgi")
cosmo = Puppy("Cosmo","huge","Mutt")
print(cosmo.happiness)
cosmo.giveTreat()
print(cosmo.happiness)
cosmo.bark()

class ToyPuppy(Puppy):
    def __init__(self,name,breed,size="1ft",happiness=5, portability="very"):
        super().__init__(name,size,breed,happiness)
        self.portability = portability

    def bark(self):
        print("yap yap")

# jellybean = ToyPuppy("Jellybean", "toy","Chihuahua",10)
# jellybean.bark()
# print(jellybean.happiness)
# jellybean.giveTreat()
# print(jellybean.happiness)
# print(vars(cosmo))
# print(vars(jellybean))
# dot notation
# Act of using a class attribute and referencing it with the period (. )
# print(luna.name)
# print(mooncake.name)
# print(cosmo.name)

class User:
    def __init__(self,name,email,password,address=""):
         self.name = name
         self.email = email
         self.password = password
         self.address = address
    def printAccountDetails(self):
        print(f"{self.name}, {self.email}, {self.password}")

class SuperUser(User):
    def __init__(self,name,email,password,accessPriviledge):
        super().__init__(name,email,password)
        self.accessPriviledge = accessPriviledge
    def printAdminStatus(self):
        print(f"You have {self.accessPriviledge} status")

class UltraUser(SuperUser):
    def showAwesomeDogPhotos(self):
        print("I have dogs")
    pass

class Address:
    def __init__(self,street,zip,city,state):
        self.street = street
        self.zip = zip
        self.city = city
        self.state = state


# Creating an instance of a class
joe = User("Joe","email@email.com","123123")
joe.printAccountDetails()
#  Classes can inherit from another class
Jarrod = SuperUser("Jarrod","j@j.com","passw0rd","Admin")
Jarrod.printAccountDetails()
Jarrod.printAdminStatus()
# Classes can inherit classes that inherited classes
liz = UltraUser("Liz", "secret@secret.com","secr3t","Ultra")
liz.printAdminStatus()
liz.printAccountDetails()
liz.showAwesomeDogPhotos()
# Attaching a class value to a variable and using it in another class
heathersHome = Address("mystic stone", "32323", "Atlanta", "GA")
heather = User("heather", "1@1", "secretpassword",heathersHome)
print(heather.address.street)
