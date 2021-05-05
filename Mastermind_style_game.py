game = "play"
print("Welcome to a Mastermind style game, created by Emma. Since you only have three colours to guess, this is easier than the real thing!")
print("""
The rules are simple. You will need a pen and paper to track your results as the programmer currently isn't smart enough to 
display your progress, tell you how many times you . You can choose from the colours, but cannot repeat any in the sequence:
RED, ORANGE, YELLOW, GREEN, BLUE, PINK, PURPLE, WHITE, BLACK, GREY, SILVER, GOLD, BROWN
""")

start = input("Are you ready to play?").lower
if start == ("no"):
    print("See you again soon!")
    exit(1)
guesses = 0
chosen_colours = 0
# valid = "red" or "orange" or "yellow" or "blue" or "green" or "pink" or "silver" or "gold" or "brown" or "purple" or "black" or "white" or "grey"
valid_colours = ["red", "orange", "yellow", "blue","green","pink", "silver", "gold", "brown", "purple", "black", "white"]
print("Player 1, please choose three colours")
while True:
    while game == "play":
        choice_1 = input("Colour 1: ").lower()
        choice_2 = input("Colour 2: ").lower()
        choice_3 = input("Colour 3: ").lower()
        chosen_colours = [choice_1, choice_2, choice_3]
        if choice_1 == choice_2 or choice_3 == choice_1 or choice_2 == choice_3:
            print("Sorry, please choose three different colours!")
        while choice_1 in valid_colours and choice_2 in valid_colours and choice_3 in valid_colours:
            # print("Sorry, this is not a valid choice")
            game = "player 2"
            break
        else:
            print("Sorry, this is not a valid choice")

    while guesses != chosen_colours:
        print("Player 2, please guess the sequence colours")
        guess_1st_col = input("Colour 1: ").lower()
        guess_2nd_col = input("Colour 2: ").lower()
        guess_3rd_col = input("Colour 3: ").lower()
        guesses = [guess_1st_col, guess_2nd_col, guess_3rd_col]

        if guesses == chosen_colours:
            print("Congratulations, you guessed correctly!")
            guess_total = f"Guesses: {attempts}"
            print(guess_total)
        elif choice_1 in guesses:
            if guess_1st_col == choice_1:
                if guess_2nd_col == choice_2:
                    print("Colour 1: CORRECT, Colour 2: CORRECT, Colour 3: Incorrect")
                elif guess_2nd_col == choice_3:
                    if guess_3rd_col == choice_2:
                        print("Colour 1: Correct, Colour 2: in sequence but in wrong place, Colour 3: in sequence but in wrong place")
                    else:
                        print("Colour 1: CORRECT, Colour 2: is in the sequence but in the wrong place, Colour 3: Incorrect")
                elif guess_2nd_col != choice_2 and guess_3rd_col == choice_3:
                    print("Colour 1: Correct, Colour 2: Incorrect, Colour 3: Correct")
                elif guess_2nd_col != choice_2 and guess_3rd_col == choice_2:
                    print("Colour 1: Correct, Colour 2: Incorrect, Colour 3: is in the sequence but in the wrong place")
                else:
                    print("Colour 1: CORRECT, Colour 2: Incorrect, Colour 3: Incorrect")
            elif guess_1st_col == choice_2 or guess_1st_col == choice_3:
                if guess_2nd_col == choice_2:
                    if guess_3rd_col == choice_2 or guess_3rd_col == choice_1:
                        print("Colours 1 and 3 are in the wrong places. Colour 2: CORRECT")
                    else:
                        print("Colour 1: In the wrong place, Colour 2: Correct, Colour 3: Incorrect")
                elif guess_2nd_col == choice_3 or guess_2nd_col == choice_1:
                    if guess_3rd_col == choice_3:
                        print("Colours 1 and 2 are in the wrong places, Colour 3: CORRECT")
                    elif guess_3rd_col != choice_2 or guess_3rd_col != choice_1:
                        print("Colours 1 and 2 are in the wrong places, Colour 3: Incorrect")
                    elif guess_3rd_col == choice_3:
                        print("Correct colours, but in the wrong places!")
                elif guess_2nd_col != choice_1 and guess_2nd_col != choice_3:
                    if guess_3rd_col == choice_3:
                        print("Colour 1 is in the wrong place, Colour 2: Incorrect. Colour 3: CORRECT")
                    elif guess_3rd_col == choice_1 or guess_3rd_col == choice_2:
                        print("Colour 1 is in the wrong place, Colour 2: Incorrect, Colour 3: In wrong place")
                    else:
                        print("Colour 1: In wrong place, Colour 2: Incorrect, Colour 3: Incorrect")
        elif guess_1st_col != choice_1 or choice_2 or choice_3:
            if guess_2nd_col == choice_2:
                if guess_3rd_col == choice_3:
                    print("Colour 1: Incorrect, Colour 2: CORRECT, Colour 3: CORRECT")
                elif guess_3rd_col == choice_1:
                    print("Colour 1: Incorrect, Colour 2: CORRECT, Colour 3: in sequence but not in the correct place.")
                else:
                    print("Colour 1: Incorrect, Colour 2: CORRECT, Colour 3: Incorrect")
            elif guess_2nd_col != choice_2:
                if guess_3rd_col == choice_3:
                    print("Colour 1: Incorrect, Colour 2: Incorrect, Colour 3: CORRECT")
                elif guess_3rd_col == choice_1 or guess_3rd_col == choice_2:
                    print("Colour 2: Incorrect, Colour 2: Incorrect, Colour 3: In sequence but not in the correct place.")
                else:
                    print("All colours are incorrect, please try again")
            elif guess_2nd_col == choice_3 or guess_2nd_col == choice_1:
                if guess_3rd_col == choice_3:
                    print("Colour 1: Incorrect, Colour 2 is in wrong place, Colour 3: CORRECT")
                elif guess_3rd_col != choice_2 or guess_3rd_col != choice_1:
                    print("Colour 1: Incorrect, Colour 2 is in wrong place, Colour 3: Incorrect")
                elif guess_3rd_col == choice_1 or guess_3rd_col == choice_2:
                    print("Colour 1: Incorrect, Colour 2 is in wrong place, Colour 3 is in wrong place")

        play_again = input("Would you like to play again? ").lower
        if play_again == "No":
            break
        print("Please try again")
        attempts = 1
        while play_again != "No" and guesses != chosen_colours:
            attempts += 1
            print("Guess count:", {attempts})
            break






