class Enemy:
    def __init__(self, hp, dmg, exp, gold):
        self.hp = hp
        self.dmg = dmg
        self.exp = exp
        self.gold = gold
    
    def fight(self):
        enemy1 = Enemy(100, 100, 20, 20)
        print(f"Your hp{self.hp} Enemy hp{enemy1.hp}")
        while enemy1.hp > 0 and self.hp > 0:
            enemy1.hp -= self.dmg
            self.hp -= enemy1.dmg
            print(f"Your hp{self.hp} Enemy hp{enemy1.hp}")
        if enemy1.hp <= 0:
            print("You WIN")
            self.gold += enemy1.gold
            self.exp += enemy1.exp
        elif self.hp <= 0:
            print("You LOSE")


enemy1 = Enemy(100, 100, 20, 20)