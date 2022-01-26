import random

def display_character_menu():
    print("""                                      
                                      CHARACTER MENU 
============================================================================================
                 A                          B                           C
            name: KIWI                 name: MANGO                 name: GUAVA
            health: 300                health: 100                 health: 300
            strength: 50               strength: 100               strength: 40
            confidence: 0              confidence: 0               confidence: 0

""")

class Character:
    def __init__(self, name, letter, health, strength, confidence, attack_a, attack_b, attack_c):
        self.name = name
        self.letter = letter
        self.health = health
        self.strength = strength
        self.confidence = confidence
        self.attack_a = attack_a
        self.attack_b = attack_b
        self.attack_c = attack_c
    def display_current_stats(self):
        print(f"""
                   CURRENT STATS FOR {self.name}
====================================================================
HEALTH: {self.health}
STRENGTH: {self.strength}
CONFIDENCE: {self.confidence}
""")
    def display_attack_options(self):
        print(f"""
                  ATTACK OPTIONS FOR {self.name}
====================================================================
A. {self.attack_a}
B. {self.attack_b}
C. {self.attack_c}
""")

kiwi = Character("KIWI", "A", 300, 50, 0, "Throw your shoe at Vivian", "Tickle Vivian", "Sing the song that Vivian hates as loud as you can")
mango = Character("MANGO", "B", 100, 100, 0, "Run your fingernails down a chalkboard", "Throw your shoe at Vivian", "Pinch Vivian as hard as you can")
guava = Character("GUAVA", "C", 300, 40, 0, "Flick Vivian as hard as you can", "Tickle Vivian", "Challenge Vivian to a mini dance battle")
vivian = Character("VIVIAN", "D", 300, 40, 60, "", "", "")

character_list = [kiwi,mango,guava]

line_one = input("Today is the day! You are headed to an interview for your dream job as an interior designer! (Press enter to continue)")
line_two = input("But wait .... You see Vivian (the girl who has been mean to you since 5th grade)! (Press enter to continue)")
line_three = input("She is definitely going to try to stop you from making it to the interview by attempting to defeat you in a battle! (Press enter to continue)")
line_four = input("If you can get past her, you can make it make it to the interview! (Press enter to continue)")
vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
name_or_run_choice = input("""
                  Vivian: "HEY YOU! What's your name again?" 
                    Type your name to give her your name                 
                                     OR                 
press 1 to point at a "squirrel" and run past her (Press enter to continue): """).upper()
while len(name_or_run_choice) > -1:
    if len(name_or_run_choice) > 0 and name_or_run_choice != "1":
        print_name = input(f"""You: "Come on, Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
        must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
        display_character_menu()
        character_letter = input("Type the letter of the character you would like to be during battle here (A, B, or C): ").upper()
        while len(character_letter) > -1:
            matching_character_letter = [character_class for character_class in character_list if character_class.letter == character_letter]
            if character_letter == "A" or character_letter == "B" or character_letter == "C":
                display_character_letter = input(f"You have chosen to be {matching_character_letter[0].name} during battle! (Press enter to see their stats)")
                matching_character_letter[0].display_current_stats()
                user_continue = input("(Press enter to continue)")
                break
            else:
                print("PLEASE CHOOSE ONE OF THE CHARACTERS THAT ARE AVAILABLE IN THE CHARACTER MENU:")
                display_character_menu()
                character_letter = input("Type the letter of the character you would like to be during battle here (A,B,or C): ").upper()
        break
    elif name_or_run_choice == "1":
        line_five = input('It worked! Vivian got distracted looking for the "squirrel" that you pointed at and you ran past her! (Press enter to continue)')
        line_six = input("You made it to the interview, but you didn't get the job. (Press enter to continue)")
        line_seven =input("Maybe next time you see Vivian you should try to win the battle against her to gain some confidence before your interview! (Press enter to continue)")
        line_eight = input("...It's the next day and you are on your way to another interview you have set up for your dream job as an interior designer! (Press enter to continue)")
        line_nine = input("Oh no ..it's Vivian again! (Press enter to continue)")
        vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
        name_or_run_choice = input("""
                     Vivian: "HEY YOU! What's your name again?"
        Type your name here to give her your name (Press enter to continue): """).upper()
        while len(name_or_run_choice) > -1:
            if len(name_or_run_choice) > 0:
                print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
                must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
                display_character_menu()
                character_letter = input("Type the letter of the character you would like to be during battle here (A, B, or C): ").upper()
                while len(character_letter) > -1:
                    matching_character_letter = [character_class for character_class in character_list if character_class.letter == character_letter]
                    if character_letter == "A" or character_letter == "B" or character_letter == "C":
                        display_character_letter = input(f"You have chosen to be {matching_character_letter[0].name} during battle! (Press enter to see their stats)")
                        matching_character_letter[0].display_current_stats()
                        user_continue = input("(Press enter to continue)")
                        break
                    else:
                        print("Please choose one of the characters that are available in the character menu!")
                        display_character_menu()
                        character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()
                break
    else:
        name_or_run_choice = input('Please type your name OR press 1 to point at a "squirrel" and run past Vivian: ')
    break

battle_begins = input(f"""
Random person on the street: "It's time for battle! {matching_character_letter[0].name} ATTACKS FIRST!" 
(Press enter to continue)
""")

vivians_attacks = [">> Vivian unleashed her pet fire ant on you! OUCH! You lost 40 health points! <<", 
">> Vivian hit you with her purse! WHY IS HER PURSE SO HARD?! You lost 40 health points! <<",
">> Vivian does the one karate move that she knows on you! You lost 40 health points! <<"]

if character_letter == "A":
    while vivian.health > 0 or kiwi.health > 0:
        if vivian.health <= 0 or kiwi.health <= 0:
            if vivian.health > kiwi.health:
                print("GAME OVER! Vivian won!")
                break
            elif kiwi.health > vivian.health:
                kiwi.confidence += 1000
                print(f"YAY! You won and your confidence is now at {kiwi.confidence}! Now get to that job interview!")
                break
        print("These are the attack options that you can use against Vivian:")
        matching_character_letter[0].display_attack_options()
        user_attack_choice = input("How would you like to attack Vivian? Choose A, B, or C: ").upper()
        if user_attack_choice == "A":
            kiwi.health -= 40
            vivian.health -= 30
            attack_a_continue = input(f"""
** You threw your shoe at Vivian! She caught your shoe and threw it back at you!\nYou lost 50 health points and Vivian lost 40 health points! **

YOUR CURRENT HEALTH: {kiwi.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "B":
            vivian.health -= 50
            attack_b_continue = input(f"""
** You tickled Vivian! She HATES being tickled! She lost 50 health points! **

YOUR CURRENT HEALTH: {kiwi.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "C":
            vivian.health -= 50
            attack_c_continue = input(f"""
** You sang the song that Vivian hates as loud as you can! She lost 50 health points! **

YOUR CURRENT HEALTH: {kiwi.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        else: 
            matching_character_letter[0].display_attack_options()
            user_attack_choice = input("Please choose an attack option from the attack menu (A,B,or C):").upper()
        if vivian.health <= 0 or kiwi.health <= 0:
            if vivian.health > kiwi.health:
                print("GAME OVER! Vivian won!")
                break
            elif kiwi.health > vivian.health:
                kiwi.confidence += 1000
                print(f"YAY! You won and your confidence is now at {kiwi.confidence}! Now get to that job interview!")
                break
        kiwi.health -= 40
        vivians_random_attack = random.choice(vivians_attacks)
        print(vivians_random_attack)
        vivians_attack_continue = input(f"""
YOUR CURRENT HEALTH: {kiwi.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
if character_letter == "B":
    while vivian.health > 0 or mango.health > 0:
        if vivian.health <= 0 or mango.health <= 0:
            if vivian.health > mango.health:
                print("GAME OVER! Vivian won!")
                break
            elif mango.health > vivian.health:
                mango.confidence += 1000
                print(f"YAY! You won and your confidence is now at {mango.confidence}! Now get to that job interview!")
                break
        print("These are the attack options that you can use against Vivian:")
        matching_character_letter[0].display_attack_options()
        user_attack_choice = input("How would you like to attack Vivian? Choose A, B, or C: ").upper()
        if user_attack_choice == "A":
            vivian.health -= 100
            attack_a_continue = input(f"""
** You ran your fingernails down a chalkboard! Vivian hates that sound!! She lost 100 points! **

YOUR CURRENT HEALTH: {mango.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "B":
            mango.health -= 30
            vivian.health -= 70
            attack_b_continue = input(f"""
** You threw your shoe at Vivian! She caught your shoe and threw it back at you!\nYou lost 30 health points and Vivian lost 70 health points! **

YOUR CURRENT HEALTH: {mango.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "C":
            vivian.health -= 100
            attack_c_continue = input(f"""
** You pinched Vivian as hard as you can! She lost 100 health points! **

YOUR CURRENT HEALTH: {mango.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        else: 
            matching_character_letter[0].display_attack_options()
            user_attack_choice = input("Please choose an attack option from the attack menu (A,B,or C):").upper()
        if vivian.health <= 0 or mango.health <= 0:
            if vivian.health > b.health:
                print("GAME OVER! Vivian won!")
                break
            elif mango.health > vivian.health:
                mango.confidence += 1000
                print(f"YAY! You won and your confidence is now at {b.confidence}! Now get to that job interview!")
                break
        mango.health -= 40
        vivians_random_attack = random.choice(vivians_attacks)
        print(vivians_random_attack)
        vivians_attack_continue = input(f"""
YOUR CURRENT HEALTH: {mango.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
if character_letter == "C":
    while vivian.health > 0 or guava.health > 0:
        if vivian.health <= 0 or guava.health <= 0:
            if vivian.health > guava.health:
                print("GAME OVER! Vivian won!")
                break
            elif guava.health > vivian.health:
                guava.confidence += 1000
                print(f"YAY! You won and your confidence is now at {guava.confidence}! Now get to that job interview!")
                break
        print("These are the attack options that you can use against Vivian:")
        matching_character_letter[0].display_attack_options()
        user_attack_choice = input("How would you like to attack Vivian? Choose A, B, or C: ").upper()
        if user_attack_choice == "A":
            vivian.health -= 40
            attack_a_continue = input(f"""
** You flicked Vivian as hard as you can! She lost lost 40 health points! **

YOUR CURRENT HEALTH: {guava.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "B":
            vivian.health -= 40
            attack_b_continue = input(f"""
** You tickled Vivian! She HATES being tickled! She lost 40 health points! **

YOUR CURRENT HEALTH: {guava.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "C":
            guava.health -= 10
            vivian.health -= 30
            attack_c_continue = input(f"""
** You challenged Vivian to a mini dance battle! She's got some moves, but she isn't nearly as good as you!
You lost 10 health points! Vivian lost 30 health points! **

YOUR CURRENT HEALTH: {guava.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        else: 
            matching_character_letter[0].display_attack_options()
            user_attack_choice = input("Please choose an attack option from the attack menu (A,B,or C):").upper()
        if vivian.health <= 0 or guava.health <= 0:
            if vivian.health > guava.health:
                print("GAME OVER! Vivian won!")
                break
            elif guava.health > vivian.health:
                guava.confidence += 1000
                print(f"YAY! You won and your confidence is now at {guava.confidence}! Now get to that job interview!")
                break
        guava.health -= 40
        vivians_random_attack = random.choice(vivians_attacks)
        print(vivians_random_attack)
        vivians_attack_continue = input(f"""
YOUR CURRENT HEALTH: {guava.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")