# battle.py
from ai_choice import get_npc_move
import random
    
def process_battle_round(player, opponent, p_move, player_current_hp, opponent_current_hp):
    round_results = [] 
    
    p_hp = player_current_hp
    o_hp = opponent_current_hp
    o_move = get_npc_move(opponent, player, p_hp, player.get_hp())

    if player.get_speed() >= opponent.get_speed():
        turn_order = [(player, opponent, p_move), (opponent, player, o_move)]
    else:
        turn_order = [(opponent, player, o_move), (player, opponent, p_move)]

    for attacker, defender, move in turn_order:
        damage, msgs = execute_turn(attacker, defender, move)
        
        if attacker == player:
            o_hp -= damage
        else:
            p_hp -= damage
        
        round_results.append({
            "attacker_name": attacker.name,
            "damage": damage,
            "messages": msgs,
            "player_hp_after": p_hp,    
            "opponent_hp_after": o_hp
        })

        if p_hp <= 0 or o_hp <= 0:
            if o_hp <= 0:
                round_results[-1]["messages"].append(f"{opponent.name} fainted!")
            if p_hp <= 0:
                round_results[-1]["messages"].append(f"{player.name} fainted!")
            break 
    
    return round_results

def execute_turn(attacker, defender, move):
    messages = []
    
    # Accuracy check
    move_acc = move.accuracy
    acc_mult = attacker.get_accuracy_multiplier()
    eva_mult = defender.get_evasion_multiplier()
    final_chance = move_acc * (acc_mult / eva_mult)
    
    if random.randint(1, 100) <= final_chance:
        messages.append(f"{attacker.name} used {move.name}!")
        
        if move.category == "Status":
            status_msg = defender.apply_status_effect(move.effect)
            messages.append(status_msg)
            return 0, messages
        else:
            damage, effect_msg = defender.take_damage(move, attacker)
            if effect_msg:
                messages.append(effect_msg)
            messages.append(f"It dealt {damage} damage!")
            return damage, messages
    else:
        messages.append(f"{attacker.name}'s attack missed!")
        return 0, messages