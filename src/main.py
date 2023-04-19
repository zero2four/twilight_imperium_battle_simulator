from ship import Ship, Fleet
from enum import Enum





    

class BattleResult(Enum):
    Attacker_win = 1
    Defender_win = 2
    Draw = 3

def simulate_battle(defender_fleet, attaker_fleet, make_battle_report = False) -> BattleResult:
    battle_round = 0
    while not defender_fleet.destroyed and not attaker_fleet.destroyed:
        #ToDo - make an option to get more battle details 

        defender_hits = defender_fleet.produce_hits()
        attaker_hits = attaker_fleet.produce_hits()
        
        defender_fleet.distribute_hits(attaker_hits)
        attaker_fleet.distribute_hits(defender_hits)
        
        if defender_fleet.destroyed and attaker_fleet.destroyed:
            return BattleResult(3)
            
        if defender_fleet.destroyed:
            return BattleResult(1)
            
        if attaker_fleet.destroyed:
            return BattleResult(2)

        battle_round += 1
        if battle_round > 100:
            raise RuntimeWarning("more then 100 iterations in a singe round of combat")
            break



def simulate_many_battles(num_simulations:int, defender_fleet: Fleet, attaker_fleet:Fleet):
    print("attakers:", attaker_list)
    print("defenders:", defender_list)
    attacker_wins = 0
    defender_wins = 0
    draw = 0
    for i in range(0,num_simulations,1):
        attaker_fleet = Fleet(attaker_list)
        defender_fleet = Fleet(defender_list)
        
        result = simulate_battle(defender_fleet, attaker_fleet)
        if result == BattleResult(1):
            attacker_wins += 1
        elif result == BattleResult(2):
            defender_wins += 1
        elif result == BattleResult(3):
            draw += 1
        
    print("attacker wins: ", attacker_wins, f"({round((attacker_wins/num_simulations)*100,2)}%)")
    print("defender wins: ", defender_wins,  f"({round((defender_wins/num_simulations)*100,2)}%)")
    print("Draws: ", draw,  f"({round((draw/num_simulations)*100,2)}%)")


if __name__ == "__main__":
    # List of method names as strings
    attaker_list = [ 'dreadnauht', 'fighter']
    attaker_fleet = Fleet(attaker_list)

    defender_list = ['destroyer', 'destroyer']
    defender_fleet = Fleet(defender_list)
    
    
    simulate_many_battles(10000,defender_fleet, attaker_fleet )