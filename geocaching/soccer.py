import time

# Matrix (Início = 0)
matrix = [
    [32, 80, 19, 98, 1, 90, 14, 85],
    [66, 22, 73, 52, 72, 57, 83, 31],
    [30, 84, 41, 73, 16, 74, 45, 92],
    [77, 6, 70, 24, 0, 28, 67, 11],
    [32, 99, 44, 81, 27, 75, 42, 98],
    [68, 21, 72, 56, 59, 42, 75, 17],
    [34, 87, 19, 92, 5, 99, 27, 88],
]

ROWS = len(matrix)
COLS = len(matrix[0])

# Start position
START_ROW = 3
START_COL = 4

MOVES = 13

# Up, Down, Left, Right
DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

best_sum = float("-inf")
best_path = []

# Counters
total_paths = 0
total_states = 0


def is_valid(r, c, visited):
    return (
        0 <= r < ROWS and
        0 <= c < COLS and
        (r, c) not in visited
    )


def dfs(r, c, visited, current_sum, path, moves_left):
    global best_sum, best_path
    global total_paths, total_states

    total_states += 1

    # Mark cell as visited
    visited.add((r, c))
    path.append((r, c))
    current_sum += matrix[r][c]

    # If no more moves
    if moves_left == 0:

        total_paths += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_path = path.copy()

    else:

        # Try all directions
        for dr, dc in DIRECTIONS:

            nr = r + dr
            nc = c + dc

            if is_valid(nr, nc, visited):

                dfs(
                    nr,
                    nc,
                    visited,
                    current_sum,
                    path,
                    moves_left - 1
                )

    # Backtrack (undo move)
    visited.remove((r, c))
    path.pop()


def main():
    start_time = time.time()   # start timer

    visited = set()
    path = []

    dfs(
        START_ROW,
        START_COL,
        visited,
        0,
        path,
        MOVES
    )

    end_time = time.time()     # end timer
    elapsed_ms = (end_time - start_time) * 1000  # convert to milliseconds

    print("=" * 45)

    print("Maximum Sum:", best_sum)

    print("\nBest Path (row, col):")
    for pos in best_path:
        print(pos, end=" -> ")
    print("END")

    values = [matrix[r][c] for r, c in best_path]
    print("\nValues on Path:")
    print(values)

    print("\nSum Check:", sum(values))

    print("\n" + "=" * 45)

    print("Total completed paths:", total_paths)
    print("Total states explored:", total_states)

    print(f"Time taken: {elapsed_ms:.2f} ms")  # runtime in milliseconds

    print("=" * 45)


if __name__ == "__main__":
    main()
