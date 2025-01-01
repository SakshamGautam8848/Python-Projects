import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    elif player =="scissors" and computer == "paper":
        print("You Win")
    else:
        print("You lose!")

    play_again = input("Play Again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thanks for playing!")