# given a row of seats, occupied (X) or free (.)
# find the minimum number of moves to put all people together

def moving_seats(arr): 
    # indexes of crosses
    crosses = [i for i, c in enumerate(arr) if c == "x"]

    n = len(crosses)
    if n == 0: return 0

    mid = crosses[len(crosses)//2]
    return sum(abs(cross - mid) for cross in crosses)

