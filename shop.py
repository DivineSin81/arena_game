from armor import Armor
import game_utils
from weapon import Weapon


def select_shop(character):
    print("Do you want to better protect yourself or deal more dmg?\n[1] Armor Shop\n[2] Weapon Shop\n[0] Exit")
    try:
        select = game_utils.get_valid_input("", [0, 1, 2])
        if select == 1:
            shop_menu(character, "armor", Armor.all)
        elif select == 2:
            shop_menu(character, "weapon", Weapon.all)
    except (ValueError):
        print("Invalid Selection.")

def shop_menu(character, item_type, item_list):
    available_items = [item for item in item_list if item.quantity > 0]
    print(f"Welcome to the {item_type.capitalize()} Shop!")

    if not available_items:
        print(f"No {item_type}s available right now.")
        return
    
    for index, item in enumerate(available_items):
        stat = item.item_dmg if item_type == "weapon" else item.item_def
        sub_stat = item.item_crit_chance if item_type == "weapon" else item.item_sub_stat
        print(f"[{index}] {item.item_name} - {'DMG' if item_type == 'weapon' else 'DEF'}: {stat}, {'Crit chance' if item_type == 'weapon' else 'Dodge/Block chance'}: {sub_stat * 100}%, Price: {item.item_price}")

    buy = game_utils.get_valid_input(f"\nSelect the index of the {item_type} you want (-1 to cancel): ", [-1] + list(range(len(available_items))))
        
    if buy == -1:
        print("You left the shop.")
        return
        
    selected_item = available_items[buy]  
    if character.gold < selected_item.item_price:
        print("Not enough gold!")
        return
    
    character.gold -= selected_item.item_price
    selected_item.quantity -= 1
    character.add_to_inventory(selected_item)
    character.equip_item(selected_item)

    print(f"\nYou bought {selected_item.item_name}! Your {'dmg' if item_type == 'weapon' else 'max HP'} increased to {character.dmg if item_type == 'weapon' else character.maxhp}. Your {'critical chance' if item_type == 'weapon' else 'Dodge/Block chance'} to {character.crit_chance * 100 if item_type == 'weapon' else character.dodge_chance * 100}% Gold left: {character.gold}")