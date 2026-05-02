#player_choice.py
from moves import MOVES
from pokemon_data import create_pokemon

def get_player_move(pokemon):
    print(f"\nWhat will {pokemon.name} do?")
    for i, move_name in enumerate(pokemon.moves):
        move = MOVES[move_name]
        print(f"{i+1}. {move.name} ({move.move_type} | {move.category})")

    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(pokemon.moves):
                return MOVES[pokemon.moves[choice]]
            print("Invalid choice, pick a move from the list.")
        except ValueError:
            print("Please enter a number.")


def choose_starter():
    starters = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu", "Rhyhorn"]
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