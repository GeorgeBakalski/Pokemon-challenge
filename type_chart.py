# type_chart.py

TYPE_EFFECTIVENESS = {
    "Fire": {
        "Grass": 2.0,
        "Water": 0.5,
        "Fire": 0.5,
        "Bug": 2.0,
        "Ice": 2.0,
        "Steel": 2.0
    },
    "Water": {
        "Fire": 2.0,
        "Grass": 0.5,
        "Water": 0.5,
        "Ground": 2.0,
        "Rock": 2.0
    },
    "Grass": {
        "Water": 2.0,
        "Fire": 0.5,
        "Grass": 0.5,
        "Ground": 2.0,
        "Rock": 2.0,
        "Poison": 0.5
    },
    "Electric": {
        "Water": 2.0,
        "Grass": 0.5,
        "Electric": 0.5,
        "Ground": 0.0,
        "Flying": 2.0
    },
    "Ground": {
        "Electric": 2.0,
        "Fire": 2.0,
        "Grass": 0.5,
        "Poison": 2.0,
        "Rock": 2.0,
        "Flying": 0.0
    },
    "Normal": {
        "Rock": 0.5,
        "Steel": 0.5,
        "Ghost": 0.0
    }
}

def get_multiplier(move_type, defender_type):
    if move_type not in TYPE_EFFECTIVENESS:
        return 1.0
    
    return TYPE_EFFECTIVENESS[move_type].get(defender_type, 1.0)