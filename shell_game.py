import random
from game_utils import get_valid_input


def shell_game(character):
    """Play a shell game where the player bets gold to guess the correct cup."""
    print("Let's gamble!")
    try:
        bet = get_valid_input("What is your bet? ", range(1, character.gold + 1))
    except ValueError:
        print("Invalid bet.")
        return

    print("Okey, we have 3 cups. Let's guess under which one is gold.")
    cups = [0, 0, 1]
    random.shuffle(cups)
    print("[0] [1] [2]")
    cup_select = get_valid_input("Choose your cup: ", [0, 1, 2])
    character.gold -= bet
    if cups[cup_select] == 1:
        character.gold += int(1.5 * bet)
        print(f"Congratulations! You win! Now, you have {character.gold}")
    else:
        print("You Lose!")
    replay = get_valid_input("Do you want to play again?\n1 - Yes\n2 - No\n", [1, 2])
    if replay == 1:
        bet = int(input("What is your bet? "))
    elif replay == 2:
        print("Bye, Bye!")