import random

num = random.randint(1,100)
easy_attempts = 10
hard_attempts = 5

print(num)

print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")

game_level = input('Choose a difficulty. Type "easy" or "hard": ')
play_game = True

def decrease_easy_attempts():
    return easy_attempts - 1

def decrease_hard_attempts():
    return hard_attempts - 1

def guess_checker():
    guess = int(input("Make a guess: "))
    if guess == num:
        print("Winner Winner chicken dinner")
    elif guess < num:
        print("Too low.\nGuess again.") 
    elif guess > num:
        print("Too high.\nGuess again")


while game_level == "hard":
    if hard_attempts > 0:
        print(f"You have {hard_attempts} attempts remaining to guess the number.")
        attempts = decrease_hard_attempts()
        guess_checker()

    hard_attempts = decrease_hard_attempts()
        

while game_level == "easy":  
    print(f"You have {easy_attempts} attempts remaining to guess the number.")
    attempts = decrease_easy_attempts()
    guess_checker()
    
    easy_attempts = decrease_easy_attempts()
       