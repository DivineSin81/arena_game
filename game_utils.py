def path():
    print(f'''
        What you wanna do?
        [1] Check Stats.
        [2] Tavern.
        [3] Fight.
        [4] Shop.
        [5] Shell Game.
        [6] Save Game.
        [7] Load Game.
        [0] Exit.
        ''')
    
def get_valid_input(prompt, valid_options):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(f"Please select valid option from {valid_options}")
        except ValueError:
            print("Please enter a valid number.")

def tavern(character):
    cost = character.lvl * 15
    print(f"In Tavern you can be healed to max HP. But it cost {cost} gold")
    heal_choice = get_valid_input("Do you want to be healed?\n[1] Yes\n[2] No\n", [1, 2])
    if heal_choice == 1:
        if character.gold >= cost:
            character.gold -= cost
            character.hp = character.maxhp
            print("Healed")
        else:
            print("Not enough gold to heal!")
    else:
        print("You leave the tavern.")