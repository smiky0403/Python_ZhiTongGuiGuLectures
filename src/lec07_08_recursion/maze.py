from typing import List, Optional

def solve_maze(
    maze: List[List[str]],
    start_x: int, start_y: int,
    target_x: int, target_y: int,
    visited: List[List[bool]],
    res: List[List[str]],
    path: Optional[List[str]] = None
) -> bool:
    
    if path is None:
        path = []

    # boundary / invalid checks
    if (start_x < 0 or start_x >= len(maze) or
        start_y < 0 or start_y >= len(maze[0]) or
        maze[start_x][start_y] == 'X' or
        visited[start_x][start_y]):
        return False

    # reached target
    if start_x == target_x and start_y == target_y:
        res.append(path[:])
        return True

    # mark visited
    visited[start_x][start_y] = True

    # explore 4 directions
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    directions = ['d', 'r', 'u', 'l']
    for i in range(4):
        path.append(directions[i])
        if solve_maze(maze, start_x + dx[i], start_y + dy[i], target_x, target_y, visited, res, path):
            return True
        path.pop()
        
    visited[start_x][start_y] = False   
    return False
    

def main():
    maze = [
        ['.', 'X', '.', '.', '.', 'X'],
        ['.', '.', '.', 'X', '.', 'X'],
        ['X', 'X', '.', 'X', '.', '.'],
        ['.', 'X', 'X', 'X', '.', 'X'],
        ['.', '.', '.', '.', '.', 'X'],
        ['.', '.', '.', '.', '.', '.']
    ]

    start_x, start_y = 0, 0
    target_x, target_y = 5, 5

    visited = [[False for _ in range(len(maze[0]))]
               for _ in range(len(maze))]

    res = []
    can_reach = solve_maze(
        maze, start_x, start_y,
        target_x, target_y,
        visited, res
    )
    print("path:", res[-1] if res else None)
    print("Can reach target?", can_reach)


if __name__ == "__main__":
    main()
