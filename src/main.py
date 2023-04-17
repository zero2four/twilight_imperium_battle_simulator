from ship import Ship, Fleet




# List of method names as strings
attaker_list = [ 'dreadnauht', 'fighter']
attaker_fleet = Fleet(attaker_list)

defender_list = ['destroyer', 'destroyer']
defender_fleet = Fleet(defender_list)
    

print("attakers:", attaker_list)
print("defenders:", defender_list)


def simulate_battle(defender_fleet, attaker_fleet):
    battle_round = 0
    while not defender_fleet.destroyed and not attaker_fleet.destroyed:

        defender_hits = defender_fleet.produce_hits()
        attaker_hits = attaker_fleet.produce_hits()
        
        defender_fleet.distribute_hits(attaker_hits)
        attaker_fleet.distribute_hits(defender_hits)
        
        if defender_fleet.destroyed and attaker_fleet.destroyed:
            return "DRAW"
            
        if defender_fleet.destroyed:
            return "ATTACKER WIN"
            
        if attaker_fleet.destroyed:
            return "DEFENDER WIN"

    
        battle_round += 1
        if battle_round > 100:
            print("error")
            break

attacker_wins = 0
defender_wins = 0
draw = 0

simulations = 10000

for i in range(0,simulations,1):
    attaker_fleet = Fleet(attaker_list)
    defender_fleet = Fleet(defender_list)
    
    result = simulate_battle(defender_fleet, attaker_fleet)
    if result == "ATTACKER WIN":
        attacker_wins += 1
    elif result == "DEFENDER WIN":
        defender_wins += 1
    elif result == "DRAW":
        draw += 1
        
print("attacker wins: ", attacker_wins, f"({round((attacker_wins/simulations)*100,2)}%)")
print("defender wins: ", defender_wins,  f"({round((defender_wins/simulations)*100,2)}%)")
print("Draws: ", draw,  f"({round((draw/simulations)*100,2)}%)")


