import sys
from collections import defaultdict
import math
from dataclasses import dataclass

from functools import cmp_to_key
import re

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
labels2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def distribution(cards):
    d = defaultdict(int)
    for c in cards:
        d[c] = d[c] + 1
    return sorted(list(d.values()), reverse=True)

def distribution2(cards):
    jokers = cards.count('J')
    l = distribution(cards.replace("J", ""))
    if not l:
        l.append(5) #full of jokers
    else:
        l[0] = l[0] + jokers
    return l

def compare(cards1, cards2):
    d1 = distribution(cards1)
    d2 = distribution(cards2)
    
    if d1 == d2:
        for i in range(0, len(cards1)):
            if cards1[i] == cards2[i]:
                continue
            return 1 if labels.index(cards1[i]) < labels.index(cards2[i]) else -1
    else:
        if d1[0] != d2[0]:
            return d1[0] - d2[0]
        return d1[1] - d2[1]

def compare2(cards1, cards2):
    d1 = distribution2(cards1)
    d2 = distribution2(cards2)
    
    if d1 == d2:
        for i in range(0, len(cards1)):
            if cards1[i] == cards2[i]:
                continue
            return 1 if labels2.index(cards1[i]) < labels2.index(cards2[i]) else -1
    else:
        if d1[0] != d2[0]:
            return d1[0] - d2[0]
        return d1[1] - d2[1]

def task1(): 
    file1 = open('input7.txt', 'r')
    Lines = file1.readlines()

    deal = dict()

    for line in Lines:
        cards, bet = line.split(" ")
        deal[cards] = int(bet)

    sum = 0
    for i, c in enumerate(sorted(list(deal.keys()), key=cmp_to_key(compare))):
        sum += (i+1)*deal[c]
        
    print(sum)

    sum = 0
    for i, c in enumerate(sorted(list(deal.keys()), key=cmp_to_key(compare2))):
        sum += (i+1)*deal[c]
        
    print(sum)

def main() -> int:
    task1()

if __name__ == '__main__':
    sys.exit(main())


