#pokemon.py
import random
from type_chart import get_multiplier

class Pokemon:
    def __init__(self, name, pokedex_id, pokemon_type, hp, attack, defence, sp_attack, sp_defence, speed, moves=None):
        self.name = name
        self.pokedex_id = pokedex_id
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.hp_IV = random.randint(0,15)
        self.attack = attack
        self.attack_IV = random.randint(0,15)
        self.defence = defence
        self.defence_IV = random.randint(0,15)
        self.sp_attack = sp_attack
        self.sp_attack_IV = random.randint(0,15)
        self.sp_defence = sp_defence
        self.sp_defence_IV = random.randint(0,15)
        self.speed = speed
        self.speed_IV = random.randint(0,15)
        if moves is None:
            self.moves = []
        else:
            self.moves = moves
        self.level = 1
        self.stages = {
    "attack": 0,
    "defence": 0,
    "sp_attack": 0,
    "sp_defence": 0,
    "speed": 0,
    "accuracy": 0,
    "evasion": 0
}

    def get_hp(self):
        return int((((self.hp + self.hp_IV) * 2 * self.level) / 100) + self.level + 10)
    
    def _calculate_stat(self, base, iv, stat_name):
        stat = int((((base + iv) * 2 * self.level) / 100) + 5)
        stage = self.stages.get(stat_name, 0)
        
        if stage >= 0:
            multiplier = (2 + stage) / 2
        else:
            multiplier = 2 / (2 + abs(stage))
            
        return int(stat * multiplier)

    def get_attack(self):
        return self._calculate_stat(self.attack, self.attack_IV, "attack")

    def get_defence(self):
        return self._calculate_stat(self.defence, self.defence_IV, "defence")

    def get_sp_attack(self):
        return self._calculate_stat(self.sp_attack, self.sp_attack_IV, "sp_attack")

    def get_sp_defence(self):
        return self._calculate_stat(self.sp_defence, self.sp_defence_IV, "sp_defence")

    def get_speed(self):
        return self._calculate_stat(self.speed, self.speed_IV, "speed")
        
    def take_damage(self, move, opponent):
        if move.category == "Physical":
            atk = opponent.get_attack()
            dfe = self.get_defence()
        elif move.category == "Special":
            atk = opponent.get_sp_attack()
            dfe = self.get_sp_defence()
        else:
            return 0 

        crit_chance = random.randint(0, 15)
        multiplier = get_multiplier(move.move_type, self.pokemon_type)
        stab = 1
        if move.move_type == opponent.pokemon_type:
            stab = 1.5

        level_mult = (2 * opponent.level / 5) + 2 if crit_chance == 0 else (opponent.level / 5) + 2

        damage = (((level_mult * move.power * (atk / dfe)) / 50) + 2) * multiplier * stab

        msg = ""
        if multiplier > 1:
            msg = "It's super effective!"
        elif multiplier < 1 and multiplier > 0:
            msg = "It's not very effective..."
        elif multiplier == 0:
            msg = f"It had no effect on {self.name}!"
        
        return int(damage), msg
    
    def apply_status_effect(self, effect):
        msg = ""
        if effect is None:
            return
        
        stat_name, change = effect
        new_stage = self.stages[stat_name] + change
        self.stages[stat_name] = max(-6, min(6, new_stage))
        
        direction = "fell" if change < 0 else "rose"
        msg = f"{self.name}'s {stat_name} {direction}!"
        return msg

    def get_accuracy_multiplier(self):
        stage = self.stages.get("accuracy", 0)
        if stage >= 0:
            return (3 + stage) / 3
        else:
            return 3 / (3 + abs(stage))
        
    def get_evasion_multiplier(self):
        stage = self.stages.get("evasion", 0)
        if stage >= 0:
            return (3 + stage) / 3
        else:
            return 3 / (3 + abs(stage))
        
    def gain_level(self, amount=1):
        self.level += amount
        print(f"{self.name} grew to level {self.level}!")