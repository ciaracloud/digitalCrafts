class Character:
    def __init__(self, letter, health, strength, confidence = 0):
        self.letter = letter
        self.health = health
        self.strength = strength
        self.confidence = confidence

def display_character_a_stats():
    print("""CURRENT STATS FOR CHARACTER A
====================================================================
HEALTH: {a.health}
STRENGTH: {a.strength}
CONFIDENCE: {a.confidence}
""")

def display_character_b_stats():
    print("""CURRENT STATS FOR CHARACTER B
====================================================================
HEALTH: {b.health}
STRENGTH: {b.strength}
CONFIDENCE: {b.confidence}
""")

def display_character_c_stats():
    print("""CURRENT STATS FOR CHARACTER C
====================================================================
HEALTH: {c.health}
STRENGTH: {c.strength}
CONFIDENCE: {c.confidence}
""")

a = Character("A", 400, 50, 0)
b = Character("B", 200, 100, 0)
c = Character("C", 500, 30, 0)
vivian = Character("Vivian", 400, 50, 60)

line_one = input("Today is the day! You are headed to an interview for your dream job as an interior designer! (Press enter to continue)")
line_two = input("But wait .... You see Vivian (the girl who has been mean to you since 5th grade)! (Press enter to continue)")
line_three = input("She is definitely going to try to stop you from making it to the interview by attempting to defeat you in a battle! (Press enter to continue)")
line_four = input("If you can get past her, you can make it make it to the interview! (Press enter to continue)")
vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
name_or_run_choice = input("""Vivian: "HEY YOU! What's your name again?" 
-Type your name to give her your name 
OR 
-Press 1 to point at a "squirrel" and run past her: """).capitalize()
while len(name_or_run_choice) > -1:
    if len(name_or_run_choice) > 0 and name_or_run_choice != "1":
        print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
        must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
        character_letter = input("""                                      CHARACTER MENU 
============================================================================================
            CHARACTER A                CHARACTER B                 CHARACTER C
            health: 400                health: 200                 health: 500
            strength: 50               strength: 100               strength: 30
            confidence: 0              confidence: 0               confidence: 0

Type the letter of the character you would like to be during battle here (A, B, or C): """).upper()
        while len(character_letter) > -1:
            if character_letter == "A" or character_letter == "B" or character_letter == "C":
                line_seven = input(f"You have chosen to be CHARACTER {character_letter}! (Press enter to continue)")
                break
            else:
                print("Please choose one of the characters that are available in the character menu!")
                character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()
        break
    elif name_or_run_choice == "1":
        line_eight = input('It worked! Vivian got distracted looking for the "squirrel" that you pointed at and you ran past her! (Press enter to continue)')
        line_nine = input("You made it to the interview, but you didn't get the job. (Press enter to continue)")
        line_ten =input("Maybe next time you see Vivian you should try to win the battle against her to gain some confidence before your interview! (Press enter to continue)")
        line_ten = input("...It's the next day and you are on your way to another interview you have set up for your dream job as an interior designer! (Press enter to continue)")
        line_eleven = input("Oh no ..it's Vivian again! (Press enter to continue)")
        vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
        name_or_run_choice = input("""Vivian: "HEY YOU! What's your name again?"
Type your name here to give her your name: """).capitalize()
        while len(name_or_run_choice) > -1:
            if len(name_or_run_choice) > 0:
                print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
                must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
                character_letter = input("""                                      CHARACTER MENU 
============================================================================================
            CHARACTER A                CHARACTER B                 CHARACTER C
            health: 400                health: 200                 health: 500
            strength: 50               strength: 100               strength: 30
            confidence: 0              confidence: 0               confidence: 0

Type the letter of the character you would like to be during battle here (A, B, or C): """).upper()
                while len(character_letter) > -1:
                    if character_letter == "A" or character_letter == "B" or character_letter == "C":
                        line_seven = input(f"You have chosen to be CHARACTER {character_letter}! (Press enter to continue)")
                        break
                    else:
                        print("Please choose one of the characters that are available in the character menu!")
                        character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()
                break
    else:
        name_or_run_choice = input('Please type your name OR press 1 to point at a "squirrel" and run past Vivian: ')
    break
# display_current_character_stats()
        


