

class Move:
    def __init__(self, name, move_type, category, power, accuracy, effect=None):
        self.name = name
        self.move_type = move_type
        self.category = category # "Physical" or "Special" or "Status"
        self.power = power
        self.accuracy = accuracy
        self.effect = effect

tackle = Move("Tackle", "Normal", "Physical", 40, 95)
scratch = Move("Scratch", "Normal", "Physical", 40, 100)
bite = Move("Bite", "Normal", "Physical", 40, 100)
growl = Move("Growl", "Normal", "Status", 0, 100, effect=("attack", -1))
leer = Move("Leer", "Normal", "Status", 0, 100, effect=("defence", -1))
slash = Move("Slash", "Normal", "Physical", 70, 100)
ember = Move("Ember", "Fire", "Special", 40, 100)
flamethrower = Move("Flamethrower", "Fire", "Special", 95, 100)
vine_whip = Move("Vine whip", "Grass", "Special", 35, 100)
razor_leaf = Move("Razor leaf", "Grass", "Special", 55, 95)
water_gun = Move("Water Gun", "Water", "Special", 40, 100)
hydro_pump = Move("Hydro pump", "Water", "Special", 120, 80)
thunder_shock = Move("ThunderShock", "Electric", "Special", 40, 100)
thunder = Move("Thunder", "Electric", "Special", 120, 70)
mud_slap = Move("Mud-Slap", "Ground", "Physical", 20, 100)
dig = Move("Dig", "Ground", "Physical", 60, 100)
