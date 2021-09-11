import random


class Creature:

    def __init__(self, id=0, name='Imie', playable=0, attitude=0, is_alive=0, base_attack=1):
        self.char_id = id
        self.name = name
        self.playable = playable
        self.attitude = attitude
        self.is_alive = is_alive
        self.base_attack = base_attack

    def __repr__(self) -> str:
        return f"Creature object - name: {self.name}, playable -  {self.playable}, attitude - {self.attitude}, is alive? {self.is_alive}, base attack - {self.base_attack}"


class Active_creature(Creature):

    def __init__(
            self, char_id = 10, name='', playable=0, attitude=0, is_alive=1, base_attack=1, dodge_chance=5,
            parry_chance=5, res_holy=0, res_shadow=0, res_arcane=0, res_water=0,
            res_fire=0, res_nature=0, crit_chance=5, hit_points=50, initiative=3,
            first_attack_chance=75, focus=0, precision=0, strength=0
    ):
        self.dodge_chance = dodge_chance
        self.parry_chance = parry_chance
        self.res_holy = res_holy
        self.res_shadow = res_shadow
        self.res_arcane = res_arcane
        self.res_water = res_water
        self.res_fire = res_fire
        self.res_nature = res_nature
        self.crit_chance = crit_chance
        self.hit_points = hit_points
        self.initiative = initiative
        self.first_attack_chance = first_attack_chance
        self.focus = focus
        self.precision = precision
        self.strength = strength

        super().__init__(char_id, name, playable, attitude, is_alive, base_attack)

    def base_attack_method(self):
        attack = random.randint(0, 100)
        if attack <= self.first_attack_chance:
            crit = random.randint(0,100)
            if crit <= self.crit_chance:
                print("CRITICAL HIT!")
                crit = 2
            else:
                crit = 1
            attack = (self.base_attack * self.strength) * crit
            print(f"Attack value = {attack}")
            return attack
        else:
            print("Attack failed")
            attack = -1
            return attack

        print("I'm attacking...")

    def dodge(self) -> bool:
        dodge = random.randint(0, 100)
        print(f"Dice roll: {dodge}")
        if dodge <= self.dodge_chance:
            print("Success! Dodged.")
            dodge = True
        else:
            print("Failed! U got hit!")
            dodge = False
        return dodge

    def __repr__(self):
        return (super().__repr__() + " Resistance " + str(self.res_fire))


d = Active_creature("test", dodge_chance=50, base_attack=3, first_attack_chance= 70,
                    strength=1, crit_chance=20)
print(d.base_attack_method())
