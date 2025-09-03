## not diagonally, just cardinal directions

from collections import deque


def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) ->  list[list[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)): 
            neighbor_row  = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if  0 <= neighbor_row < num_rows and  0 <= neighbor_col < num_cols: 
                if  image[neighbor_row][neighbor_col] == color: 
                    yield neighbor_row , neighbor_col

    def bfs(root): 
        queue = deque([root])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] =  replacement
        visited[r][c] = True

        while len(queue) > 0: 
            node = queue.popleft()
            for neighbor in  get_neighbors(node, color): 
                r, c = neighbor
                if visited[r][c]: 
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited[r][c] =  True

    bfs((r,c))
    return image

