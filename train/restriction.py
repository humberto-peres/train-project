from train.exceptions import ConstraintViolationException

class Restriction:
    def validateMovements(self, commands):
        if len(commands) > 50:
            raise ConstraintViolationException("O trem não pode se mover mais de 50 posições.")
        
        previousDirection = commands[0]
        count = 0

        for command in commands:
            if command == previousDirection:
                count += 1
                if count > 20:
                    raise ConstraintViolationException("O trem não pode fazer mais de 20 movimentos consecutivos na mesma direção.")
            else:
                previousDirection = command
                count = 1
                