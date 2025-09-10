# return the k-largest element from an unsorted array
from heapq import heapify, heappop
def find_kth_largest(nums: list[int], k: int) -> int: 
    nums = [-x for x in nums] ## turn into max heap
    heapify(nums)

    for _  in range(k-1):
        heappop(nums)
    return -nums[0]
