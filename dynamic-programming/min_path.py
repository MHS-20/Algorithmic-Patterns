# min path in a 2D grid, going only down or right
def min_path(grid: list[list[int]]) -> int:
    def helper(pos: tuple[int, int], memo: dict[tuple[int, int], int]) -> int:
        i, j = pos
        
        if i >= len(grid) or j >= len(grid[0]):
            return 10000
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 0

        if pos in memo:
            return memo[pos]

        down = helper((i + 1, j), memo)
        right = helper((i, j + 1), memo)

        memo[pos] = min(down, right) + 1
        return memo[pos]

    return helper((0, 0), {})

