from train.movement import Movement
from train.restriction import Restriction
from train.exceptions import InvalidCommandException

class Train:
    def __init__(self):
        self.position = 0
        self.movement = Movement()
        self.restriction = Restriction()
    
    def printTrain(self):
        trainArt = """
            .---- -  -
           (   ,----- - -
            \_/      ___
          c--U---^--'o  [_
          |------------'_|  PARTIU!!!
         /_(o)(o)--(o)(o)
     ~~~~~~~~~~~~~~~~~~~~~~~~
        """
        print(trainArt)

    def printPepe(self):
        pepeArt = """
⠀⠀⠀⣀⡤⠤⣤⣤⡤⠤⠒⢤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡶⢋⣝⣾⠁⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⠋⢺⠏⠛⠆⠀⢈⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠟⡀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⠟⠁⠀⠙⠭⠉⠀⠀⠈⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢛⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⡀⠀⢘⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⣧⠀⠀⠀⠀⠀⠀⠀⣠⠟⠋⠉⢻⣏⠀⢉⠛⠲⣤⡀⠀⠀⠀⠀⠀
 ⢿⣿⣷⠆ ⠰⠒⠋⠁   ⣸⣏⡇⠘⡆ ⢀⣷⡄  O TREM NÃO PARTIU
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⡏⠀⢣⠀⠸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⡆⢱⠀⠈⢒⡆⠈⣽⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣧⢾⣽⣾⡀⡾⣝⣡⡴⣿⣶⡒⢶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣥⠈⠉⠻⠋⠀⡽⠋⠉⠉⢲⡍⠉⠁⣸⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣏⠀⠀⠀⠀⣇⠀⢀⠖⢉⠤⣄⣴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠂⠤⠚⠀⠈⠒⠚⠚⠉⠀⠀⠀⠀⠀⠀⠀
        """

        print(pepeArt)

    def execute(self, commands):
        for command in commands:
            if command not in ['1', '2']:
                raise InvalidCommandException(f"Comando inválido '{command}'")
        
        self.restriction.validateMovements(commands)
        route = [self.position]

        for command in commands:
            if command == '1':
                self.position += self.movement.moveLeft()
            elif command == '2':
                self.position += self.movement.moveRight()
            route.append(self.position)
        
        return self.position, route

    