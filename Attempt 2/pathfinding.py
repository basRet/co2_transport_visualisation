from collections import deque
import numpy as np

def pathfinder(grid, start, max_fuel):
    rows, cols = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    result = np.zeros_like(grid, dtype=int)

    queue = deque([(start, max_fuel)])
    visited[start] = True
    result[start] = 1

    while queue:
        pos, fuel = queue.popleft()
        x, y = pos

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny]:
                remaining_fuel = fuel - grid[nx, ny]
                if remaining_fuel >= 0:
                    visited[nx, ny] = True
                    result[nx, ny] = 1
                    queue.append(((nx, ny), remaining_fuel))

    return result