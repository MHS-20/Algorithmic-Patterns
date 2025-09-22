# given two array of positions, one of mice and one of holes, of the same length
# find the minimum time after which all mice have reached a hole
# count time as difference in position

def mth(mice, holes):
    mice.sort()
    holes.sort()

    ans = 0
    for a, b in zip(mice, holes):
        ans = max(ans, abs(b-a))
