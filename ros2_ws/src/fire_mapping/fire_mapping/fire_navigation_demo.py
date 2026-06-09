import heapq
import time

# 20x20 map
ROWS = 20
COLS = 20

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Obstacles
obstacles = [
    (8, 8),
    (8, 9),
    (9, 8),
    (10, 8),
    (11, 8),
]

for x, y in obstacles:
    grid[y][x] = 1

# Robot start
start = (10, 10)

# Fires: (x, y, intensity)
fires = [
    (3, 3, 2),     # Small
    (7, 15, 3),    # Medium
    (15, 5, 4)     # Large
]

# Choose highest intensity fire
target_fire = max(fires, key=lambda fire: fire[2])

goal = (target_fire[0], target_fire[1])


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

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

            if nx < 0 or nx >= COLS:
                continue

            if ny < 0 or ny >= ROWS:
                continue

            if grid[ny][nx] == 1:
                continue

            neighbor = (nx, ny)

            tentative_g = g_score[current] + 1

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

print("\nTARGET FIRE")
print(target_fire)

print("\nPATH")
print(path)

# Visualization
display = [row[:] for row in grid]

for x, y, intensity in fires:

    if intensity == 2:
        display[y][x] = "s"

    elif intensity == 3:
        display[y][x] = "m"

    elif intensity == 4:
        display[y][x] = "L"

for x, y in path:

    if (x, y) == start:
        continue

    if (x, y) == goal:
        continue

    display[y][x] = "*"

display[start[1]][start[0]] = "R"
display[goal[1]][goal[0]] = "F"

print("\n===== FIRE NAVIGATION MAP =====\n")

for row in display:

    line = ""

    for cell in row:

        if cell == 0:
            line += ". "

        elif cell == 1:
            line += "X "

        else:
            line += str(cell) + " "

    print(line)

print("\nROBOT FOLLOWING PATH\n")

for step in path:

    x, y = step

    display = [row[:] for row in grid]

    for ox, oy, intensity in fires:

        if intensity == 2:
            display[oy][ox] = "s"
        elif intensity == 3:
            display[oy][ox] = "m"
        elif intensity == 4:
            display[oy][ox] = "L"

    display[y][x] = "R"

    print("\n--------------------")

    for row in display:

        line = ""

        for cell in row:

            if cell == 0:
                line += ". "

            elif cell == 1:
                line += "X "

            else:
                line += str(cell) + " "

        print(line)

    time.sleep(1)
