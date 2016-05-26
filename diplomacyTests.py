import diplomacy

def createTestGame():
    territory_list = [
        ['LON', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
        ['PAR', ['LON', 'VEN', 'MUN', 'MOS', 'BUD', 'ANK']],
        ['VEN', ['PAR', 'LON', 'MUN', 'MOS', 'BUD', 'ANK']],
        ['MUN', ['PAR', 'VEN', 'LON', 'MOS', 'BUD', 'ANK']],
        ['MOS', ['PAR', 'VEN', 'MUN', 'LON', 'BUD', 'ANK']],
        ['BUD', ['PAR', 'VEN', 'MUN', 'MOS', 'LON', 'ANK']],
        ['ANK', ['PAR', 'VEN', 'MUN', 'MOS', 'BUD', 'LON']]
    ]

    powers_list = [
        ['Austria', [['LON', 'Army'], ['BUD', 'Army']]],
        ['France', [['PAR', 'Army'], ['MOS','None'],['VEN','Army']]]
    ]

    order_list = [
        ['LON','Hold'],
        ['BUD','Move',          'MOS'],
        ['PAR','Hold_Support',  'MOS'],
        ['VEN','Move_Support',  'BUD', 'MOS']
    ]

    testGame = diplomacy.Game()

    testGame.name ='Test Game'

    testGame.createTerritoriesFromList(territory_list)

    testGame.createPowersWithUnitsFromList(powers_list)

    return testGame

def main ():
    print('diplomacyTests is main')

    testGame = createTestGame()

    print(testGame)

if __name__ == "__main__":
    main ()


