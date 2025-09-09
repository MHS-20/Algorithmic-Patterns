# counting the number of possible path from top-left corner to bottom-right corner
def count_path(grid: list[list[int]]) -> int:
    def counting_paths(
        grid: list[list[int]], pos: tuple[int, int], memo: dict[tuple[int, int], int]) -> int:
        i, j = pos
        if i >= len(grid) or j >= len(grid[0]):
            return 0

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1

        if pos in memo:
            return memo[pos]

        down = counting_paths(grid, (i + 1, j), memo)
        right = counting_paths(grid, (i, j + 1), memo)

        memo[pos] = down + right
        return memo[pos]

    return counting_paths(grid, (0, 0), {})
