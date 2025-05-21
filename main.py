from character import Character
from enemy import Enemy
import shell_game
import shop
import texts


def main_loop(character):
    while character.hp > 0:
        texts.path()
        try:
            select_road = int(input("Select: "))
            if select_road == 1:
                print(str(character))
            elif select_road == 3:
                Enemy.fight(character)
            elif select_road == 4:
                shop.select_shop(character)
            elif select_road == 5:
                shell_game.shell_game(character)
            elif select_road == 0:
                break
            else:
                print("Choose the right path!!")
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    character = Character.class_select_function()
    main_loop(character)