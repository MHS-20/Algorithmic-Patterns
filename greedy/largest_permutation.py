# given the numbers from 1 to N, and a number K of swap you can make
# interpreting the array as single number, return the maximum number possible
# you can swap also non-adjacent numbers
def largest_permutation(arr, swaps):
    i = 0
    max = len(arr) # max element is arr is N
    pos = {x: i for i, x in enumerate(arr)} # values and their original position

    while swaps and i < len(arr):
        j = pos[max]
        if i == j: # already in the right position
            continue

        swaps =- 1
        arr[i], arr[j] = arr[j], arr[i]
        pos[arr[i]], pos[arr[j]] = pos[arr[j]], pos[arr[i]]
        i += 1
        max -= 1

    return arr

