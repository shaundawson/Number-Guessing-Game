import random

#Create global constant for number of attempts
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check the user's guess against answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
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
    
    turns = set_difficulty() #global variable
    print(f"You have {turns} attempts remaining to guess a number.")
    
    
    guess = 0 #global variable
    while guess != answer:
        #Ask the user guess a number
        guess = int(input("Make a guess: "))
        #Check the user's guess. Repeat the guessiing functionality if they get it wrong. 
        check_answer(guess,answer)

#Track the number of turns by 1 and reduce by 1 if they get it wrong



game()
