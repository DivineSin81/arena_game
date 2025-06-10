class Character:
    def __init__(self, name, hp, maxhp, dmg, gold, lvl, exp, maxexp):
        self._name = name
        self._hp = max(0, hp)
        self._maxhp = max(0, maxhp)
        self._dmg = max(0, dmg)
        self._gold = max(0, gold)
        self._lvl = max(1, lvl)
        self._exp = max(0, exp)
        self._maxexp = max(0, maxexp)
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._maxhp))
    
    @property
    def maxhp(self):
        return self._maxhp
    
    @maxhp.setter
    def maxhp(self, value):
        self._maxhp = max(0, value)
        if self._hp > self._maxhp:
            self._hp = self._maxhp
    
    @property
    def dmg(self):
        return self._dmg
    
    @dmg.setter
    def dmg(self, value):
        self._dmg = max(0, value)
    
    @property
    def gold(self):
        return self._gold
    
    @gold.setter
    def gold(self, value):
        self._gold = max(0, value)
    
    @property
    def lvl(self):
        return self._lvl
    
    @lvl.setter
    def lvl(self, value):
        self._lvl = max(1, value)
    
    @property
    def exp(self):
        return self._exp
    
    @exp.setter
    def exp(self, value):
        self._exp = max(0, value)
        while self._exp >= self._maxexp:
            self.level_up()
    
    @property
    def maxexp(self):
        return self._maxexp
    
    @maxexp.setter
    def maxexp(self, value):
        self._maxexp = max(1, value)

    def level_up(self):
        self._lvl += 1
        self._exp -= self._maxexp
        self._maxexp = int(self._maxexp * 1.5)
        self._maxhp += 50
        self._hp = self._maxhp
        self._dmg += 20
        print(f"Level Up! You are now level {self._lvl}. Max HP: {self._maxhp}, DMG: {self._dmg}")

    def __str__(self):
        return f"===========\nclass {self._name}\nhp {self._hp}\nmaxhp {self._maxhp}\ndmg {self._dmg}\ngold {self._gold}\nlvl {self._lvl}\nexp {self._exp}\nmaxexp {self._maxexp}\n==========="
    
    @staticmethod
    def select_class():
        print("Hello!\nChoose your class:\n1.Warrior\n2.Archer")
        while True:
            try:
                select_class = int(input("Choose your class: "))
                if select_class == 1:
                    return Character("Warrior", 250, 250, 100, 0, 1, 0, 100)
                elif select_class == 2:
                    return Character("Archer", 150, 150, 200, 60, 1, 0, 100)
                else:
                    print("Invalid class selection.")
            except ValueError:
                print("Please enter a valid number.")