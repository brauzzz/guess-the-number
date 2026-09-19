logo = r"""
Welcome to...
  ___  _  _  ____  ____  ____    ____  _  _  ____    __ _  _  _  _  _  ____  ____  ____  _   
 ╱ __)╱ )( ╲(  __)╱ ___)╱ ___)  (_  _)╱ )( ╲(  __)  (  ( ╲╱ )( ╲( ╲╱ )(  _ ╲(  __)(  _ ╲╱ ╲  
( (_ ╲) ╲╱ ( ) _) ╲___ ╲╲___ ╲    )(  ) __ ( ) _)   ╱    ╱) ╲╱ (╱ ╲╱ ╲ ) _ ( ) _)  )   ╱╲_╱  
 ╲___╱╲____╱(____)(____╱(____╱   (__) ╲_)(_╱(____)  ╲_)__)╲____╱╲_)(_╱(____╱(____)(__╲_)(_)  
"""
import random
def find_number():
    number = random.randint(1, 100)
    return number

def evaluate(number, guess, lives):
    if guess > number:
        lives -= 1
        print("Too high.")
        return lives
    elif guess < number:
        lives -= 1
        print("Too low.")
        return lives

def gtn():
    number = find_number()
    lives = 0
    game_over = False
    while game_over == False:
        print(logo)
        print("Im thinking of a number between 1 and 100.")
        #print("Psst... The number is " + str(number))
        difficulty = input("Choose your difficulty. Type 'easy' or 'hard':\n ").lower()
        if difficulty == "easy":
            lives = 10
        elif difficulty == "hard":
            lives = 5
        else:
            print("Invalid difficulty. Type 'easy' or 'hard'.")
            game_over = True
        while lives > 0 and game_over == False:
            guess = int(input("Guess a number: \n"))
            if guess == number:
                game_over = True
                print("You win! The number was " + str(number))
            else:
                lives = evaluate(number, guess, lives)
                print("You have " + str(lives) + " lives left.")
                if lives == 0:
                    game_over = True
                    print(f"You lose! The number was {number}!")

play_first = input("Would you like to play Guess the Number? (y/n) \n").lower()
if play_first == "y":
    print("\n"*100)
    gtn()
elif play_first == "n":
    exit()
play = True
while play:
    play_again = input("Would you like to play Guess the Number again? (y/n) \n").lower()
    if play_again == "y":
        print("\n"*100)
        gtn()
    elif play_again == "n":
        play = False