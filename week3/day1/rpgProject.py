line_one = input("Today is the day! You are headed to an interview for your dream job as an interior designer! (Press enter to continue)")
line_two = input("But wait .... You see Vivian (the girl who has been mean to you since 5th grade)! (Press enter to continue)")
line_three = input("She is definitely going to try to stop you from making it to the interview by attempting to defeat you in a battle! (Press enter to continue)")
line_four = input("If you can get past her, you can make it make it to the interview! (Press enter to continue)")
line_five = input("As you approach Vivian, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
character_letter = input("""                                      CHARACTER MENU 
============================================================================================
            CHARACTER A                CHARACTER B                 CHARACTER C
            health: 400                health: 200                 health: 500
            strength: 50               strength: 100               strength: 30

Type the letter of the character you would like to be during battle here: """).upper()
while len(character_letter) == 1:
    if character_letter == "A" or character_letter == "B" or character_letter == "C":
        print(f"You have chosen to be CHARACTER {character_letter}! Let's continue!")
    else:
        print("Please choose one of the characters that are available in the character menu!")
        character_letter = input("Type the letter of the character you would like to be during battle here: ").upper()