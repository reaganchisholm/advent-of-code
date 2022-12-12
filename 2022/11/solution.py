import math

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""" 


def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n\n")
            return lines

class Monkey:
    def __init__(self, number, starting_items, operation, test, pass_test_throw, fail_test_throw, worry_divisible = True):
        self.number = number 
        self.items = starting_items
        self.items_inspected = 0
        self.operation_string = operation
        self.pass_test_throw = pass_test_throw
        self.fail_test_throw = fail_test_throw
        self.test_string = test
        self.worry_divisible = worry_divisible 
    
    def get_inspected_items(self):
        return self.items_inspected

    def inspect_all_items(self):
        copy_of_items = self.items.copy()
        for item in copy_of_items:
            self.inspect(item)

    def inspect(self, item):
        self.items_inspected += 1
        testing_item = self.items.pop(0)
        new_value = self.operation(testing_item)
        self.test(new_value)
        
    def operation(self, item):
        old = item
        new_value = eval(self.operation_string)
        if(self.worry_divisible):
            new_value = math.floor(new_value / 3)
        else:
            lcm = math.lcm(3, 13, 2, 11, 5, 17, 19, 7) # hard coded for solution
            new_value = math.floor(new_value) % lcm
                
        return new_value
    
    def test(self, new_value):
        op, _, amount = self.test_string.split(" ")

        if op == "divisible":
            outcome = new_value % int(amount) == 0

            if(outcome):
                self.throw(new_value, self.pass_test_throw)
            else: 
                self.throw(new_value, self.fail_test_throw)
        else:
            print("Unknown test: " + self.test_string)
    
    def throw(self, new_value, monkey):
        monkeys[int(monkey)].receive(new_value)
    
    def receive(self, item):
        self.items.append(item)
    
def part_1():
    global monkeys
    lines = get_lines(False)
    monkeys = []

    for i, line in enumerate(lines):
        global starting_items
        global operation
        global test
        global pass_test_throw
        global fail_test_throw

        starting_items = []
        operation = ""
        test = ""
        pass_test_throw = ""
        fail_test_throw = ""

        for j in line.splitlines():
            sl = j.strip()
            if(sl.startswith("Starting items:")):
                starting_items = list(map(int, j.split(": ")[1].split(", ")))
                continue
            elif(sl.startswith("Operation:")):
                operation = j.split("= ")[1]
                continue
            elif(sl.startswith("Test:")):
                test = j.split(": ")[1]
                continue
            elif(sl.startswith("If true:")):
                pass_test_throw = j.split(" ")[-1]
                continue
            elif(sl.startswith("If false:")):
                fail_test_throw = j.split(" ")[-1]
                continue
            else:
                continue

        monke = Monkey(i, starting_items, operation, test, pass_test_throw, fail_test_throw)
        monkeys.append(monke)

    for r in range(20):
        for m in monkeys:
            m.inspect_all_items()
        
    totals_inspected = []
    
    for i, m in enumerate(monkeys):
        totals_inspected.append(m.get_inspected_items())
    
    totals_inspected.sort(reverse=True)
    print(f"Part 1 --- {totals_inspected[0] * totals_inspected[1]}")

def part_2():
    global monkeys
    lines = get_lines(False)
    monkeys = []

    for i, line in enumerate(lines):
        global starting_items
        global operation
        global test
        global pass_test_throw
        global fail_test_throw

        starting_items = []
        operation = ""
        test = ""
        pass_test_throw = ""
        fail_test_throw = ""

        for j in line.splitlines():
            sl = j.strip()
            if(sl.startswith("Starting items:")):
                starting_items = list(map(int, j.split(": ")[1].split(", ")))
                continue
            elif(sl.startswith("Operation:")):
                operation = j.split("= ")[1]
                continue
            elif(sl.startswith("Test:")):
                test = j.split(": ")[1]
                continue
            elif(sl.startswith("If true:")):
                pass_test_throw = j.split(" ")[-1]
                continue
            elif(sl.startswith("If false:")):
                fail_test_throw = j.split(" ")[-1]
                continue
            else:
                continue

        monke = Monkey(i, starting_items, operation, test, pass_test_throw, fail_test_throw, False)
        monkeys.append(monke)

    for r in range(10000):
        for m in monkeys:
            m.inspect_all_items()
        
    totals_inspected = []
    
    for i, m in enumerate(monkeys):
        totals_inspected.append(m.get_inspected_items())
    
    totals_inspected.sort(reverse=True)
    print(f"Part 2 --- {totals_inspected[0] * totals_inspected[1]}")

part_1()
part_2()