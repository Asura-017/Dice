import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")  # Wait for user input
    result = roll_dice()
    print(f"You rolled a {result} 🎲")
    
    play_again = input("Roll again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing! 🎲")
        break
