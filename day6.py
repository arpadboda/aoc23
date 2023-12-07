import sys
from collections import defaultdict
import math
from dataclasses import dataclass

import re

def task1(): 
    file1 = open('input6.txt', 'r')
    Lines = file1.readlines()

    times = []
    records = []

    for line in Lines:
        if not times:
            times = [int(x) for x in re.split(r'\s{1,}', line.split(":")[1].strip())]
        else:
            records = [int(x) for x in re.split(r'\s{1,}', line.split(":")[1].strip())]

    
    sum = 1

    for i in range(0, len(times)):
        cnt = 0
        time = times[i]
        for k in range(1, time):
            if k * (time - k) > records[i]:
                cnt = cnt +1
        sum = sum  * cnt

    print(sum)


def task2():
    file1 = open('input6.txt', 'r')
    Lines = file1.readlines()

    time = 0
    record = 0

    for line in Lines:
        if not time:
            time = int(line.split(":")[1].replace(" ",""))
        else:
            record = int(line.split(":")[1].replace(" ",""))

    print(time)
    print(record)

    sum = 0

    for k in range(1, time):
        if k * (time - k) > record:
            sum = sum + 1

    print(sum)


def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


