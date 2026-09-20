class Player():
    def __init__(self):
        self.inventory = []
        self.hp = 150
        self.defense = 0.3
        self.speed = 5
        self.potions = []
    

    def damage(self, dmg):
        self.hp -= dmg - int(dmg*self.defense)
        print("you took damage!")
        
    
    def inv_add(self, item):
        self.inventory.append(item)