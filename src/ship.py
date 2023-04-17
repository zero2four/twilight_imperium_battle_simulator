import random



class Fleet:
    ship_list = []
    destroyed: bool


    def __init__(self,ship_type_list):
        self.ship_list = []
        self._make_ship_list(ship_type_list)
        self._sort_ship_list()
        self.destroyed = self._is_fleet_destroyed()
        
        
    def _make_ship_list(self, ship_type_list):

        for ship_type in ship_type_list:
            ship_obj = Ship()
            # Get reference to method by ship_type
            method_ref = getattr(ship_obj, ship_type) 
            # Call the method, create and appende returende ship
            self.ship_list.append(method_ref())
    
    def _sort_ship_list(self):
        self.ship_list.sort(key=lambda ship: (ship.sustain_damage, ship.rank))
        
        
    def _is_fleet_destroyed(self)-> bool:
        if not self.ship_list:
            #print("Fleet destroyed!")
            self.destroyed = True
            return True
        
        return False
    
    def distribute_hits(self, hits:int):
        while hits > 0:
            # test if list is empty

            if self._is_fleet_destroyed():
                
                break
                
            target = self.ship_list[-1]
            
            if target.sustain_damage:
                target.sustain_damage = False
                self._sort_ship_list()
                
                #print(f"hit sustained by {target.ship_type}")
            else:
                self.ship_list.pop()
                #print(f"{target.ship_type} destroyed")
                if self._is_fleet_destroyed():
                    break
  
            hits -= 1
            
    def produce_hits(self):
        hits = 0
        for ship in self.ship_list:
            hits += ship.roll_for_hit()
            
        return hits
    
        
        
class Ship:
    ship_type: str = None
    rank: int = None # lower is better
    hit_on: int = None
    attacks = None
    sustain_damage: bool = None

    def __init__(self, ship = None): 
        if ship is not None:
            self.ship_type = ship.ship_type
            self.attacks = ship.attacks
            self.hit_on: int = ship.hit_on
            self.sustain_damage: bool = ship.sustain_damage
            self.rank: int = ship.rank

    def destroyer(self):
        self.ship_type = "Destroyer"
        self.rank = 7
        self.attacks = 1
        self.hit_on = 9
        self.sustain_damage = False

        return Ship(self)

    def dreadnauht(self):
        self.ship_type = "Dreadnauht"
        self.rank = 3
        self.attacks = 1
        self.hit_on = 5
        self.sustain_damage = True
 
        return Ship(self)


    def roll_for_hit(self):
        """
        Roll for a hit based on the ship's hit probability.

        Returns:
            bool: True if the hit is successful, False otherwise.
        """
        hits = 0
        for i in range(0,self.attacks):
            if random.randint(1, 10) >= self.hit_on:
                hits+= 1
        
        return hits


