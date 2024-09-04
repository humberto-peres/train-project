from train.train import Train
import os
import time

def main():
    os.system("cls")
    train = Train()
    commands = []
    traveledPositions = [0]

    while True:
        os.system("cls")
        print("""
  _____ ___ ___ __  __     _  _   _ _____ ___  _  _  ___  __  __  ___  
 |_   _| _ \ __|  \/  |   /_\| | | |_   _/ _ \| \| |/ _ \|  \/  |/ _ \ 
   | | |   / _|| |\/| |  / _ \ |_| | | || (_) | .` | (_) | |\/| | (_) |
   |_| |_|_\___|_|  |_| /_/ \_\___/  |_| \___/|_|\_|\___/|_|  |_|\___/ 
        
        [1] - Mover o trem para ESQUERDA
        [2] - Mover o trem para DIREITA
        [0] - Parar o trem
        """)
        direction = input("\tOpção: ").upper()

        if direction == '0':
            break
        
        if direction not in ['1', '2']:
            print(f"\tErro: Comando inválido '{direction}'. Use 1 para ESQUERDA ou 2 para DIREITA.")
            time.sleep(1)
            continue
        
        if direction  in ['1', '2']:
            direction_str = "Esquerda" if direction == '1' else "Direita"
            print(f"\tVocê virou para a {direction_str}.")
            time.sleep(1)

        commands.append(direction)
    
    try:
        if direction == '0' and len(commands) > 0:
            endPosition, route = train.execute(commands)
            traveledPositions.extend(route)
            print(f"\tPosição final do trem: {endPosition}")
            train.printTrain()
        else:
            train.printPepe()
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
