#moves.py

class Move:
    def __init__(self, name, move_type, category, power, accuracy, effect=None):
        self.name = name
        self.move_type = move_type
        self.category = category # "Physical" or "Special" or "Status"
        self.power = power
        self.accuracy = accuracy
        self.effect = effect

MOVES = {
    "Tackle" : Move("Tackle", "Normal", "Physical", 40, 95),
    "Scratch" : Move("Scratch", "Normal", "Physical", 40, 100),
    "Bite" : Move("Bite", "Normal", "Physical", 60, 100),
    "Growl" : Move("Growl", "Normal", "Status", 0, 100, effect=("attack", -1)),
    "Leer" : Move("Leer", "Normal", "Status", 0, 100, effect=("defence", -1)),
    "Slash" : Move("Slash", "Normal", "Physical", 70, 100),
    "Ember" : Move("Ember", "Fire", "Special", 40, 100),
    "Flamethrower" : Move("Flamethrower", "Fire", "Special", 95, 100),
    "Vine whip" : Move("Vine whip", "Grass", "Special", 35, 100),
    "Razor leaf" : Move("Razor leaf", "Grass", "Special", 55, 95),
    "Water Gun" : Move("Water Gun", "Water", "Special", 40, 100),
    "Hydro pump" : Move("Hydro pump", "Water", "Special", 120, 80),
    "ThunderShock" : Move("ThunderShock", "Electric", "Special", 40, 100),
    "Thunder" : Move("Thunder", "Electric", "Special", 120, 70),
    "Mud-Slap" : Move("Mud-Slap", "Ground", "Physical", 20, 100),
    "Dig" : Move("Dig", "Ground", "Physical", 60, 100),
}