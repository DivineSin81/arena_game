class Character:
    def __init__(self, name, hp, maxhp, dmg, gold, lvl, exp, maxexp):
        self.__name = name
        self.hp = hp
        self.maxhp = maxhp
        self.dmg = dmg
        self.gold = gold
        self.lvl = lvl
        self.exp = exp
        self.maxexp = maxexp

    def __str__(self):
        return f"===========\nclass {self.__name}\nhp {self.hp}\nmaxhp {self.maxhp}\ndmg {self.dmg}\ngold {self.gold}\nlvl {self.lvl}\nexp {self.exp}\nmaxexp {self.maxexp}\n==========="
    
    @property
    def name(self):
        return self.__name
    
    def class_select(self):
        if self == 1:
            character = Warrior_class
            return character
        elif self == 2:
            character = Archer_class
            return character
        else:
            raise OverflowError('Sorry choosen class doesnt exists')

    def class_select_function():
        print("Hello!\nChoose your class:\n1.Warrior\n2.Archer")
        while True:
            try:
                select_class = int(input("Choose your class: "))
                character = Character.class_select(select_class)
                if character:
                    return character
                else:
                    print("Invalid class selection.")
            except ValueError:
                print("Please enter a valid number.")

Warrior_class = Character("Warrior", 250, 250, 100, 0, 1, 0, 100)
Archer_class = Character("Archer", 150, 150, 200, 60, 1, 0, 100)