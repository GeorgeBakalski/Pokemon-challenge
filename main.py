#main.py
from player_choice import choose_starter
from pokemon_data import get_random_opponent
from battle import start_battle

def main():
    player_mon = choose_starter()
    player_mon.level = 5
    current_health = player_mon.get_hp()
    wins = 0

    while True:
        battle = "Normal"
        wins += 1
        
        if wins % 10 == 0:
            battle = "BOSS"
            opponent = get_random_opponent()
            opponent.level = player_mon.level + 2
            print(f"--- BOSS BATTLE: {opponent.name} Level {opponent.level} ---")
            levels_to_gain = 5
        else:
            opponent = get_random_opponent()
            opponent.level = max(1, player_mon.level - 2)
            levels_to_gain = 1

        victory, current_health = start_battle(player_mon, opponent, current_health)

        if victory:
            if battle == "BOSS" :
                player_mon.gain_level(levels_to_gain)
                current_health = player_mon.get_hp()
                player_mon.stages = {
    "attack": 0,
    "defence": 0,
    "sp_attack": 0,
    "sp_defence": 0,
    "speed": 0,
    "accuracy": 0,
    "evasion": 0
}
            else:
                old_max = player_mon.get_hp() 
                player_mon.gain_level(levels_to_gain)
                new_max = player_mon.get_hp() 

                hp_gained = new_max - old_max
                heal_amount = int(player_mon.get_hp() * 0.20)
                current_health = min(player_mon.get_hp(), current_health + heal_amount)
                    
        else:
            print(f"Game Over! Final Score: {wins - 1}")
            break
  
if __name__ == "__main__":
    main()