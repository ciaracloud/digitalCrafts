#this is my code to start a phonebook app

def lookUpEntry():
    print("Let's look up an entry!")
    userLookUp = input("Who do you want to look up? ")
    for entry in phonebook:
            if entry["name"] == userLookUp:
                print(f"The phone number for {entry['name']} is {entry['phone']}.")

def addEntry():
    print("Let's add an entry!")
    name = input("What is the name? ")
    phone = input("What is the phone number? Please enter phone number in this format: xxx-xxx-xxxx. ")
    entry = {"name": name, "phone": phone}
    phonebook.append(entry) 
    print(f"Created entry for {name.capitalize()} with the phone number {phone}. \n This is the updated phonebook: \n {phonebook}.")

def deleteEntry():
    print("Let's delete an entry!")
    userDelete = input("What user would you like to delete? ")
    userInPhonebook = [entry for entry in phonebook if entry["name"] == userDelete]
    if len(phonebook) == 0:
        print("Looks like no one is in your phone book, try adding someone!")
        return
    else:   
        print(f"\n This is the current phonebook: \n {phonebook}.")

        if len(phonebook) > 0:
            print(f"removed {userInPhonebook[0]['name']}")
            phonebook.remove(userInPhonebook[0])  
            print(f"Deleted the entry for {userDelete} from the phonebook. \n This is the updated phonebook: \n {phonebook}")
        else:
            userDoesNotExist = userDelete
            print(f"{userDoesNotExist} is not in your phonebook. Try typing a name that is already in your phonebook.")

def printPhonebookNice():
    counter = 0
    for entry in phonebook:
        print(f"{counter}. {entry['name']}: {entry['phone']}")
        counter += 1

def listAllEntries():
    print("Here's a list of all entries in the phonebook currently:")
    printPhonebookNice()

phonebook = [
    {"name": "Jocelynn", "phone": "123-456-7890"}, {"name": "Ciara", "phone": "904-123-7899"}, {"name": "Taylor", "phone": "222-222-2222"}
]

print("This is the current phonebook:")
printPhonebookNice()

while True:
    userInput = (input("\nElectronic Phone Book \n ==================== \n 1. Look up an entry \n 2. Add an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit \n What do you want to do (1-5)? "))
    if userInput == "1":
        lookUpEntry()
    elif userInput == "2":
        addEntry()
    elif userInput == "3":
        deleteEntry()    
    elif userInput == "4":
        listAllEntries()
    elif userInput == "5":
        print("Bye.")
        break

#QUESTION TO ASK:
#1. Don't completely understand this: 'userInPhonebook = [entry for entry in phoneBookEntries if entry["name"] == whoToDelete]'



    