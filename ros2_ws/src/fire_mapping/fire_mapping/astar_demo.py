import heapq

# 0 = free space
# 1 = obstacle

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_score = {start: 0}

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        x, y = current

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:

            if (
                nx < 0 or nx >= rows or
                ny < 0 or ny >= cols
            ):
                continue

            if grid[nx][ny] == 1:
                continue

            tentative_g = g_score[current] + 1

            neighbor = (nx, ny)

            if (
                neighbor not in g_score or
                tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g +
                    heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_list,
                    (f_score, neighbor)
                )

    return None


path = astar(grid, start, goal)

print("Path Found:")
print(path)

display = []

for row in grid:
    display.append(row[:])

for x, y in path:

    if (x, y) == start:
        continue

    if (x, y) == goal:
        continue

    display[x][y] = "*"

display[start[0]][start[1]] = "R"
display[goal[0]][goal[1]] = "F"

print("\nMAP:\n")

for row in display:

    line = ""

    for cell in row:

        if cell == 0:
            line += ". "

        elif cell == 1:
            line += "X "

        elif cell == "*":
            line += "* "

        elif cell == "R":
            line += "R "

        elif cell == "F":
            line += "F "

    print(line)
