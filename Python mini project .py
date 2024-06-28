import random

print(">> Welcome to the Rock, Paper, Scissors game. <<")

options = ['rock', 'paper', 'scissors']

user_win = 0
comp_win = 0

while True:
    n = random.randint(0, 2)
    comp_opt = options[n]

    user_opt = input("Enter your option (rock, paper, scissors) or 'q' to quit: ").lower()

    if user_opt == 'q':
        break
    elif user_opt not in options:
        print("Kindly enter a valid option...")
        continue

    print(f"Computer chose: {comp_opt}")

    if user_opt == comp_opt:
        print("It's a tie!")
    elif (user_opt == 'rock' and comp_opt == 'scissors') or \
         (user_opt == 'paper' and comp_opt == 'rock') or \
         (user_opt == 'scissors' and comp_opt == 'paper'):
        user_win += 1
        print("You won!")
    else:
        comp_win += 1
        print("Computer won...")

print(f"You won {user_win} game(s) out of {user_win + comp_win}.")
