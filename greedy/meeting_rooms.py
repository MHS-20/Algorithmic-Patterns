# given an array of ranges, representing meetings timestamps
# return how many meeting rooms are needed
# eg: maximum number of overlapping intervals
def meeting_rooms(meetings): 
    data = []

    for start, end in meetings:
        data.append((start,+1))
        data.append((end, -1))

    data.sort()

    curr = 0
    ans = 0

    for _, n in data: 
        curr += n
        ans = max(ans, curr)
    return ans
