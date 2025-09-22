# given an array of N nums, find the one that appears more than N/2 times
def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Verify (if needed)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None
