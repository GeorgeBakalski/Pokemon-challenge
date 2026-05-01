import random

class Pokemon:
    def __init__(self, name, pokemon_type, hp, attack, defence, sp_attack, sp_def, speed):
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.hp_IV = random.randint(0,15)
        self.attack = attack
        self.attack_IV = random.randint(0,15)
        self.defence = defence
        self.defence_IV = random.randint(0,15)
        self.sp_attack = sp_attack
        self.sp_attack_IV = random.randint(0,15)
        self.sp_def = sp_def
        self.sp_def_IV = random.randint(0,15)
        self.speed = speed
        self.speed_IV = random.randint(0,15)
        self.level = 1
        self.stages = {
    "attack": 0,
    "defence": 0,
    "sp_attack": 0,
    "sp_def": 0,
    "speed": 0
}

    def get_hp(self):
        return int((((self.hp + self.hp_IV) * 2 * self.level) / 100) + self.level + 10)
    
    def _calculate_stat(self, base, iv):
        return int((((base + iv) * 2 * self.level) / 100) + 5)

    def get_attack(self):
        return self._calculate_stat(self.attack, self.attack_IV)
    
    def get_defence(self):
        return self._calculate_stat(self.defence, self.defence_IV)
    
    def get_sp_attack(self):
        return self._calculate_stat(self.sp_attack, self.sp_attack_IV)
    
    def get_sp_defence(self):
        return self._calculate_stat(self.sp_def, self.sp_def_IV)
    
    def get_speed(self):
        return self._calculate_stat(self.speed, self.speed_IV)