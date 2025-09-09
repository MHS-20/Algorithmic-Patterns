# return if it is possible to reach the specified amount using the numbers in the array
def possible_sums(amount: int, numbers: list[int], memo: dict[int, bool]) -> bool:
    if amount == 0:
        return True

    if amount in memo:
        return memo[amount]

    for n in numbers:
        if n < amount:
            if possible_sums(amount - n, numbers, memo):
                memo[amount] = True
                return True

    memo[amount] = False
    return False
