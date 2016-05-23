# A program to act as a diplomacy judge written in Python
# We will stat with Pure.
# Pure Diplomacy utilizes a map that consists of 7 territories, each a home territory of the 7 powers
# There are only armies
# All spaces connect to all other spaces

def UpdateMap():
    print("Map has been updated")

# MapFleets = []
def AddImplicitHolds(units, orders):
    for x in range(len(units)):
        ordersFound = False
        for s in range(len(orders)):
            if orders[s][0] == units[x][0]:
                ordersFound = True
                break
        if ordersFound == False:
            orders.append([units[x][0], "HOLDS", [units[x][0], "HOLDS", units[x][0]]])

def AddStrengthScorePlace(orders):
    strength = 1
    leng = len(orders)
    for x in range(leng):
        orders[x].append(strength)

def AddStrengths(moves, supports):
    for s in supports:
        for m in moves:
            if s[2] == m[2]:
                m[3] += 1

MapArmies = [
    ['LON', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['PAR', ['LON', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['VEN', ['PAR', 'LON', 'MUN', 'MOS', 'BUD', 'ANK']],
    ['MUN', ['PAR', 'VEN', 'LON', 'MOS', 'BUD', 'ANK']],
    ['MOS', ['PAR', 'VEN', 'MUN', 'LON', 'BUD', 'ANK']],
    ['BUD', ['PAR', 'VEN', 'MUN', 'MOS', 'LON', 'ANK']],
    ['ANK', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'LON']]
]

Units =[
    ['LON', 'ENG'],
    ['PAR', 'FRA'],
    ['VEN', 'ITA'],
    ['MUN', 'GER'],
    ['BUD', 'AUS'],
    ['ANK', 'TUR'],
    ['MOS', 'RUS']
]

Orders = [
    ['LON', 'MOVES', ['LON', 'MOVES', 'PARIS']],
    ['VEN', 'SUPPORTS', ['LON', 'MOVES', 'PARIS']],
    ['PAR', 'SUPPORTS', ['MOS', 'HOLDS', 'MOS']],
    ['MUN', 'SUPPORTS', ['PAR', 'HOLDS', 'PAR']],
    ['BUD', 'MOVES', ['BUD', 'MOVES', 'MOS']],
    ['ANK', 'SUPPORTS', ['BUD', 'MOVES', 'MOS']]
]
#print(Orders)
AddImplicitHolds(Units, Orders)
#print(Orders)

MoveOrders = []
SupportOrders = []
HoldOrders = []

for each in Orders:
    if each[1] == 'MOVES':
        MoveOrders.append(each)
    if each[1] == 'SUPPORTS':
        SupportOrders.append(each)
    if each[1] == 'HOLDS':
        HoldOrders.append(each)

AddStrengthScorePlace(MoveOrders)
AddStrengthScorePlace(SupportOrders)
AddStrengthScorePlace(HoldOrders)
AddStrengths(MoveOrders, SupportOrders)
AddStrengths(HoldOrders, SupportOrders)
print(MoveOrders)
print(HoldOrders)

#AddStrengths(HoldOrders, SupportOrders)

#print(SupportOrders)
#print(HoldOrders)

#AddStrengths(MoveOrders, SupportOrders)


