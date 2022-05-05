import random

#Create global constant for number of attempts
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


turns = 0 
#Function to check the user's guess against answer. Track the number of turns and reduce by 1 if wrong
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else: 
        print(f"You got it! The answer was {answer}.")

#Function to set difficulty
def set_difficulty():
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    if level == "easy":
        return EASY_LEVEL_TURNS 
    else: 
        return HARD_LEVEL_TURNS

def game():
    #Choose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I\'m thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Psst, the correct answer is {answer}")
    
    turns = set_difficulty() #set number of turns
    
    #Repeat the guessiing functionality if they get it wrong.
    guess = 0 #global variable
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess a number.")
        #Ask the user guess a number
        guess = int(input("Make a guess: "))
        #Check the user's guess. 
        turns = check_answer(guess,answer,turns) #This is the number of turns remaining. It updates the local variable on line 36 everytime the answer is checked

game()
