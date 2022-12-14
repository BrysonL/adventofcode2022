import copy

def ingest_data_pt1():
    all_rock_locations = []
    # ingest the grid and create nodes for each
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            points = line.split(' -> ')
            for i in range(len(points)):
                start_point = points[i].split(',')
                start_point = [int(start_point[0]), int(start_point[1])]
                points_to_add = []
                if i != len(points) - 1:
                    end_point = points[i+1].split(',')
                    end_point = [int(end_point[0]), int(end_point[1])]

                    max_x = max(start_point[0], end_point[0])
                    min_x = min(start_point[0], end_point[0])

                    max_y = max(start_point[1], end_point[1])
                    min_y = min(start_point[1], end_point[1])

                    points_to_add = [[x,y] for x in range(min_x, max_x + 1) for y in range(min_y, max_y+1)]

                    for point in points_to_add:
                        if point not in all_rock_locations:
                            all_rock_locations.append(point)

                    # print(points[i], points[i+1])
                    # print(points_to_add)

    return all_rock_locations

def drop_sand(drop_loc, list_in_col):
    # list_in_col is all currently occupied locations with the same x that have an item in them
    # find all locations below the dropping sand
    below_locs = [point for point in list_in_col if point[1] > drop_loc[1]]
    if len(below_locs) == 0:
        return None

    # the sand stops at one unit above (minus since higher y means below) the occupied location below it
    resting_y = min(y for [x,y] in below_locs) - 1

    return [drop_loc[0], resting_y]

def drop_all_sand(all_rock_locations):
    all_item_locations = copy.deepcopy(all_rock_locations)
    drop_x = 500
    drop_loc = [drop_x, 0]

    drop_count = 0

    while True:
        drop_count += 1
        # print('drop', drop_count)
        while True:
            list_in_col = [point for point in all_item_locations if point[0] == drop_loc[0]]
            # print('drop loc', drop_loc)
            # print('list in col', list_in_col)
            resting_place = drop_sand(drop_loc, list_in_col)
            if resting_place is None:
                # we only want to count previous drops, not the last one
                min_x = min(x for [x, y] in all_item_locations)
                max_x = max(x for [x, y] in all_item_locations)
                min_y = 0
                max_y = max(y for [x, y] in all_item_locations)

                display_grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]

                for j in range(len(display_grid)):
                    for i in range(len(display_grid[j])):
                        if [i+min_x, j] in all_rock_locations:
                            display_grid[j][i] = '#'
                        elif [i+min_x, j] in all_item_locations:
                            display_grid[j][i] = 'o'
                for row in display_grid:
                    print(''.join(row))

                return drop_count - 1

            # fall diagonal left first
            if [resting_place[0]-1, resting_place[1]+1] not in all_item_locations:
                drop_loc = [resting_place[0]-1, resting_place[1]+1]
            # then fall dignonal right
            elif [resting_place[0]+1, resting_place[1]+1] not in all_item_locations:
                drop_loc = [resting_place[0]+1, resting_place[1]+1]
            # else we've reached the final resting place
            else:
                # reset drop location
                drop_loc = [drop_x, 0]
                # break out of while loop
                break

        if resting_place == [500, 0]:
            min_x = min(x for [x, y] in all_item_locations)
            max_x = max(x for [x, y] in all_item_locations)
            min_y = 0
            max_y = max(y for [x, y] in all_item_locations)

            display_grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]

            for j in range(len(display_grid)):
                for i in range(len(display_grid[j])):
                    if [i+min_x, j] in all_rock_locations:
                        display_grid[j][i] = '#'
                    elif [i+min_x, j] in all_item_locations:
                        display_grid[j][i] = 'o'
            for row in display_grid:
                print(''.join(row))

            return drop_count

        all_item_locations.append(resting_place)

def drop_sand(drop_loc, list_in_col):
    # list_in_col is all currently occupied locations with the same x that have an item in them
    # find all locations below the dropping sand
    below_locs = [point for point in list_in_col if point[1] > drop_loc[1]]
    if len(below_locs) == 0:
        return None

    # the sand stops at one unit above (minus since higher y means below) the occupied location below it
    resting_y = min(y for [x,y] in below_locs) - 1

    return [drop_loc[0], resting_y]

def drop_all_sand(all_rock_locations):
    all_item_locations = copy.deepcopy(all_rock_locations)
    drop_x = 500
    drop_loc = [drop_x, 0]

    drop_count = 0

    while True:
        drop_count += 1
        # print('drop', drop_count)
        while True:
            list_in_col = [point for point in all_item_locations if point[0] == drop_loc[0]]
            # print('drop loc', drop_loc)
            # print('list in col', list_in_col)
            resting_place = drop_sand(drop_loc, list_in_col)
            if resting_place is None:
                # we only want to count previous drops, not the last one
                min_x = min(x for [x, y] in all_item_locations)
                max_x = max(x for [x, y] in all_item_locations)
                min_y = 0
                max_y = max(y for [x, y] in all_item_locations)

                display_grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]

                for j in range(len(display_grid)):
                    for i in range(len(display_grid[j])):
                        if [i+min_x, j] in all_rock_locations:
                            display_grid[j][i] = '#'
                        elif [i+min_x, j] in all_item_locations:
                            display_grid[j][i] = 'o'
                for row in display_grid:
                    print(''.join(row))

                return drop_count - 1

            # fall diagonal left first
            if [resting_place[0]-1, resting_place[1]+1] not in all_item_locations:
                drop_loc = [resting_place[0]-1, resting_place[1]+1]
            # then fall dignonal right
            elif [resting_place[0]+1, resting_place[1]+1] not in all_item_locations:
                drop_loc = [resting_place[0]+1, resting_place[1]+1]
            # else we've reached the final resting place
            else:
                # reset drop location
                drop_loc = [drop_x, 0]
                # break out of while loop
                break

        if resting_place == [500, 0]:
            min_x = min(x for [x, y] in all_item_locations)
            max_x = max(x for [x, y] in all_item_locations)
            min_y = 0
            max_y = max(y for [x, y] in all_item_locations)

            display_grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]

            for j in range(len(display_grid)):
                for i in range(len(display_grid[j])):
                    if [i+min_x, j] in all_rock_locations:
                        display_grid[j][i] = '#'
                    elif [i+min_x, j] in all_item_locations:
                        display_grid[j][i] = 'o'
            for row in display_grid:
                print(''.join(row))

            return drop_count

        all_item_locations.append(resting_place)


if __name__ == '__main__':
    all_rock_locations = ingest_data_pt1()

    min_x = min(x for [x,y] in all_rock_locations) - 1000
    max_x = max(x for [x,y] in all_rock_locations) + 1000

    y_floor = max(y for [x,y] in all_rock_locations) + 2

    # add the floor (no need to check if already there since we're past the max)
    floor_points = [[x, y_floor] for x in range(min_x, max_x + 1)]
    for point in floor_points:
        all_rock_locations.append(point)


    # print(all_rock_locations)

    sand_drops = drop_all_sand(all_rock_locations)
    print(sand_drops)