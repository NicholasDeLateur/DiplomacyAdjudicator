# A program to act as a diplomacy judge written in Python
# We will stat with Pure.
# Pure Diplomacy utilizes a map that consists of 7 territories, each a home territory of the 7 powers
# There are only armies
# All spaces connect to all other spaces

import math

class Unit:
    pass
    def __init__(self):
        self.type = ''
        self.location = ''
        self.power = ''
        self.order = ''
        self.attack = 1
        self.defense = 1
        self.moving = True
    def PrintInfo(self):
        print("This unit is the", self.power, self.type, "at", self.location)

def DetermineWhetherHolding(units):
    for x in units:
        if x.order[1] != 'MOVES':
            x.moving = False

def DetermineCuts(units):
    for x in units: # for each unit
        for y in units: # check it against each other unit
            if x.moving == True and x.order[2][2]== y.location: # if the unit is moving
                if y.moving == False and y.order[2][2] != x.location: # can't cut a support against yourself!
                    y.order = [y.location, "HOLDS", [y.location, "HOLDS", y.location]]

def AddSupportStrengths(units, orders):
    for FindSupporter in units:
        for Supported in units:
            if FindSupporter.order[1] == 'SUPPORTS' and Supported.location == FindSupporter.order[2][0]:
                # Now that we have found a match we need to know if it's supporting a move or a hold
                if Supported.moving == True and Supported.order[2] == FindSupporter.order[2]:
                    Supported.attack += 1
                if Supported.moving == False and FindSupporter.order[2][1] == 'HOLDS':
                    Supported.defense += 1

# List of territory connections that an army would see. This needs to be hard coded for each map individually
MapArmies = [
    ['LON', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['PAR', ['LON', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['VEN', ['PAR', 'LON', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['MUN', ['PAR', 'VEN', 'LON', 'MOS', 'BUD', 'ANK']],
    ['MOS', ['PAR', 'VEN', 'MUN', 'LON', 'BUD', 'ANK']],
    ['BUD', ['PAR', 'VEN', 'MUN', 'MOS', 'LON', 'ANK']],
    ['ANK', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'LON']]
]

Units = []
# Starting units. This needs to be hard coded for each map individually
A1 = Unit()
A1.location = 'BUD'
A1.power = 'AUS'
A1.type = 'Army'
E1 = Unit()
E1.location = 'LON'
E1.power = 'ENG'
E1.type = 'Army'
F1 = Unit()
F1.location = 'PAR'
F1.power = 'FRA'
F1.type = 'Army'
G1 = Unit()
G1.location = 'MUN'
G1.power = 'GER'
G1.type = 'Army'
I1 = Unit()
I1.location = 'VEN'
I1.power = 'ITA'
I1.type = 'Army'
R1 = Unit()
R1.location = 'MOS'
R1.power = 'RUS'
R1.type = 'Army'
T1 = Unit()
T1.location = 'ANK'
T1.power = 'TUR'
T1.type = 'Army'
Units.append(A1)
Units.append(E1)
Units.append(F1)
Units.append(G1)
Units.append(I1)
Units.append(R1)
Units.append(T1)

# EXAMPLE set of orders. Theoretically this Order list should take in a new list every turn
Orders = [
    ['LON', 'MOVES', ['LON', 'MOVES', 'PAR']],
    ['VEN', 'SUPPORTS', ['LON', 'MOVES', 'PAR']],
    ['PAR', 'SUPPORTS', ['MOS', 'HOLDS', 'MOS']],
    ['MUN', 'SUPPORTS', ['PAR', 'HOLDS', 'PAR']],
    ['BUD', 'MOVES', ['BUD', 'MOVES', 'MOS']],
    ['ANK', 'MOVES', ['ANK', 'MOVES', 'BUD']],
    ['MOS', 'SUPPORTS', ['ANK', 'MOVES', 'BUD']]
]
# Make a copy of submitted orders so we can manipulate them for computation purposes without loss of record
OrderRecord = Orders
# assign orders to individual units
for x in Units:
    for y in Orders:
        if x.location == y[0]:
            x.order = y

# Start adjudicating!

DetermineWhetherHolding(Units)
DetermineCuts(Units)
AddSupportStrengths(Units, Orders)
