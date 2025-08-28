from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def bfs(start_state):
    visited = set()
    queue = deque()
    queue.append((start_state, [])) 

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        visited.add(state_to_tuple(current_state))
        x, y = find_blank(current_state)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                new_state = [row[:] for row in current_state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                if state_to_tuple(new_state) not in visited:
                    queue.append((new_state, path + [current_state]))

    return None 

start_state = [[1, 2, 3],
               [0, 4, 6],
               [7, 5, 8]]

solution_path = bfs(start_state)

if solution_path:
    print("Solution found in", len(solution_path) - 1, "moves:")
    for step in solution_path:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")
