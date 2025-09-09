# given a grid of numbers, find the path that maximizes the sum
# from top-left corner to top-right corner, going just down or right
def max_sum_path(grid: list[list[int]]) -> int:
    def helper(grid: list[list[int]], pos: tuple[int, int], memo: dict[tuple[int, int], int]) -> int:
        i, j = pos
        if i >= len(grid) or j >= len(grid[0]):
            return -10000

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[-1][-1]

        if pos in memo:
            return memo[pos]

        down = helper(grid, (i + 1, j), memo)
        right = helper(grid, (i, j + 1), memo)

        memo[pos] = max(down, right) + grid[i][j]
        return memo[pos]
    return helper(grid, (0,0), {})


 
