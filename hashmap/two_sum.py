# return indices of the two numbers such that they add up to target.
def two_sum(arr: list[int], target: int) -> list[int]: 
    num_to_index = {}

    for i, num in enumerate(arr): 
        complement = target - num

        if complement in num_to_index: 
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

