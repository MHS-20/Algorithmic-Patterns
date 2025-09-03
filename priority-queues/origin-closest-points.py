from heapq import heappop, heappush

def  k_closest_point(points: list[list[int]], k: int) -> list[list[int]]:
    heap : list[tuple[int, list[int]]] = [] 
    res =  []
    
    for pt in points: 
        heappush(heap, (pt[0]**2 + pt[1]**2, pt))
    
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)
    return res
