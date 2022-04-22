import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess= 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: ")) # user guess
        # now we want computer to give us some feedback like number is low or high any so we will use if
        if guess < random_number:
            print("Sorry! Guess again. Too low")
        elif guess > random_number:
            print("Sorry! Guess again. Too high")
        #break

    print(f"Yay congratulation! Tou have guess the number {random_number} correctly!!!")
#user_guess(15)

def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low    #could be high b/c low=high
        feedback = input(f"Is {guess} too high (H),too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f"yah! The Computer guessed your number {guess}, correctly!!!")

computer_guess(100)