test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

class Crt:
    def __init__(self):
        self.screen = []
        self.line = []

    def draw(self, pls_draw, symbol = '#'):
        if(pls_draw):
            self.line.append(symbol)
        else:
            self.line.append('.')
        
        if(len(self.line) == 40):
            self.screen.append(self.line)
            self.line = []

    def print_screen(self):
        for p in self.screen:
            print(''.join(p))

class Cpu:
    def __init__(self):
        self.x = 1
        self.current = 1
        self.cycles = {}
        self.crt = Crt()
    
    def get_cycles(self):
        return self.cycles
    
    def cycle(self, amount = 1):
        for i in range(amount):
            if(self.current > 40):
                num = self.current % 40 
            else:
                num = self.current

            if(num == self.x or num == self.x + 1 or num == self.x + 2):
                self.crt.draw(True)
            else: 
                self.crt.draw(False)

            self.cycles[self.current] = self.x
            self.current += 1
    
    def addx(self, num):
        self.cycle(2)
        self.x += num
    
    def noop(self):
        self.cycle()
    
    def print_screen(self):
        self.crt.print_screen()

def part_1_and_2():
    cpu = Cpu()
    lines = get_lines(False)
    cycles = cpu.get_cycles()

    for l in lines:
        if l.startswith('addx'):
            cpu.addx(int(l.split(' ')[1]))
        elif l.startswith('noop'):
            cpu.noop()
        else:
            raise Exception('Unknown command: ' + l)

    cycles_wanted = {20, 60, 100, 140, 180, 220}
    totals = []

    for c in cycles_wanted:
        totals.append(c * cycles[c])

    print(f"Part 1 --- {sum(totals)}")
    print(f"Part 2 ---------------------------------")
    cpu.print_screen()

part_1_and_2()