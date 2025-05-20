from character import Character
from enemy import Enemy
from weapon import Weapon
from item import Item

wepon1 = Weapon("Night Bringer Edge", 100, 20, 1, "weapon")

Weapon.test(2)

print("Hello!")
print("Choose your class:")
print("1-Warrior, 2-Archer")
select_class = int(input("Choose your class: "))
character = Character.class_select(select_class)

print(f"So let's begin your adventure as {character.name}")

print(f'''
    What you wanna do?
      1.Check Stats.
      2.Tavern.
      3.Fight.
      4.Shop.
      5.Shell Game.
      0.Exit.
      ''')


while character.hp > 0:
    select_road = int(input("Select: "))
    if select_road == 1:
        print(str(character))
    elif select_road == 3:
        Enemy.fight(character)
    elif select_road == 4:
        Item.shop(character, wepon1)
    elif select_road == 5:
        pass
    elif select_road == 0:
        break
    else:
        print("Choose the right path!!")