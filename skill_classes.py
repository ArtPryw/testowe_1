import random
'''FIREBAL - typ ogień, zwraca obrażenia. 
bazowy atak * 1.5 + 1dmg za każdy punkt focus. 
Krytyczne niepowodzenie zadaje połowe obrażeń rzucającemu.'''

class Skill:
    def __init__(self, name, attack_type):
        self.name = name
        self.type = attack_type

    #cast zwraca listę - obrażenia_dla_celu, obrazenia_atakujacego i efekt
    def cast(self):
        print("Cast a spell.")

class Offensive_skill(Skill):
    
    def __init__(self, spell_dmg, name, attack_type):
        self.spell_dmg = spell_dmg
        super().__init__(name, attack_type)

class Defensive_skill(Skill):
    
    def __init__(self, pros, name, attack_type):
        self.pros = pros
        super().__init__(name, attack_type)