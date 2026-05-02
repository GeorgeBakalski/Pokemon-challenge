# battle.py
from player_choice import get_player_move
from ai_choice import get_npc_move
import random

def start_battle(player, opponent):
    print(f"\nA wild {opponent.name} appeared!")
    print(f"Go, {player.name}!")

    player_hp = player.get_hp()
    opponent_hp = opponent.get_hp()

    while player_hp > 0 and opponent_hp > 0:
        print(f"\n{player.name}: {player_hp}/{player.get_hp()} HP")
        print(f"{opponent.name}: {opponent_hp}/{opponent.get_hp()} HP")

        # 1. Get Moves
        p_move = get_player_move(player)
        o_move = get_npc_move(opponent, player, player_hp, player.get_hp())

        # 2. Determine Order
        if player.get_speed() >= opponent.get_speed():
            turn_order = [(player, opponent, p_move), (opponent, player, o_move)]
        else:
            turn_order = [(opponent, player, o_move), (player, opponent, p_move)]

        # 3. Execute Turns
        for attacker, defender, move in turn_order:
            move_acc = move.accuracy
            acc_mult = attacker.get_accuracy_multiplier()
            eva_mult = defender.get_evasion_multiplier()
            final_chance = move_acc * (acc_mult / eva_mult)
            
            if random.randint(1, 100) <= final_chance:
                print(f"\n{attacker.name} used {move.name}!")
                
                if move.category == "Status":
                    defender.apply_status_effect(move.effect)
                else:
                    damage = defender.take_damage(move, attacker)
                    if attacker == player:
                        opponent_hp -= damage
                    else:
                        player_hp -= damage
                    print(f"It dealt {damage} damage!")

                if player_hp <= 0 or opponent_hp <= 0:
                    break
            else:
                print(f"{attacker.name}'s attack missed!")

    if player_hp > 0:
        print(f"\n{opponent.name} fainted! You win!")
        return True
    else:
        print(f"\n{player.name} fainted! Game Over.")
        return False