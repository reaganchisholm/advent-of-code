from enum import IntEnum
from itertools import groupby
from collections import defaultdict

test_input="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
JK22J 471"""

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
    grouped_hands = defaultdict(list)
    hands = []

    for l in lines:
        hand, bid = l.split()
        hand_rank = determine_hand(hand)
        hands.append({
            'hand_rank': hand_rank,
            'hand': hand,
            'bid': int(bid)
        })
    
    for hand_info in hands:
        grouped_hands[hand_info['hand_rank']].append(hand_info)

    grouped_hands = dict(sorted(grouped_hands.items(), key=lambda x: x[0], reverse=True))

    sorted_hands = []
    for rank in sorted(grouped_hands.keys()):
        sorted_group = sorted(grouped_hands[rank], key=hand_sort_key, reverse=False)
        sorted_hands.extend(sorted_group)

    totals = []
    for i,h in enumerate(sorted_hands):
        totals.append(h['bid'] * (i + 1))

    print(f"Part 1 --- {sum(totals)}")

def part_2():
    lines = get_lines(False)
    grouped_hands = defaultdict(list)
    hands = []

    for l in lines:
        hand, bid = l.split()
        hand_rank = determine_hand(hand, True)
        hands.append({
            'hand_rank': hand_rank,
            'hand': hand,
            'bid': int(bid)
        })
    
    for hand_info in hands:
        grouped_hands[hand_info['hand_rank']].append(hand_info)

    grouped_hands = dict(sorted(grouped_hands.items(), key=lambda x: x[0], reverse=True))
    sorted_hands = []

    for rank in sorted(grouped_hands.keys()):
        sorted_group = sorted(grouped_hands[rank], key=hand_sort_key_p2, reverse=False)
        sorted_hands.extend(sorted_group)
    
    totals = []
    for i,h in enumerate(sorted_hands):
        totals.append(h['bid'] * (i + 1))

    print(f"Part 2 --- {sum(totals)}")

def determine_hand(hand, handle_joker = False):
    sorted_hand = ''.join(sorted(hand))
    grouped_cards = [''.join(g) for _, g in groupby(sorted_hand)];

    if handle_joker:
        if 'J' in hand:
            joker_count = hand.count('J')
            if len(grouped_cards) == 2 or len(grouped_cards) == 1:
                return Hand.FIVE_OF_A_KIND
            elif len(grouped_cards) == 3:
                if len(grouped_cards[0]) == 3 or len(grouped_cards[1]) == 3 or len(grouped_cards[2]) == 3:
                    return Hand.FOUR_OF_A_KIND
                elif joker_count == 1:
                    return Hand.FULL_HOUSE
                else:
                    return Hand.FOUR_OF_A_KIND
            elif len(grouped_cards) == 4: 
                return Hand.THREE_OF_A_KIND
            elif len(grouped_cards) == 5:
                return Hand.ONE_PAIR
            else:
                print("Unhandled wildcard hand")
                
    if len(grouped_cards) == 1:
        return Hand.FIVE_OF_A_KIND

    if len(grouped_cards) == 5:
        return Hand.HIGH_CARD

    elif len(grouped_cards) == 2:
        if len(grouped_cards[0]) == 4 or len(grouped_cards[1]) == 4:
            return Hand.FOUR_OF_A_KIND
        else:
            return Hand.FULL_HOUSE

    elif len(grouped_cards) == 3:
        if len(grouped_cards[0]) == 3 or len(grouped_cards[1]) == 3 or len(grouped_cards[2]) == 3:
            return Hand.THREE_OF_A_KIND
        else:
            return Hand.TWO_PAIR

    elif len(grouped_cards) == 4:
        return Hand.ONE_PAIR
    
    else:
        print("Unknown hand")
        return -1

def hand_sort_key(hand_info):
    order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return tuple(order[card] for card in hand_info['hand'])

def hand_sort_key_p2(hand_info):
    order = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
    return tuple(order[card] for card in hand_info['hand'])
    
# Strongest to weakest
class Hand(IntEnum):
    FIVE_OF_A_KIND = 7 # AAAAA
    FOUR_OF_A_KIND = 6 # AA8AA
    FULL_HOUSE = 5 # 23332
    THREE_OF_A_KIND = 4 # TTT98
    TWO_PAIR = 3 # 23432
    ONE_PAIR = 2 # A23A4
    HIGH_CARD = 1 # 23456

part_1()
part_2()