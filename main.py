from character import Character
from enemy import Enemy
import save_load
import shell_game
import shop
import game_utils


def main_loop(character):
    while character.hp > 0:
        game_utils.path()
        select_road = game_utils.get_valid_input("Select: ", [0, 1, 2, 3, 4, 5, 6, 7])
        if select_road == 1:
            print(str(character))
        elif select_road == 2:
            game_utils.tavern(character)
        elif select_road == 3:
            Enemy.fight(character)
        elif select_road == 4:
            shop.select_shop(character)
        elif select_road == 5:
            shell_game.shell_game(character)
        elif select_road == 6:
            save_load.save_game(character)
        elif select_road == 7:
            loaded_character = save_load.load_game()
            if loaded_character:
                return loaded_character
        elif select_road == 0:
            break


if __name__ == "__main__":
    character = Character.select_class()
    while True:
        character = main_loop(character)
        if character is None or character.hp <= 0:
            print("Game Over.")
            break