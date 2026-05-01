

def start_battle(player, opponent):
    print(f"A wild {opponent.name} appeared!")
    print(f"Go, {player.name}!")

    player_current_hp = player.get_hp()
    opponent_current_hp = opponent.get_hp()

    while player_current_hp > 0 and opponent_current_hp > 0:
        
        # 1. Determine who goes first based on get_speed()
        # 2. Let the first one attack
        # 3. Check if the second one fainted
        # 4. If not, let the second one attack
        pass