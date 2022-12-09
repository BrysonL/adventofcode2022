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

def move_knots(grid, instructions, starting_pos, num_lengths):
    # explicitly assign to get around alias instead of deep copy
    rope_poss = [[starting_pos[0], starting_pos[1]] for i in range(num_lengths)]

    for instruction in instructions:
        dir = instruction[0]
        moves = instruction[1]

        while moves > 0:
            moves -= 1

            # move the head knot
            if dir == 'U':
                rope_poss[0][1] += 1
            if dir == 'D':
                rope_poss[0][1] -= 1
            if dir == 'R':
                rope_poss[0][0] += 1
            if dir == 'L':
                rope_poss[0][0] -= 1

            prev_rope_dir = dir
            # decide if we need to move each length
            for i in range(1, num_lengths):
                cur_len = rope_poss[i]
                past_len = rope_poss[i-1]
                if past_len[0] - cur_len[0] > 1:  # if horiz move right needed
                    cur_len[0] += 1
                    if past_len[1] - cur_len[1] > 1:  # double diagonal up
                        cur_len[1] += 1
                    elif cur_len[1] - past_len[1] > 1:  # double diagonal down
                        cur_len[1] -= 1
                    else:  # either single diagonal or no change
                        cur_len[1] = past_len[1]

                if cur_len[0] - past_len[0] > 1:  # if horiz move left needed
                    cur_len[0] -= 1
                    if past_len[1] - cur_len[1] > 1:  # double diagonal up
                        cur_len[1] += 1
                    elif cur_len[1] - past_len[1] > 1:  # double diagonal down
                        cur_len[1] -= 1
                    else:  # either single diagonal or no change
                        cur_len[1] = past_len[1]

                if past_len[1] - cur_len[1] > 1: # if vert move up needed
                    cur_len[1] += 1
                    # double diagonal right (I think these are covered above, so this may be duplicative)
                    if past_len[0] - cur_len[0] > 1:
                        cur_len[0] += 1
                    elif cur_len[0] - past_len[0] > 1:  # double diagonal left
                        cur_len[0] -= 1
                    else: # either single diagonal or no change
                        cur_len[0] = past_len[0]

                if cur_len[1] - past_len[1] > 1: # if vert move down needed
                    cur_len[1] -= 1
                    if past_len[0] - cur_len[0] > 1:  # double diagonal right
                        cur_len[0] += 1
                    elif cur_len[0] - past_len[0] > 1:  # double diagonal left
                        cur_len[0] -= 1
                    else: # either single diagonal or no change
                        cur_len[0] = past_len[0]

            # update grid with new tail pos
            print(rope_poss)
            grid[rope_poss[-1][1]][rope_poss[-1][0]] = 1

    return grid


if __name__ == '__main__':
    grid, instructions, starting_pos = ingest_data_pt1()

    grid = move_knots(grid, instructions, starting_pos, 10)

    for line in grid:
        print(line)

    print(sum(sum(line) for line in grid))
