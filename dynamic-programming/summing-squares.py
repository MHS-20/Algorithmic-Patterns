# minimum perfect squares that sums up to the input
from math import sqrt

def summingSquares(n: int) -> int:
    def helper(n: int, memo: dict[int, int]) -> int:
        if n == 0:
            return 0

        if n in memo:
            return memo[n]

        results = []
        for i in range(1, int(sqrt(n)) + 1):
            results.append(helper(n - i * i, memo))

        memo[n] = min(results) + 1
        return memo[n]

    return helper(n, {})
