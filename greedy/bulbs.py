# given N bulbs, 1 is ON, 0 is OFF
# turning a bulb on, cause all bulbs to the right to flip
# find the min number of switches to turn all bulb on

def bubls(arr):
    cost = 0
    for b in arr: 
        if cost % 2 != 0:
            b = not b

        if b % 2 != 0:
            cost += 1

    return cost
