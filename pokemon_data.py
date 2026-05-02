#pokemon_data.py

from pokemon import Pokemon 
from moves import Move, MOVES
import random

BASE_STATS = {
    "Charmander": ["Fire", 39, 52, 43, 60, 50, 65, ["Scratch", "Growl", "Ember"]],
    "Squirtle": ["Water", 44, 48, 65, 50, 64, 43, ["Scratch", "Leer", "Water Gun"]],
    "Bulbasaur": ["Grass", 45, 49, 49, 65, 65, 45, ["Tackle", "Leer", "Vine whip"]],
    "Pikachu": ["Electric", 35, 55, 30, 50, 40, 90, ["Scratch", "Growl", "ThunderShock"]],
    "Rhyhorn": ["Ground", 80, 85, 95, 30, 30, 25, ["Tackle", "Growl", "Mud-Slap"]]
}

def create_pokemon(name):
    data = BASE_STATS[name]
    stats = data[:-1]  
    moves = data[-1]   
    
    p = Pokemon(name, *stats)
    p.moves = moves
    return p

def get_random_opponent():
    name = random.choice(list(BASE_STATS.keys()))
    return create_pokemon(name)

