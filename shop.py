from armor import Armor
from weapon import Weapon


def select_shop(character):
    print("Do you want to better protect yourself or deale more dmg?\n[1] Armor Shop\n[2] Weapon Shop\n[0]Exit")
    try:
        select = int(input(""))
        if select == 1:
            armor_shop(character)
        elif select == 2:
            weapon_shop(character)
        else:
            print("Invalid Shop.")
    except (ValueError):
        print("Invalid Selection.")

def weapon_shop(character):
    available_weapon = [w for w in Weapon.all if w.quantity > 0]

    print("Welcom to the Weapon Shop!")

    if not available_weapon:
        print("No weapons available right now.")
        return

    for index, weapon in enumerate(available_weapon):
        print(f"[{index}] {weapon.item_name} - DMG: {weapon.item_dmg}, Price {weapon.item_price}")

    try:
        buy = int(input("\nSelect the index of the weapon you want (-1 to cancel): "))
        if buy == -1:
            print("You left the shop.")
            return
        selected_weapon = available_weapon[buy]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    if character.gold < selected_weapon.item_price:
        print("Not enough gold!")
        return
    
    character.gold -= selected_weapon.item_price
    character.dmg += selected_weapon.item_dmg
    selected_weapon.quantity -= 1
    #Dodaj dodanie do eq

    print(f"\nYou bought {selected_weapon.item_name}! Your dmg increased to {character.dmg}. Gold left: {character.gold}")
        
def armor_shop(character):
    available_armor = [a for a in Armor.all if a.quantity >0]

    print("Welcom to the Armor Shop!")

    if not available_armor:
        print("No armor available right now.")
        return
    
    for index, armor in enumerate(available_armor):
        print(f"[{index}] {armor.item_name} - DEF: {armor.item_def}, Price {armor.item_price}")

    try:
        buy = int(input("\nSelect the index of the armor you want (-1 to cancel): "))
        if buy == -1:
            print("You left the shop.")
            return
        selected_armor = available_armor[buy]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    if character.gold < selected_armor.item_price:
        print("Not enough gold!")
        return
    
    character.gold -= selected_armor.item_price
    character.maxhp += selected_armor.item_def
    selected_armor.quantity -= 1

    print(f"\nYou bought {selected_armor.item_name}! Your max HP increased to {character.maxhp}. Gold left: {character.gold}")