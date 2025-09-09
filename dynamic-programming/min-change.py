# Minimum number of values from an array that sum to a specified amount: 
def min_change(amount: int, coins: list[int], memo: dict[int, int]) -> int:
    if amount == 0:
        return 0

    if amount < 0:
        return -1

    if amount in memo:
        return memo[amount]

    min_coins = -1
    for c in coins:
        result = min_change(amount - c, coins, memo)
        if result != -1:
            min_coins = min(min_coins, result + 1)

    memo[amount] = min_coins
    return min_coins
