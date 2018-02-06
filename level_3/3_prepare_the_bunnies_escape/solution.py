def answer(maze):

    queue = []
    visited = set()
    nodes_passed = 0
    walls_passed = 0

    queue.append(((0, 0), nodes_passed + 1, walls_passed))
    visited.add((0, 0))
    while queue:
        (i, j), nodes_passed, walls_passed = queue.pop()
        if (i, j) == (len(maze), len(maze[i])):
            break
        up = (i-1, j)
        down = (i+1, j)
        left = (i, j-1)
        right = (i, j+1)
        for m, n in [up, down, left, right]:
            if 0 <= m < len(maze) and 0 <= n < len(maze[0]) and ((m, n) not in
                                                                 visited):
                if walls_passed + maze[m][n] < 2:
                    queue.insert(0, ((m, n), nodes_passed + 1, walls_passed +
                                 maze[m][n]))
                    visited.add((m, n))
    return nodes_passed
