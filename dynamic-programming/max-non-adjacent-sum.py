# find the max sum of non adjacent element of an array
def non_adjacent(nums: list[int]) -> int:
    def helper(i: int, memo: dict[int, int]) -> int:
        # se sono oltre la fine, non ci sono più numeri
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        skip = helper(i + 1, memo)
        take = nums[i] + helper(i + 2, memo)

        memo[i] = max(skip, take)
        return memo[i]

    return helper(0, {})
