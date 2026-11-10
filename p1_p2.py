class Card():
    def __init__(self, name, hp, deff,  atk, mana):
        self.name = name 
        self.hp = hp
        self.deff = deff
        self.atk = atk
        self.mana = mana


        
        
class Griffin(Card):
    def __init__(self, name, hp, deff,  atk, mana):
        self.name = "Griffin"
        self.hp = 10
        self.deff = 1
        self.atk = 2
        self.mana = 10
    def voice_line(self):
        print("SKREAAATCCCHH!!!!!")
    def basic_attack(self, atk ):
        basic_attack = self.atk * 1 
    def advance_attack(self, atk):   
        advance_attack = self.atk * 2
class Wild_Slime(Card):
    def __init__(self, name, hp, deff, atk, mana):
        self.name = "Wild Slime"
        self.hp = 10
        self.deff = 0
        self.atk = 1
        self.mana = 0
    def voice_line(self):   
        print("Bloop bloop ") 
class Wild_Wolf(Card):
    def __init__(self, name, hp, deff, atk, mana):
        self.name = "Wild Slime"
        self.hp = 10
        self.deff = 1
        self.atk = 1
        self.mana = 1


player = Griffin("Griffin", 10, 1, 2, 10)
monster = Wild_Slime("Wild Slime", 10, 0 ,1, 0)

player_current_mana = player.mana
monster_current_mana = monster.mana

player_current_hp = player.hp
monster_current_hp = monster.hp
while player.hp > 0:

    print(
         f"\n--- Status ---\n[Spelare: {player.name}] HP: {player.hp} | Mana: {player.mana}"
    )
    print(f"[{monster.name}] HP: {monster.hp} | Mana: {monster.mana}")
    
    if monster.hp <= 0:
        print(f"{monster.name} slakdagd")
    move = int(input("   Vill du?\n1) attackera\n2) Hoppa över din attackrunda för att få 2 Mana: "))
    if move == 1:
        attack_type = int(input("   Vill du: \n1) Basic attack\n2) advance attack(-3 mana)"))
        if attack_type == 1:
            player.mana += 1
            player.voice_line()
            damage = player.atk - monster.deff
            if damage > 0:
                monster_current_hp -= damage   
                print(f"  {monster.name} tog 1 skada\n{monster.name} har nu {monster.hp}hp kvar: ")
            else:
                print(f"{monster.name} defense är för högt för att du ska kunna skada den med denna attack")  
        elif attack_type == "2":
            if player.mana >= 3:
                player.voice_line()
                player.mana -= 3
                damage = (player.atk * 2) - monster.deff

                if damage > 0:
                    monster.hp -= damage
                    print(
                        f"{monster.name} tog {damage} skada och har nu {monster.hp} HP kvar."
                    )
                else:
                    print(f"{monster.name} tog ingen skada.")
            else:
                print("Du har inte tillräckligt med mana!")  



    
        

