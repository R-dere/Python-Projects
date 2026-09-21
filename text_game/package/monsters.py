import random
class Slime_monster():
    def __init__(self):
        self.name = "Slime monster"
        self.options = ["Attack", "Defend", "Slime"]
        self.hp = 50
        self.defense = 0.4
        self.dmg = random.randint(30,40)
        self.speed = 3

    def damage(self,dmg):
        tot_dmg = dmg - int(dmg*self.defense)
        self.hp -= tot_dmg
        return tot_dmg

class Wendigo():
    def __init__(self):
        self.name = "Wendigo"
        self.options = ["Attack", "Defend", "leave", "Stalk"]
        self.hp = 70
        self.defense = 0.3
        self.dmg = random.randint(45,50)
        self.speed = 2
