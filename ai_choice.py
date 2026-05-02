# ai_choice.py
import random
from moves import MOVES
from type_chart import get_multiplier

def get_npc_move(npc_pokemon, player_pokemon, player_current_hp, player_max_hp):

    if player_current_hp > (player_max_hp * 0.7):
        status_moves = [m for m in npc_pokemon.moves if MOVES[m].category == "Status"]
 
        if status_moves and random.random() < 0.5:
            return MOVES[random.choice(status_moves)]

    if random.random() < 0.15:
            return MOVES[random.choice(npc_pokemon.moves)]
    
    best_move = None
    best_score = -1
    
    attacking_moves = [m for m in npc_pokemon.moves if MOVES[m].category != "Status"]
    
    if not attacking_moves:
        return MOVES[npc_pokemon.moves[0]]

    for move_name in attacking_moves:
        move = MOVES[move_name]
        
        # Calculate score based on Type Multiplier and STAB
        score = get_multiplier(move.move_type, player_pokemon.pokemon_type)
        if move.move_type == npc_pokemon.pokemon_type:
            score *= 1.5
            
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move