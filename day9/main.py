def ingest_data_pt1():
    grid = []
    instructions = []
    vert_pos = 0
    vert_max = 0
    vert_min = 0

    horiz_pos = 0
    horiz_max = 0
    horiz_min = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split(' ')
            dir = line[0]
            moves = int(line[1])
            instructions.append([dir, moves])

            if dir == 'U':
                vert_pos += moves
            if dir == 'D':
                vert_pos -= moves

            vert_max = max(vert_pos, vert_max)
            vert_min = min(vert_pos, vert_min)

            if dir == 'R':
                horiz_pos += moves
            if dir == 'L':
                horiz_pos -= moves

            horiz_max = max(horiz_pos, horiz_max)
            horiz_min = min(horiz_pos, horiz_min)

    horiz_tot = abs(horiz_min) + horiz_max + 1  # the 1 is counting space 0
    vert_tot = abs(vert_min) + vert_max + 1
    starting_pos = [abs(horiz_min), abs(vert_min)]
    # print(instructions)
    print(horiz_min, horiz_max, vert_min, vert_max)
    print(horiz_tot, vert_tot, starting_pos)

    grid = [[0 for i in range(horiz_tot)] for j in range(vert_tot)]
    grid[starting_pos[1]][starting_pos[0]] = 1

    return grid, instructions, starting_pos

def move_knots(grid, instructions, starting_pos):
    head_pos = [starting_pos[0], starting_pos[1]]  # explicitly assign to get around alias instead of deep copy
    tail_pos = [starting_pos[0], starting_pos[1]]

    for instruction in instructions:
        dir = instruction[0]
        moves = instruction[1]

        while moves > 0:
            moves -= 1

            # move the head knot
            if dir == 'U':
                head_pos[1] += 1
            if dir == 'D':
                head_pos[1] -= 1
            if dir == 'R':
                head_pos[0] += 1
            if dir == 'L':
                head_pos[0] -= 1

            # decide if we need to move the tail
            if dir in ['U', 'D']:  # vert move
                if head_pos[1] - tail_pos[1] > 1: # head is 2 above of the tail
                    tail_pos[1] += 1
                    if tail_pos[0] != head_pos[0]: # if there is also a diagonal space, move horiz
                        tail_pos[0] = head_pos[0]
                elif tail_pos[1] - head_pos[1] > 1: # head is 2 below the tail
                    tail_pos[1] -= 1
                    if tail_pos[0] != head_pos[0]: # if there is also a diagonal space, move horiz
                        tail_pos[0] = head_pos[0]

            if dir in ['L', 'R']:  # horiz move
                if head_pos[0] - tail_pos[0] > 1: # head is 2 in front of the tail
                    tail_pos[0] += 1
                    if tail_pos[1] != head_pos[1]: # if there is also a diagonal space, move vert
                        tail_pos[1] = head_pos[1]
                elif tail_pos[0] - head_pos[0] > 1: # head is 2 behind the tail
                    tail_pos[0] -= 1
                    if tail_pos[1] != head_pos[1]: # if there is also a diagonal space, move vert
                        tail_pos[1] = head_pos[1]

            # update grid with new tail pos
            print(head_pos, tail_pos)
            grid[tail_pos[1]][tail_pos[0]] = 1

    return grid

def move_knots(grid, instructions, starting_pos):
    head_pos = [starting_pos[0], starting_pos[1]]  # explicitly assign to get around alias instead of deep copy
    tail_pos = [starting_pos[0], starting_pos[1]]

    for instruction in instructions:
        dir = instruction[0]
        moves = instruction[1]

        while moves > 0:
            moves -= 1

            # move the head knot
            if dir == 'U':
                head_pos[1] += 1
            if dir == 'D':
                head_pos[1] -= 1
            if dir == 'R':
                head_pos[0] += 1
            if dir == 'L':
                head_pos[0] -= 1

            # decide if we need to move the tail
            if dir in ['U', 'D']:  # vert move
                if head_pos[1] - tail_pos[1] > 1: # head is 2 above of the tail
                    tail_pos[1] += 1
                    if tail_pos[0] != head_pos[0]: # if there is also a diagonal space, move horiz
                        tail_pos[0] = head_pos[0]
                elif tail_pos[1] - head_pos[1] > 1: # head is 2 below the tail
                    tail_pos[1] -= 1
                    if tail_pos[0] != head_pos[0]: # if there is also a diagonal space, move horiz
                        tail_pos[0] = head_pos[0]

            if dir in ['L', 'R']:  # horiz move
                if head_pos[0] - tail_pos[0] > 1: # head is 2 in front of the tail
                    tail_pos[0] += 1
                    if tail_pos[1] != head_pos[1]: # if there is also a diagonal space, move vert
                        tail_pos[1] = head_pos[1]
                elif tail_pos[0] - head_pos[0] > 1: # head is 2 behind the tail
                    tail_pos[0] -= 1
                    if tail_pos[1] != head_pos[1]: # if there is also a diagonal space, move vert
                        tail_pos[1] = head_pos[1]

            # update grid with new tail pos
            print(head_pos, tail_pos)
            grid[tail_pos[1]][tail_pos[0]] = 1

    return grid


if __name__ == '__main__':
    grid, instructions, starting_pos = ingest_data_pt1()

    grid = move_knots(grid, instructions, starting_pos)

    for line in grid:
        print(line)

    print(sum(sum(line) for line in grid))