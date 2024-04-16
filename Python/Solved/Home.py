def count_people(R, C, layout):
    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_people = 0

    # Create a cumulative sum matrix to efficiently calculate the number of empty spaces in a rectangle
    cumulative_sum = [[0] * (C + 1) for _ in range(R + 1)]

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if layout[i - 1][j - 1] == '.':
                cumulative_sum[i][j] = 1 + cumulative_sum[i - 1][j] + cumulative_sum[i][j - 1] - cumulative_sum[i - 1][j - 1]

    # Iterate through each empty space
    for i in range(R):
        for j in range(C):
            if layout[i][j] == '.':
                # Try placing the table starting from this empty space
                for k in range(1, min(R - i, C - j) + 1):
                    # Calculate the perimeter of the table
                    perimeter = 0
                    for dx, dy in directions:
                        x, y = i, j
                        for _ in range(2):
                            x += dx * (k - 1)
                            y += dy * (k - 1)
                            if 0 <= x < R and 0 <= y < C and layout[x][y] == '.':
                                perimeter += k
                            else:
                                break
                        dx, dy = -dy, dx  # Rotate the direction clockwise

                    max_people = max(max_people, perimeter)

    return max_people

# Input
R, C = map(int, input().split())
layout = [input() for _ in range(R)]

# Output
print(count_people(R, C, layout))
