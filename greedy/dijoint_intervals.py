# given an array of intervals, return the max number of disjoint internvals

def disjoint(intervals): 
    intervals.sort(key=lambda x:x[1])
    _, prev_end = intervals[0]
    count = 1

    for s, e in intervals: 
        if s <= prev_end:
            pass
        else: 
            _, prev_end = s, e
            count += 1

    return count

