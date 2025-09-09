# Give the number of ways that is possible to make the input using elements from an array. 
# An element can be used multiple times, but avoid dulicate solutions in which jsut changes the order. 

def counting_change(amount: int, coins: list[int])->int: 
    def helper(amount: int, coins: list[int], index: int, memo: dict[tuple[int, int], int])->int:
        if amount == 0: 
            return  1

        if index >= len(coins):
            return 0

        if (amount, index) in memo: 
            return memo[(amount, index)]

        value = coins[index]
        tot, qty = 0, 0
        while qty * value < amount:
            subamount = amount - qty*value
            tot += helper(subamount, coins, index+1, memo)
            qty += 1
        memo[(amount, index)] = tot
        return tot
    return helper(amount, coins, 0, {})
