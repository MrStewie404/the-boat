from modules import *
from time import sleep
cls = ImprovedTerminal().clear_terminal


while True:
    name = str(input('Введите имя игрока\n: '))
    try:
        CheckError = CheckError()
        result = CheckError.check_input(user_input=name, mode = "name")
        if result != False:
            cls(); break
        
    except Exception as e:
        print(e)

board = Board()
map = (Board().place_ships(Ship().constructor()))
System = System(name)
queue = System.queue(name)
Player = Player(name, map)
Computer = Computer(map)


while True:
    board.update_map(map)
    map_image = board.__str__()
    print(f'Поле боя\n{map_image}')
    print(queue)

    if name == queue.split()[2]:
        while True:
            user_input = input(f'{name}, введите точку в которую вы желаете выстрелить\n:')
            result = CheckError.check_input(user_input, mode = 'position')
            if result != False:
                break
        System.reg_attack(Computer.map, user_input)

    else:
        sleep(1)
        user_input = Computer.create_attack()
        System.reg_attack(Player.map, user_input)

    if System.check_ships(map) is False:
        break

    sleep(1)
    queue = System.queue(who_player=queue.split()[2])
    cls()