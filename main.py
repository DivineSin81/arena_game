from character import Character
from enemy import Enemy

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
      0.Exit.
      ''')


while character.hp > 0:
    select_road = int(input("Select: "))
    if select_road == 1:
        print(str(character))
    if select_road == 3:
        test_enemy = Enemy(100, 100, 20, 20)
        while test_enemy.hp > 0 and character.hp > 0:
            test_enemy.hp -= character.dmg
            character.hp -= test_enemy.dmg
            print(f"Your hp{character.hp} Enemy hp{test_enemy.hp}")
        if test_enemy.hp <= 0:
            print("You WIN")
            character.gold += test_enemy.gold
            character.exp += test_enemy.exp
        elif character.hp <= 0:
            print("You LOSE")
    elif select_road == 0:
        break
    else:
        print("Choose the right path!!")
