character_list = []
import random
class Character:
    def __init__(self, letter, health, strength, confidence = 0):
        self.letter = letter
        self.health = health
        self.strength = strength
        self.confidence = confidence
    def display_current_stats(self):
        print(f"""
              CURRENT STATS FOR CHARACTER {self.letter}
====================================================================
HEALTH: {self.health}
STRENGTH: {self.strength}
CONFIDENCE: {self.confidence}
""")

def display_character_menu():
    print("""                                      
                                      CHARACTER MENU 
============================================================================================
            CHARACTER A                CHARACTER B                 CHARACTER C
            health: 300                health: 100                 health: 400
            strength: 50               strength: 100               strength: 30
            confidence: 0              confidence: 0               confidence: 0

""")

def display_character_a_stats():
    a.display_current_stats()

def display_character_b_stats():
    b.display_current_stats()

def display_character_c_stats():
    c.display_current_stats()

def display_vivian_stats():
    vivian.display_current_stats()

def display_attack_options_a():
    print("""               
            CHARACTER A ATTACK OPTIONS
======================================================
A. Throw your shoe at Vivian
B. Tickle Vivian
C. Sing the song that Vivian hates as loud as you can
""")

def display_attack_options_b():
    print("""               
             CHARACTER B ATTACK OPTIONS
======================================================
A. Run your finger nails down a chalkboard
B. Throw your shoe at Vivian
C. Pinch Vivian as hard as you can
""")

def display_attack_options_c():
    print("""               
            CHARACTER C ATTACK OPTIONS
======================================================
A. Flick Vivian as hard as you can
B. Tickle Vivian
C. Challenge Vivian to a mini dance battle
""")

a = Character("A", 300, 50, 0)
b = Character("B", 100, 100, 0)
c = Character("C", 400, 30, 0)
vivian = Character("VIVIAN", 300, 40, 60)

line_one = input("Today is the day! You are headed to an interview for your dream job as an interior designer! (Press enter to continue)")
line_two = input("But wait .... You see Vivian (the girl who has been mean to you since 5th grade)! (Press enter to continue)")
line_three = input("She is definitely going to try to stop you from making it to the interview by attempting to defeat you in a battle! (Press enter to continue)")
line_four = input("If you can get past her, you can make it make it to the interview! (Press enter to continue)")
vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
name_or_run_choice = input("""Vivian: "HEY YOU! What's your name again?" 
-Type your name to give her your name 
OR 
-Press 1 to point at a "squirrel" and run past her: """).upper()
while len(name_or_run_choice) > -1:
    if len(name_or_run_choice) > 0 and name_or_run_choice != "1":
        print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
        must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
        display_character_menu()
        character_letter = input("Type the letter of the character you would like to be during battle here (A, B, or C): ").upper()
        while len(character_letter) > -1:
            if character_letter == "A":
                display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                display_character_a_stats()
                user_continue = input("(Press enter to continue)")
                break
            elif character_letter == "B":
                display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                display_character_b_stats()
                user_continue = input("(Press enter to continue)")
                break
            elif character_letter == "C": 
                display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                display_character_c_stats()
                user_continue = input("(Press enter to continue)")
                break
            else:
                print("Please choose one of the characters that are available in the character menu!")
                character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()
        break
    elif name_or_run_choice == "1":
        line_five = input('It worked! Vivian got distracted looking for the "squirrel" that you pointed at and you ran past her! (Press enter to continue)')
        line_six = input("You made it to the interview, but you didn't get the job. (Press enter to continue)")
        line_seven =input("Maybe next time you see Vivian you should try to win the battle against her to gain some confidence before your interview! (Press enter to continue)")
        line_eight = input("...It's the next day and you are on your way to another interview you have set up for your dream job as an interior designer! (Press enter to continue)")
        line_nine = input("Oh no ..it's Vivian again! (Press enter to continue)")
        vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
        name_or_run_choice = input("""Vivian: "HEY YOU! What's your name again?"
Type your name here to give her your name: """).upper()
        while len(name_or_run_choice) > -1:
            if len(name_or_run_choice) > 0:
                print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
                must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
                display_character_menu()
                character_letter = input("Type the letter of the character you would like to be during battle here (A, B, or C): ").upper()
                while len(character_letter) > -1:
                    if character_letter == "A":
                        display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                        display_character_a_stats()
                        user_continue = input("(Press enter to continue)")
                        break
                    elif character_letter == "B":
                        display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                        display_character_b_stats()
                        user_continue = input("(Press enter to continue)")
                        break
                    elif character_letter == "C": 
                        display_character_letter = input(f"You have chosen to be CHARACTER {character_letter}! (To see their stats press enter)")
                        display_character_c_stats()
                        user_continue = input("(Press enter to continue)")
                        break
                    else:
                        print("Please choose one of the characters that are available in the character menu!")
                        character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()
                break
    else:
        name_or_run_choice = input('Please type your name OR press 1 to point at a "squirrel" and run past Vivian: ')
    break
     
# line_ten = input("""Anytime you would like to see your current stats during battle, press 0, otherwise press enter to continue the battle.
# Now let's begin! (Press enter to continue)""")
# if line_ten == 0 and character_letter == "A":
#     display_character_a_stats()
# elif line_ten == 0 and chararcter_letter == "B":
#     display_character_b_stats()
# elif line_ten == 0 and character_letter == "C":
#     display_character_c_stats()

vivians_attacks = ["Vivian unleashed her pet fire ant on you! OUCH! You lost 40 health points", 
"Vivian hit you with her purse and some of her change flew out! You lost 40 health points",
"Vivian does the one karate move that she knows on you! You lost 40 points"]

print("""
It's time for battle! You attack first!
""")
if character_letter == "A":
    while vivian.health > 0 or a.health > 0:
        print("These are the attack options that you can use against Vivian:")
        display_attack_options_a()
        user_attack_choice = input("How would you like to attack Vivian? Choose A, B, or C: ").upper()
        if user_attack_choice == "A":
            a.health -= 50
            vivian.health -= 10
            attack_a_continue = input(f"""
You threw your shoe at Vivian! She caught your shoe and threw it back at you!\nYou lost 50 health points and Vivian lost 10 health points!

YOUR CURRENT HEALTH: {a.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "B":
            vivian.health -= 50
            attack_b_continue = input(f"""
You have decided to tickle Vivian! She HATES being tickled! She lost 50 health points!

YOUR CURRENT HEALTH: {a.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        elif user_attack_choice == "C":
            vivian.health -= 50
            attack_c_continue = input(f"""
You sang the song that Vivian hates as loud as you can! She lost 50 health points!

YOUR CURRENT HEALTH: {a.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
        else: 
            display_attack_options_a()
            user_attack_choice = input("Please choose an attack option from the attack menu").upper()
        a.health -= 40
        vivians_random_attack = random.choice(vivians_attacks)
        print(vivians_random_attack)
        vivians_attack_continue = input(f"""
YOUR CURRENT HEALTH: {a.health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)
""")
elif character_letter == "B":
    while vivian.health > 0 or b.health > 0:
        print("These are the attack options that you can use against Vivian:")
        display_attack_options_b()
        break
elif character_letter == "C":
    while vivian.health > 0 or c.health > 0:
        print("These are the attack options that you can use against Vivian:")
        display_attack_options_c()
        break