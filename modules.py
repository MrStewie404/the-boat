import messages
from random import choices, randint as rand

class Board:
    def __init__(self, size: int = 6):
        self.size = int(size)
        self.map = None

    def create_map(self) -> list:
        """Создание карты на основе заданных параметров"""
        map = []
        for y in range(self.size):
            map.append([])
            for x in range(self.size):
                map[y].append("O")

        return map
    
    def place_ships(self, ships):
        map = self.create_map()

        text = ''
        ship = '■'
        for ship_ship in ships:
            for squares in ship_ship:
                text += f"{ship}"
            text += f"\n"

        for line in range(len(map)):
            for element in range(len(map[line])):
                for ship_ship in ships:
                    for squares in ship_ship:
                        if line == squares[0]-1 and element == squares[1]-1:
                            map[line][element] = ship

        return map

    def update_map(self, map):
        """Обновление карты"""
        self.map = map

    def __str__(self):
        """Строковое представление объекта"""
        string_image = []

        # Создание горизонтальной строки
        horizontal_string = '  |'
        for element in range(len(self.map[1])):
            horizontal_string += f' {element+1} |'

        # Создание поля в виде строк в массивах
        string_image = f'{horizontal_string}\n'
        for line in range(len(self.map)):
            string_image += f'{line+1} |'
            for pos in range(len(self.map)):
                string_image += f" {self.map[line][pos]} |"
            string_image += '\n'

        return string_image


class Ship:
    def __init__(self, size:int = 6):
        self.size = size

    def constructor(self):
        size = self.size
        ship = '■'

        coordinates = [[[1, 1], [1, 2], [1, 3]], 
                       [[2, 4], [2, 5]],
                       [[4, 5], [5, 5]],
                       [[4, 1]], [[4, 3]], [[6, 1]], [[6, 3]]
                    ]

        return coordinates

class CheckError:
    def __init__(self):
        pass

    def check_input(self, user_input, mode):

        if mode == 'position':
            if len(user_input.split()) != 2:
                print(messages.error_len)
                return False

            if any(char.isalpha() for char in user_input):
                print(messages.error_of_pos)
                return False
            
            for i in user_input.split():
                if int(i) < 1 or 6 < int(i):
                    print(messages.error_len)
                    return False


class Player:
    def __init__(self, name, map):
        self.name = name
        self.map = map
        self.score = 0
        self.misses = 0

    def score_upper(self):
        self.score += 1
        return self.score
    
    def misses_upper(self):
        self.misses += 1
        return self.misses
    

class Computer:
    def __init__(self, map):
        self.map = map
        self.score = 0
        self.misses = 0
        self.memory_fire = set()

    def create_attack(self):
        """Генерация координаты выстрела"""
        while True:
            attack_position = (rand(0, 5), rand(0, 5))

            if attack_position not in self.memory_fire:
                self.memory_fire.add(attack_position)
                return f"{attack_position[0]} {attack_position[1]}"
    
    def score_upper(self):
        self.score += 1
        return self.score
    
    def misses_upper(self):
        self.misses += 1
        return self.misses


class System:
    def __init__(self, player_one: str, player_two = "Компьютер"):
        self.player_one = player_one
        self.player_two = player_two
        self.dict_player = {1: player_one, 2: player_two}
        self.who_player = player_two

    def queue(self, who_player):
        """Позволяет играть по-очереди"""
        if who_player == self.player_one:
            self.who_player = self.dict_player.get(2)

        elif who_player == self.player_two:
            self.who_player = self.dict_player.get(1)

        return f'Ход делает {self.who_player}'

    def reg_attack(self, map, user_input):
        """Проверяет попадание в цель"""
        user_input = user_input.split()
        element = map[int(user_input[0])-1][int(user_input[1])-1]

        if element == '■':
            map[int(user_input[0])-1][int(user_input[1])-1] = 'X'
            print(f"Игрок {self.who_player} попал!")
        elif element == 'O':
            print(f"Игрок {self.who_player} промахнулся...")
            map[int(user_input[0])-1][int(user_input[1])-1] = 'T'
        else:
            print(f"Игрок {self.who_player} промахнулся...")

        Board().update_map(map)
        # print(Board)
            
        
    def check_ships(self, map):
        """Проверяет существование кораблей"""
        exist = 0
        for line in map:
            if '■' in line:
                exist += 1
        if exist == 0:
            print(f"Игрок {self.who_player} победил!")
            return False
            

class ImprovedTerminal:
    def __init__(self):
        import os
        self.os = os

    def clear_terminal(self):
        """Очистка окна терминала"""
        if self.os.name == 'nt':
            self.os.system('cls')
        else:
            self.os.system('clear')


if __name__ == '__main__':
    ships = Ship().constructor()
    map = (Board(6).place_ships(ships))
    map = Board().output_image(map=map)

    print(map)