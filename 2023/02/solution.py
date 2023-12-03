test_input="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(False)
    possible_games = [] 
    possible_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    current_game = 1

    for l in lines:
        l = l.split(': ')[1]
        games = [i.strip() for i in l.split(';')]
        is_possible = True
        for g in games:
            cubes = g.split(',')
            if(is_possible == False):
                break
            for c in cubes:
                c = c.strip()
                amount, color = c.split(' ')
                amount = int(amount)
                if amount > possible_cubes[color]:
                    is_possible = False
                    break
        
        if is_possible:
            possible_games.append(current_game)
        current_game += 1
    
    answer = sum(possible_games)
    print(f"Part 1 --- {answer}")

def part_2():
    lines = get_lines(False)
    game_powers = []

    for l in lines:
        l = l.split(': ')[1]
        games = [i.strip() for i in l.split(';')]
        min_needed = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        for g in games:
            cubes = g.split(',')
            for c in cubes:
                c = c.strip()
                amount, color = c.split(' ')
                amount = int(amount)
                if amount > min_needed[color] or min_needed[color] == 0:
                    min_needed[color] = amount

        power = 1
        for key, value in min_needed.items():
            power *= value
        game_powers.append(power)
    
    answer = sum(game_powers)
    print(f"Part 2 --- {answer}")

part_1()
part_2()
