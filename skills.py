from skill_classes import *
import random

class Fire_ball(Offensive_skill):

    def __init__(self, focus,char_crit_chance, spell_dmg, name, attack_type):
        self.char_chance_attack = 60
        self.focus = focus
        self.char_crit_chance = char_crit_chance

        super().__init__(spell_dmg, name, attack_type)
    #cast zwraca listę - obrażenia_dla_celu, obrazenia_atakujacego i efekt
    def cast(self) -> []:
        dmg = 0
        caster_dmg = 0
        effect = ''
        chance = random.randint(0,100)
        crit = random.randint(0, 100)
        if chance <= self.char_chance_attack:
            if crit <= self.char_crit_chance:
                dmg = (self.spell_dmg * 1.5 + self.focus)*2
                print(f"Zadałeś obrażenia krytyczne - {dmg}")
            else:
                dmg = self.spell_dmg * 1.5 + self.focus
                print(f"Zadałeś obrażenia - {dmg}")
        elif chance >= 95:
                if crit <= self.char_crit_chance:
                    caster_dmg = (self.spell_dmg * 1.5 + self.focus) * 2
                    print(f"Zadałeś SOBIE obrażenia krytyczne - {caster_dmg}")
                else:
                    caster_dmg = self.spell_dmg * 1.5 + self.focus
                    print(f"Zadałeś SOBIE obrażenia - {caster_dmg}")
        else:
            print("Cast failed.")
        return [dmg, caster_dmg, effect]

    def __repr__(self):
        return "FIREBALL - fire type. Calc: base attack * 1.5 + 1dmg\
        per each focus point. Critical failure: del 50% dmg to caster."

