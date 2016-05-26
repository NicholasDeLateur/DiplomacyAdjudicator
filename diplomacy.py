from collections import OrderedDict

import testImport

import diplomacyTests

import diplomacyUtilities


class Game:
    def __init__(self):
        self.name = ''
        self.powers = dict() #Perhaps could also be called/thought of as the players
        self.territories = dict() #All the territories in the game, the key is the name of the territory, value is actual object

    def __repr__(self):
        return 'String Rep of Game:' \
               + self.name + '\n' \
               + '\nTerritories:' + '\n' + diplomacyUtilities.makeSortedStringRepOfDict(self.territories) \
               + '\n Powers: \n' + diplomacyUtilities.makeSortedStringRepOfDict(self.powers) \


    def addPower(self, power_name):
        power = Power()
        power.name = power_name
        self.powers[power_name] = power

    def createTerritoriesFromList(self,territories_list):
        for next_territory in territories_list:
            new_territory = Territory()
            new_territory.name = next_territory[0]
            for next_neighbor in next_territory[1]:
                new_territory.neighbor_names.append(next_neighbor)
            self.territories[next_territory[0]] =new_territory


    def createPowersWithUnitsFromList(self,powers_and_units_list):
        for next_power in powers_and_units_list:
            new_power = Power()
            new_power.name = next_power[0]
            for next_territory in next_power[1]:
                new_power.territory_names.append(next_territory[0])
                if(next_territory[1] != 'None'):
                    new_unit = Unit()
                    new_unit.territory_name = next_territory[0]
                    new_unit.type = next_territory[1]
                    new_power.units.append(new_unit)
            self.powers[new_power.name] = new_power

class Power:
    def __init__(self):
        self.name = ''
        self.territory_names = [] #Just the names of territories currently owned by this power.  Is key for looking up territory in game.territories
        self.units = [] #Units are always owned by a power

    def addUnit(self, type, territory):
        unit = Unit()
        unit.type = type
        unit.territory = territory

    def __repr__(self):
        return self.name + '\n\t' + '\n\t'.join(self.territory_names) +'\n\t' +'\n\t'.join(map(str,self.units))


class Territory:
    def __init__(self):
        self.name = ''
        self.neighbor_names = [] #Names of territories that are neighbors of this territory
        self.is_a_supply_center = False

    def __repr__(self):
        return self.name + '\n\t' + '\n\t'.join(self.neighbor_names)


class Unit:
    def __init__(self):
        self.territory_name = None #Name of territory this unit is currently in
        self.order = None
        self.type = None #Army or fleet are the types


    def __repr__(self):
        return self.type  + ' in ' + self.territory_name

class Order:
    def _init_(self):
        self.order_type = None
        self.move_to = None #If type is move, this is name of territory moving to
        self.hold_support_target = None #If type is hold support, name of territory that is being supported
        self.move_support_who_supported = None #If type is move support, name of territory that supported unit is currently in
        self.move_support_target = None #If type is move support name of territory that supported unit is moving to


def main ():
    testGame = diplomacyTests.createTestGame()

    print(testGame)
    testImport.printHello()

if __name__ == "__main__":
    main ()



