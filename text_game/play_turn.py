import package as p
import random

player = p.Player()
monsters = [p.Slime_monster(), ]
loot_w = [p.Aimbot_bow(), p.Rusty_sickle(), p.Bow(), p.Weak_bow(), p.Fists()]
chosen_weapon = False
current_monster = random.choice(monsters)
current_weapon = p.Fists()

def user_turn():
    global chosen_weapon
    global current_monster
    global current_weapon
    
    if player.potions != []:
            choice = int(input("""
            what would you like to do for your turn?
            1.Attack >:D
            2.Drink a potion
            3.Switch weapons (gives a bonus action but cannot attack this turn)
            """))
    else:
            choice = int(input("""
            what would you like to do for your turn?
            1.Attack >:D
            2.Drink a potion (none available)
            3.Switch weapons (gives a bonus action but cannot attack this turn)
            """))
    match choice:
        case 1:
            if not chosen_weapon:
                for i in range(current_weapon.hit_amt):
                    temp = random.randint(0,current_weapon.hit_chance)
                    if temp == 1:
                        print(f"you dealt {current_monster.damage(current_weapon.dmg)} damage on hit {i+1}")
                        current_monster.damage(current_weapon.dmg)
                        print(f"{current_monster.name} is on {current_monster.hp} HP!")
                    else:
                        print("you missed!")
            else:
                print("you can't do that!")
                user_turn()
        case 2:
            if player.potions != []:
                input(f"{player.potions} \nWhat potion would you like to drink? \n>>>")
            else:
                print("you can't do that!")
                user_turn()
        case 3:
            new_weap = input(f"{player.inventory} \n what weapon would you like to use?\n>>>")
            if new_weap in player.inventory:
                print(f"Equipped weapon {new_weap}!")
                chosen_weapon = True
                user_turn()
            else:
                print("you can't equip that,you don't have it!")
                user_turn()
