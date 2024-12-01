import re

test_input=r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

# test_input=r"""broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(True)
    start = lines[0]
    lines = lines[1:]
    modules = {}

    # Setup modules
    for l in lines:
        type, key, output = re.findall(r'([%&])([a-z]+) -> ([a-z]+(?:, [a-z]+)*)', l)[0]

        if(type == '&'):
            inc = {}
        else :
            inc = 0

        modules[key] = {
            "key": key,
            "type": type,
            "output": output.split(", "),
            "status": 0,
            "inc": inc,
            "out": 0 
        }
    
    queue = [{
        "key": 'broadcaster',
        "type": "broadcaster",
        "output": start.split(" -> ")[1].split(', '),
        "status": 0,
        "inc": None,
        "out": 0
    }]

    pulses = [0, 0]
    while queue:
        next = queue.pop(0)
        send_pulse = next["out"]
        # % is flip flop, initiall off, if high pusle comes, it ignores it, if low pulse comes it flips, off->on send high pulse, on->off send low pulse

        # & conjuction remember the last type of pulse sent, if all inputs are high, sends low pulse, if any input is low, sends high pulse

        # Add handling for % and &
        if next["type"] == '%':
            if(next["inc"] == 0): 
                if next["status"] == 0:
                    modules[next["key"]]['status'] = 1
                    send_pulse = 1
                elif next["status"] == 1:
                    modules[next["key"]]['status'] = 0
                    send_pulse = 0
            else: 
                send_pulse = None
        elif next["type"] == '&':
            if all(next["inc"].values()):
                send_pulse = 0
            else:
                send_pulse = 1

        if send_pulse == 0:
            pulses[0] += 1
        elif send_pulse == 1:
            pulses[1] += 1

        if send_pulse != None:
            for o in next['output']:
                print(f"{next['key']} -{send_pulse}-> {modules[o]['key']}")
                if(modules[o]["type"] == '%'):
                    modules[o]["inc"] = send_pulse
                elif(modules[o]["type"] == '&'):
                    modules[o]["inc"][key] = send_pulse
            queue.append(modules[next['output'][0]])
        else:
            print(next)

    print(f"Part 1 --- {pulses}")

part_1()