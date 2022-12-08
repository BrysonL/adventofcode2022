def ingest_data_pt1():
    grid = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            row = []
            for char in line:
                row.append(int(char))

            grid.append(row)

    return grid


def count_visible_trees(grid):
    count = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

    # count left to right on each row
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if the tree is on the edge, count it
            # this saves me from some dealing with empty lists later
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid) - 1:
                count[i][j] = 1

            else:
                row = grid[i]
                col = [rw[j] for rw in grid]
                current_val = grid[i][j]
                if current_val > max(row[:j]) \
                        or current_val > max(row[j + 1:]) \
                        or current_val > max(col[:i]) \
                        or current_val > max(col[i + 1:]):
                    count[i][j] = 1

    # for row in count:
    #     print(row)

    return count


def calc_scenic_score(grid):
    score = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

    # count left to right on each row
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if the tree is on the edge, it gets score 0
            # this saves me from some dealing with empty lists later
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid) - 1:
                score[i][j] = 0

            # now we need to figure out how far it is from each tree to either an edge or the next tree of
            # at least it's height
            else:
                row = grid[i]
                col = [rw[j] for rw in grid]
                current_val = grid[i][j]
                left_count = 0
                right_count = 0
                up_count = 0
                down_count = 0

                # print(i, j)
                # check looking up
                for k in range(i-1, -1, -1):
                    grid_value = col[k]
                    up_count += 1

                    if grid_value < current_val:
                        continue
                    else:
                        # print("up",col[k:i])
                        break

                # check looking down
                for k in range(i + 1, len(grid)):
                    grid_value = col[k]
                    down_count += 1
                    if grid_value < current_val:
                        continue
                    else:
                        # print("down", col[i+1:k+1])
                        break

                # check looking left
                for k in range(j - 1, -1, -1):
                    grid_value = row[k]
                    left_count += 1
                    if grid_value < current_val:
                        continue
                    else:
                        # print("left", row[k:i])
                        break

                # check looking right
                for k in range(j + 1, len(grid)):
                    grid_value = row[k]
                    right_count += 1
                    if grid_value < current_val:
                        continue
                    else:
                        # print("right", row[i+1:k+1])
                        # print(up_count, down_count, left_count, right_count)
                        # return
                        break

                score[i][j] = left_count * right_count * up_count * down_count

    # for row in score:
    #     print(row)

    return score

if __name__ == '__main__':
    grid = ingest_data_pt1()

    # for row in grid:
    #     print(row)

    count = count_visible_trees(grid)
    print(sum(sum(row) for row in count))

    score = calc_scenic_score(grid)
    print(max(max(row) for row in score))