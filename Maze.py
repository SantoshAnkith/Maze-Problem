maze = [
    [' ','#',' ',' ',' ',' '],
    [' ','#',' ','#','#',' '],
    [' ','#',' ',' ','#',' '],
    [' ',' ','#',' ',' ',' '],
    ['#',' ','#',' ','#',' '],
    [' ',' ',' ','#',' ',' ']
]

n = len(maze)
path = []

def solve(r, c):
    if r == n-1 and c == n-1:
        path.append((r, c))
        return True
    if r < 0 or c < 0 or r >= n or c >= n or maze[r][c] == '#' or maze[r][c] == '.':
        return False
    maze[r][c] = '.'
    path.append((r, c))
    if solve(r+1, c) or solve(r, c+1) or solve(r-1, c) or solve(r, c-1):
        return True
    path.pop()
    return False

if solve(0, 0):
    print(path)
else:
    print("No path found")