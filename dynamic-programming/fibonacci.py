def fibonacci(n: int, memo: dict[int, int]) -> int:
    if n == 1 or n == 0:
        return n

    if n in memo:
        return memo[n]

    result: int = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result
