#pokemon_data.py

from pokemon import Pokemon 
from moves import Move, MOVES
import random

BASE_STATS = {
    "Charmander": {
        "id": 4,
        "type": "Fire",
        "hp": 39,
        "attack": 52,
        "defence": 43,
        "sp_attack": 60,
        "sp_defence": 50,
        "speed": 65,
        "moves": ["Scratch", "Growl", "Ember"],
        "front_img": "assets/sprites/4.png",
        "back_img": "assets/sprites/back/4.png"
    },
    "Squirtle": {
        "id": 7,
        "type": "Water",
        "hp": 44,
        "attack": 48,
        "defence": 65,
        "sp_attack": 50,
        "sp_defence": 64,
        "speed": 43,
        "moves": ["Scratch", "Leer", "Water Gun"],
        "front_img": "assets/sprites/7.png",
        "back_img": "assets/sprites/back/7.png"
    },
    "Bulbasaur": {
        "id": 1,
        "type": "Grass",
        "hp": 45,
        "attack": 49,
        "defence": 49,
        "sp_attack": 65,
        "sp_defence": 65,
        "speed": 45,
        "moves": ["Tackle", "Leer", "Vine whip"],
        "front_img": "assets/sprites/1.png",
        "back_img": "assets/sprites/back/1.png"
    },
    "Pikachu": {
        "id": 25,
        "type": "Electric",
        "hp": 35,
        "attack": 55,
        "defence": 30,
        "sp_attack": 50,
        "sp_defence": 40,
        "speed": 90,
        "moves": ["Scratch", "Growl", "ThunderShock"],
        "front_img": "assets/sprites/25.png",
        "back_img": "assets/sprites/back/25.png"
    },
    "Rhyhorn": {
        "id": 111,
        "type": "Ground",
        "hp": 80,
        "attack": 85,
        "defence": 95,
        "sp_attack": 30,
        "sp_defence": 30,
        "speed": 25,
        "moves": ["Tackle", "Growl", "Mud-Slap"],
        "front_img": "assets/sprites/111.png",
        "back_img": "assets/sprites/back/111.png"
    }
}
def create_pokemon(name):
    data = BASE_STATS[name]
    
    # Pokemon stats
    p = Pokemon(
        name, 
         data["id"],
        data["type"], 
        data["hp"], 
        data["attack"], 
        data["defence"], 
        data["sp_attack"], 
        data["sp_defence"], 
        data["speed"]
    )
    
    # Moves and appearance
    p.moves = data["moves"]
    p.front_img = data["front_img"]
    p.back_img = data["back_img"]
    
    return p

def get_random_opponent():
    name = random.choice(list(BASE_STATS.keys()))
    return create_pokemon(name)

