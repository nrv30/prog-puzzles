def read_input(filepath):
    with open(filepath, "r") as f:
        return f.read().split('\n')

def advance(grid, pos):
    y, x = pos 
    if grid[y][x] == '^':
        y -= 1
    elif grid[y][x] == '<':
        x -= 1
    elif grid[y][x] == 'v':
        y += 1
    elif grid[y][x] == '>':
        x += 1
    else:
        print('error unknown option')

    return (y, x)

def abs_idx(grid, pos):
    return len(grid[0]) * pos[0] + pos[1]

def solve(grid):
    visited = [False] * (len(grid[0]) * len(grid))
    pos = (0, 0)
    visited[abs_idx(grid, pos)] = True
    while (True):
        pos = advance(grid, pos)
        idx = abs_idx(grid, pos)
        if visited[idx] == True:
            break
        visited[idx] = True

    return len([street for street in visited if street])


if __name__ == "__main__":
    print(solve(read_input("input.txt")))