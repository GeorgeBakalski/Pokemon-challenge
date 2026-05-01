from pokemon import Pokemon 
import random

BASE_STATS = {
    "Charmander": ["Fire", 39, 52, 43, 60, 50, 65],
    "Squirtle": ["Water", 44, 48, 65, 50, 64, 43],
    "Bulbasaur": ["Grass", 45, 49, 49, 65, 65, 45],
    "Pikachu": ["Electric", 35, 55, 30, 50, 40, 90],
    "Rhyhorn": ["Ground", 80, 85, 95, 30, 30, 25]
}

def create_pokemon(name):
    stats = BASE_STATS[name]
    return Pokemon(name, *stats)

def get_random_opponent():
    name = random.choice(list(BASE_STATS.keys()))
    return create_pokemon(name)

def choose_starter():
    starters = ["Charmander", "Squirtle", "Bulbasaur"]
    while True:
        print("Choose your starter:")
        for i, name in enumerate(starters):
            print(f"{i+1}. {name}")
        
        user_input = input("> ")
        
        if user_input.isdigit():
            choice = int(user_input) - 1
            if 0 <= choice < len(starters):
                return create_pokemon(starters[choice])
        
        print("Invalid choice, try again!")