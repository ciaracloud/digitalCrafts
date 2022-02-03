# This is my code to start a phonebook app

phoneBookEntries = [
  {"name": "joe" ,"phoneNumber": "888-123-1231"},
  {"name": "phil" ,"phoneNumber": "888-123-1231"},
    {"name": "sam" ,"phoneNumber": "888-123-1231"},
  
]
def phoneBook():
   userInput = input("""
   =====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
   """ )
   return userInput

def addEntry():
    userName = input("What is the name of the user?\n")
    userPhoneNumber = input("What is the phone number? Enter in xxx-xxx-xxxx format including the - \n")
    print(f"Created user {userName} with phone number {userPhoneNumber} \n")
    createdUser = {"name": userName,"phoneNumber":userPhoneNumber}
    phoneBookEntries.append(createdUser)


def lookUpEntry():
    whoToFind = input("Who would you like to find?")
    for entry in phoneBookEntries:
            # entry = { "name": "", "phoneNumber": ""}
            if entry["name"] == whoToFind:
                print(f"{entry['name']} : Phone Number: {entry['phoneNumber']}")

def printEveryone():
    for entry in phoneBookEntries:
        print(f"{entry['name']}: phone: {entry['phoneNumber']}")

def deleteEntry():
    if len(phoneBookEntries) == 0:
        print("Looks like no one is in your phone book, try adding someone!")
        return
    else:  
        # how to delete by index
        # count = 0
        # for entry in phoneBookEntries:
        #     print(f"""
        #     {count}. {entry["name"]} : {entry["phoneNumber"]}
        #     """)
        #     count += 1  
       
        # whoToDelete = int(input("Who should we delete? Type in the number on the left of the person to delete."))eeeee
        # personWeAreDeleting = phoneBookEntries[whoToDelete]["name"]
        # one = 1
        # print(f"Deleting user {personWeAreDeleting}")
        # del phoneBookEntries[whoToDelete]
      
        # How to delete by name entered
        # print(phoneBookEntries)
        printEveryone()
        whoToDelete = input("Who would you like to delete?")
        # this statement basically checks to see if the condition at the end. entry["name"] == whoToDelete matches
        # if it finds a name that matches in the list, it will fill userInPhonebook with that value
        # otherwise it will return an empty list
        userInPhonebook = [entry for entry in phoneBookEntries if entry["name"] == whoToDelete]
        
        if len(userInPhonebook) > 0:
            print(f"removed {userInPhonebook[0]['name']}")
            phoneBookEntries.remove(userInPhonebook[0])  
            printEveryone()
        else:
            userDoesNotExist = whoToDelete
            print(f"What are you doing, that {userDoesNotExist} is not in your phonebook.")
            return
            
while True:
    userChoice = phoneBook()
    if userChoice == "1":
        lookUpEntry()
    if userChoice == "2":
        addEntry()
    if userChoice == "3":
        deleteEntry()
    if userChoice == "4":
        printEveryone()
    if userChoice == "5":
        print("Bye.")
        break