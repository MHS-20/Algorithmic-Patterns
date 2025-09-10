# find the pivo of the rotation

# solution: there are two sections: those greater than the last element, 
# and those smaller than the last element
# it's like finding the first true for the second condition
def find_min_rotated(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
