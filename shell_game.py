import random
from game_utils import get_valid_input


def shell_game(character):
    print("Let's gamble!")
    bet = int(input("What is your bet? "))
    while bet > 0 and bet <= character.gold:
        print("Okey, we have 3 cups. Let's guess under witch one is gold.")
        cups = [0, 0, 1]
        random.shuffle(cups)
        print("[0] [1] [2]")
        cup_select = get_valid_input("Choose your cup: ", [0, 1, 2])
        character.gold -= bet
        if cups[cup_select] == 1:
            character.gold += int(1.5 * bet)
            print(f"Congratulation! You win! Now, you have {character.gold}")
        else:
            print("You Lose!")
        replay = get_valid_input("Do you want to play again?\n1 - Yes\n2 - No\n", [1, 2])
        if replay == 1:
            bet = int(input("What is your bet? "))
        elif replay == 2:
            print("Bye, Bye!")
            break
    if bet > character.gold:
        print("Sorry, not enough money.")