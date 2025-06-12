import json
from character import Character
from weapon import Weapon
from armor import Armor


def save_game(character):
    try:
        with open("save.json", "w") as f:
            json.dump({
                "name": character.name,
                "hp": character.hp,
                "maxhp": character.maxhp,
                "dmg": character.dmg,
                "crit_chance": character.crit_chance,
                "dodge_chance": character.dodge_chance,
                "gold": character.gold,
                "lvl": character.lvl,
                "exp": character.exp,
                "maxexp": character.maxexp,
                "equiped_weapon": character.equiped_weapon.item_name if character.equiped_weapon else None,
                "equiped_armor": character.equiped_armor.item_bane if character.equiped_armor else None,
                "inventory": [
                    {
                        "item_name": item.item_name,
                        "type": item.type,
                        "item_dmg": item.item_dmg if item.type == "weapon" else 0,
                        "item_crit_chance": item.item_crit_chance if item.type == "weapon" else 0,
                        "item_def": item.item_def if item.type == "armor" else 0,
                        "item_sub_stat": item.item_sub_stat if item.type == "armor" else 0,
                        "item_price": item.item_price,
                        "quantity": item.quantity
                    } for item in character.inventory
                ]
            }, f)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Failed to save game: {e}")

def load_game():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
            character = Character(
                data["name"],
                data["hp"],
                data["maxhp"],
                data["dmg"],
                data["crit_chance"],
                data["dodge_chance"],
                data["gold"],
                data["lvl"],
                data["exp"],
                data["maxexp"],
                data["equiped_weapon"],
                data["equiped_armor"],
                data["inventory"]
            )
            for item_data in data.get("inventory", []):
                if item_data["type"] == "weapon":
                    item = Weapon(
                        item_data["item_name"],
                        item_data["item_dmg"],
                        item_data["item_crit_chance"],
                        item_data["item_price"],
                        item_data["quantity"]
                    )
                elif item_data["type"] == "armor":
                    item = Armor(
                        item_data["item_name"],
                        item_data["item_def"],
                        item_data["item_sub_stat"],
                        item_data["item_price"],
                        item_data["quantity"]
                    )
                character.add_to_inventory(item)

            equiped_weapon_name = data.get("equiped_weapon")
            equiped_armor_name = data.get("equiped_armor")
            for item in character.inventory:
                if equiped_weapon_name and item.item_name == equiped_weapon_name and item.type == "weapon":
                    character.equip_item(item)
                if equiped_armor_name and item.item_name == equiped_armor_name and item.type == "armor":
                    character.equip_item(item)

            print("Character loaded successfully")
            return character
    except FileNotFoundError:
        print("No saved game found.")
        return None
    except KeyError as e:
        print(f"Corrupted save file: Missing key {e}")
        return None