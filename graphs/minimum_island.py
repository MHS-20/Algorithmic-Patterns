# count the island with minimum size
def island_count(grid):
    visited = set()
    count = 10000
    num_rows = len(grid)
    num_cols = len(grid[0])

    def dfs(cell):
        count = 1
        visited.add(cell)
        for neighbor in getNeighbors(cell):
            if neighbor in visited:
                continue
            res = dfs(neighbor)
            count += res
        return count

    def getNeighbors(cell):
        delta_row = [1, 0, -1, 0]
        delta_col = [0, 1, 0, -1]
        row, col = cell
        neighbors = []
        for i in range(len(delta_row)):
            nr = row + delta_row[i]
            nc = col + delta_col[i]
            if 0 <= nr < num_rows and 0 <= nc < num_cols:
                if grid[nr][nc] == "L":
                    neighbors.append((nr, nc))
        return neighbors

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "L":
                if (i, j) in visited:
                    continue
                res = dfs((i, j))
                count = min(count, res)
    return count if count != 10000 else 0
